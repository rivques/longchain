from collections.abc import Callable, Sequence
from typing import Awaitable, Union
from longchain.core.agentaction import AgentAction
from longchain.core.dataclasses import PathResult, Player, PlayerAction
from longchain.core.path import Path

class ArbitraryAgentAction(AgentAction):
    def __init__(self, run: Union[Callable[[Path, Player, Sequence[PlayerAction]], PathResult], Callable[[Path, Player, Sequence[PlayerAction]], Awaitable[PathResult]]]) -> None:
        self.run_func = run

    async def run(self, path, player, player_actions):
        result = self.run_func(path, player, player_actions)
        if isinstance(result, Awaitable):
            return await result
        return result
