from __future__ import annotations
from abc import abstractmethod, ABC
from collections.abc import Sequence

from typing import TYPE_CHECKING
if TYPE_CHECKING: # only import classes used for typing when type checking, to avoid a circular dependency
    from longchain.core.dataclasses import NextAction, PathResult, Player, PlayerAction
    from longchain.core.path import Path

class AgentAction(ABC):
    _next_action: NextAction = 'player'
    # this gurantees to ActionResolvers that they can set the next action if they want to
    @property
    def next_action(self) -> NextAction:
        return self._next_action
    @next_action.setter
    def next_action(self, value: NextAction):
        self._next_action = value

    @abstractmethod
    async def run(self, path: Path, player: Player, player_actions: Sequence[PlayerAction]) -> PathResult:
        pass