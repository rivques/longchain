from __future__ import annotations
from abc import ABC, abstractmethod
from collections.abc import Sequence, Callable, Awaitable
from typing import Never, TYPE_CHECKING

if TYPE_CHECKING: # only import classes used for typing when type checking, to avoid a circular dependency
    from longchain.core.dataclasses import Message, Player, PlayerAction

class Messager(ABC):
    @abstractmethod
    async def send_messages(self, messages: Sequence[Message], do_send_message_hint: bool):
        pass
    @abstractmethod
    async def start(self, tick: Callable[[Player, Sequence[PlayerAction]], Awaitable[None]], start_interaction: Callable[[Player], Awaitable[None]]) -> Never:
        # this function is called and should never return. it needs to configure itself to call tick whenever
        # a player takes an action and start_interaction whenever a new player starts an interaction.
        # it also needs to handle verifying that the player isn't trying to start a second simultaneous interaction
        pass