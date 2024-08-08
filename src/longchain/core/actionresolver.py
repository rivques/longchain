from __future__ import annotations
from abc import ABC, abstractmethod
from collections.abc import Sequence

from typing import TYPE_CHECKING
if TYPE_CHECKING: # only import classes used for typing when type checking, to avoid a circular dependency
    from longchain.core.agentaction import AgentAction
    from longchain.core.dataclasses import Player, PlayerAction


class ActionResolver(ABC):
    @abstractmethod
    async def tick(self, player: Player, player_actions: Sequence[PlayerAction]) -> Sequence[AgentAction]:
        pass