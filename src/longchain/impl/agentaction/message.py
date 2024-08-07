from typing import Optional
from longchain.core.agentaction import AgentAction
from longchain.core.dataclasses import Message, NextAction, PathResult


class MessageAgentAction(AgentAction):
    def __init__(self, message: str, name: Optional[str] = None, icon_url: Optional[str] = None, next_action: NextAction = 'player') -> None:
        self.message = message
        self.name = name
        self.icon_url = icon_url
        self.next_action = next_action

    async def run(self, path, player, player_actions):
        return PathResult(next_action=self.next_action, new_path_id=None, messages=[Message(text=self.message, interaction_id=player.interaction_id, icon=self.icon_url, name=self.name)])