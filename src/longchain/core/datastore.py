from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional, TYPE_CHECKING

if TYPE_CHECKING: # only import classes used for typing when type checking, to avoid a circular dependency
    from longchain.core.dataclasses import Player

class Datastore(ABC):
    @abstractmethod
    async def get_player_by_id(self, player_id: str) -> Optional[Player]:
        pass
    
    @abstractmethod
    async def get_player_by_interaction_id(self, interaction_id: Any) -> Optional[Player]:
        pass

    @abstractmethod
    async def remove_player(self, player_id: str):
        pass

    @abstractmethod
    async def save_player(self, player: Player):
        pass