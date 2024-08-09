# longchain
## Usage
* `Quest` - The main object. Ititialize it, then call `asyncio.run(quest.run())` to run it.
* `Path` - A Path is one "step" in a player's experience. 
* `ActionResolver` - This is the real decision-making part of the `Path`. The two main ones are the `SequentialActionResolver`, which takes several `Action`s and just runs them in order, and the `LlmActionResolver`, which uses an LLM to decide what to do.
  * `starts_without_player_action` - If this parameter is `True`, then a `ChangePathAction` with `next_action='path'` can immediately call this `ActionResolver` without waiting for player input.
* `AgentAction` - This is a single step a path takes. It's something like sending a message or moving to another path. They have a `next_action` parameter which controls whether the player is prompted for an input or not before the next action happens.
* `core` vs `impl` vs `plugins` - `core` is the main part of the library, `impl` is the implementation of the `core` interfaces, and `plugins` are more niche implementations. For example, the path following code is in `core`, the `LlmActionResolver` is in `impl`, and the Bag utilities are in `plugins`.
* `Datastore` - This is an interface for the quest to keep player state. The only one currently implemented is `jsonfile`, but another one could be implemented for a database or something.
* `Messager` - Like Datastore, this is an abstraction layer that allows the quest to send messages to the player. The only one currently implemented is `slack`.
* `LlmActionResolver` - There's a lot here so it gets its own bullet point. The LLM automatically talks to the player, and you can add `LlmTool`s in the `agent_actions` parameter to allow it to do more. The `system_prompt` parameter can either be a string or a callable taking an `LlmContext`. This allows the system prompt to change based on what's going on, which is recommended (LLMs are not good at keeping information secret).
  * `LlmTool` - These describe an action the LLM can take. `description` should tell the LLM when to call the tool. `params` is a list of `LlmToolParam`s, which have a `name` and a `schema` (which is a JSON Schema object).  `available` and `action` are callables that take an `LlmContext` and return a boolean and an `AgentAction` respectively. `available` should return `True` if the tool can be used, and `action` should return the `AgentAction` to take if the tool is used. These both get `LlmContext`s, and `action` also gets a `dict` of the params the LLM called the action with. `strict` can turn on structured output, which forces the LLM's output to conform to the `params` perfectly but disables some JSON Schema properties. [See more in the OpenAI docs.](https://platform.openai.com/docs/guides/function-calling/function-calling-with-structured-outputs). If `strict` is off, don't trust the LLM to call your function correctly.

### Example
There is an example project in the [examples folder](https://github.com/rivques/longchain/tree/main/examples/sockthief).
## Development
### to build:
```
.\venv\Scripts\activate
py -m build
python -m twine upload dist/*
```
### to regenerate the bag api:
1. download the update bag.proto
2. `pip install grpcio grpcio_tools`
3. run `cd .\src\longchain\plugins\bag\api\`
4. run `python -m grpc_tools.protoc -I . --grpc_python_out . --python_out . --pyi_out . bag.proto`
5. Go to the generated bag_pb2_grpc.py and change the `bag_pb2` import to `import longchain.plugins.bag.api.bag_pb2 as bag__pb2`
## Naming
It's a tool for making _long chains_ of NPC interactions.