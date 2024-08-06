from abc import ABC, abstractmethod
from typing import Any, Optional

from longchain.core.dataclasses import Player

class Datastore(ABC):
    @abstractmethod
    def get_player_by_id(self, player_id: Any) -> Optional[Player]:
        pass
    
    @abstractmethod
    def get_player_by_interaction_id(self, interaction_id: Any) -> Optional[Player]:
        pass

    @abstractmethod
    def remove_player(self, player_id: Any):
        pass

    @abstractmethod
    def save_player(self, player: Player):
        pass