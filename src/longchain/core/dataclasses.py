from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from typing import Any, Literal, Optional


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
    messages: Sequence[Message]
    is_error: bool = False

@dataclass
class Player:
    id: str
    current_path: str
    name: str
    interaction_id: str
    path_states: Mapping[str, dict]
    messager_state: dict

@dataclass
class PlayerAction:
    name: str
    data: dict