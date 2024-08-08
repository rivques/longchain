from collections.abc import Sequence
from dataclasses import dataclass
from typing import Literal, Optional


@dataclass
class Message:
    text: str
    interaction_id: str
    icon: Optional[str] = None
    name: Optional[str] = None

NextAction = Literal['player', 'path']
@dataclass
class PathResult:
    next_action: NextAction
    new_path_id: Optional[str]
    messages: list[Message]
    error: Optional[Exception] = None
    remove_this_player: bool = False

@dataclass
class Player:
    id: str
    current_path: str
    name: str
    interaction_id: str
    path_states: dict[str, dict]
    messager_state: dict
    plugin_state: dict[str, dict]

@dataclass
class PlayerAction:
    name: str
    data: dict