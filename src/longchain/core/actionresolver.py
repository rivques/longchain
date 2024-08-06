from abc import ABC, abstractmethod
from collections.abc import Sequence

from longchain.core.agentaction import AgentAction
from longchain.core.dataclasses import Player, PlayerAction


class ActionResolver(ABC):
    @abstractmethod
    async def tick(self, player: Player, player_actions: Sequence[PlayerAction]) -> AgentAction:
        pass