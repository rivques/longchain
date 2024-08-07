from collections.abc import Sequence
from longchain.core.actionresolver import ActionResolver
from longchain.core.dataclasses import Message, PathResult, Player, PlayerAction

class Path:
    def __init__(self, id: str, starts_without_player_action: bool, action_resolver: ActionResolver):
        self.id = id
        self.starts_without_player_action = starts_without_player_action
        self.action_resolver = action_resolver

    async def tick(self, player: Player, player_actions: Sequence[PlayerAction]) -> PathResult:
        try:
            action = await self.action_resolver.tick(player, player_actions)
        except Exception as e:
            return PathResult(error=e, next_action='player', new_path_id=None, messages=[Message(text=f"An error occurred while attempting to get an action with {self.action_resolver.__class__.__name__}: {e}", interaction_id=player.interaction_id)])
        try:
            path_result = await action.run(self, player, player_actions)
        except Exception as e:
            return PathResult(error=e, next_action='player', new_path_id=None, messages=[Message(text=f"An error occurred while attempting to run a(n) {action.__class__.__name__}: {e}", interaction_id=player.interaction_id)])
        return path_result