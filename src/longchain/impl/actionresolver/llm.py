from __future__ import annotations
from collections.abc import Callable, Sequence
from dataclasses import dataclass
import json
from typing import Awaitable, Optional, Union, cast
from longchain.core.actionresolver import ActionResolver
from longchain.core.path import Path
try:
    from openai import AsyncOpenAI
    from openai.types.chat.chat_completion_message_param import ChatCompletionMessageParam
    from openai.types.chat.chat_completion_tool_param import ChatCompletionToolParam
    from openai._types import NOT_GIVEN, NotGiven
except ImportError:
    raise ImportError("Llm features must use the `llm` extra.")

from longchain.core.agentaction import AgentAction
from longchain.core.dataclasses import Player, PlayerAction
from longchain.impl.agentaction.message import MessageAgentAction

@dataclass
class LlmToolResult:
    agent_actions: list[AgentAction]
    model_feedback: str

@dataclass
class LlmTool:
    name: str
    description: str
    params: list[LlmToolParam]
    available: Union[Callable[[LlmContext], bool], Callable[[LlmContext], Awaitable[bool]]]
    action: Union[Callable[[LlmContext, dict]], Callable[[LlmContext, dict], Awaitable[LlmToolResult]]]
    strict: bool = False # Whether to enable structured output. More: https://platform.openai.com/docs/guides/function-calling/function-calling-with-structured-outputs

@dataclass
class LlmToolParam:
    name: str
    schema: dict

@dataclass
class LlmContext:
    player: Player
    player_actions: Sequence[PlayerAction]

class OpenAIActionResolver(ActionResolver):
    def __init__(self, openai_token, system_prompt: Union[str, Callable[[LlmContext], str], Callable[[LlmContext], Awaitable[str]]], agent_actions: list[LlmTool]=[], model="gpt-4o-mini", openai_base_url=None, name=None, icon_url=None, preload_messages: Optional[list[ChatCompletionMessageParam]]=None, max_convo_length=50):
        self.client = AsyncOpenAI(api_key=openai_token, base_url=openai_base_url)
        self.model = model
        self.system_prompt = system_prompt
        self.name = name
        self.agent_actions = agent_actions
        self.icon_url = icon_url
        self.preload_messages = preload_messages if preload_messages is not None else []
    
    async def tick(self, player, player_actions):
        if player.current_path not in player.path_states:
            player.path_states[player.current_path] = {"messages": self.preload_messages.copy()}
        for action in player_actions:
            if action.name == "say":
                player.path_states[player.current_path]["messages"].append({"role": "user", "content": action.data["message"]})
        if player.path_states[player.current_path]["messages"]:
            last_message = player.path_states[player.current_path]["messages"][-1]
            if last_message["role"] == "assistant":
                raise ValueError("Assistant cannot respond twice in a row. Check that tools executed correctly and that the messager had some player actions.")
        context = LlmContext(player=player, player_actions=player_actions)
        if callable(self.system_prompt):
            system_prompt = self.system_prompt(context)
            if isinstance(system_prompt, Awaitable):
                system_prompt = await system_prompt
        else:
            system_prompt = self.system_prompt
        messages: list[ChatCompletionMessageParam] = [{"role": "system", "content": system_prompt}]
        messages.extend(player.path_states[player.current_path]["messages"])

        tools: Union[list[ChatCompletionToolParam], NotGiven] = []
        for tool in self.agent_actions:
            tool_available = tool.available(context)
            if isinstance(tool_available, Awaitable):
                tool_available = await tool_available
            if not tool_available:
                continue
            tools.append({
                "type": "function",
                "function": {
                    "name": tool.name,
                    "description": tool.description,
                    "parameters": {
                        "type": "object",
                        "properties": {param.name: param.schema for param in tool.params}
                    }
                },
                "strict": tool.strict # type: ignore the openai lib hasn't updated to include this value
            })
        if len(tools) < 1:
            tools = NOT_GIVEN

        response = await self.client.chat.completions.create(model=self.model, messages=messages, tools=tools)
        
        result = []
        if len(response.choices) < 1:
            raise ValueError(f"OpenAI response error: {json.dumps(response)}")
        if response.choices[0].message.content is not None:
            result.append(MessageAgentAction(message=response.choices[0].message.content, name=self.name, icon_url=self.icon_url))
            player.path_states[player.current_path]["messages"].append({"role": "assistant", "content": response.choices[0].message.content})
        if response.choices[0].message.tool_calls is not None:
            for tool_call in response.choices[0].message.tool_calls:
                player.path_states[player.current_path]["messages"].append(tool_call.to_dict(mode='json'))
                our_tool = next((tool for tool in self.agent_actions if tool.name == tool_call.function.name), None)
                if our_tool is None:
                    # the ai called a tool we don't have, so we'll just ignore it
                    continue
                tool_available = our_tool.available(context)
                if isinstance(tool_available, Awaitable):
                    tool_available = await tool_available
                if not tool_available:
                    # the tool is not available, so we'll ignore it
                    continue

                tool_result = our_tool.action(context, json.loads(tool_call.function.arguments))
                if isinstance(tool_result, Awaitable):
                    tool_result = await tool_result
                result.extend(tool_result.agent_actions)
                player.path_states[player.current_path]["messages"].append({"role": "tool", "content": tool_result.model_feedback})

        return result