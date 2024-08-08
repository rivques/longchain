from collections.abc import Sequence
from longchain.core.actionresolver import ActionResolver
from longchain.core.dataclasses import Message, PathResult, Player, PlayerAction

class Path:
    def __init__(self, id: str, starts_without_player_action: bool, action_resolver: ActionResolver):
        self.id = id
        self.starts_without_player_action = starts_without_player_action
        self.action_resolver = action_resolver

    async def tick(self, player: Player, player_actions: Sequence[PlayerAction]) -> PathResult:
        result = PathResult(next_action='player', new_path_id=None, messages=[])
        try:
            actions = await self.action_resolver.tick(player, player_actions)
        except Exception as e:
            return PathResult(error=e, next_action='player', new_path_id=None, messages=[Message(text=f"An error occurred while attempting to get an action with {self.action_resolver.__class__.__name__}: {e}", interaction_id=player.interaction_id)])
        for action in actions:
            try:
                path_result = await action.run(self, player, player_actions)
            except Exception as e:
                return PathResult(error=e, next_action='player', new_path_id=None, messages=[Message(text=f"An error occurred while attempting to run a(n) {action.__class__.__name__}: {e}", interaction_id=player.interaction_id)])
            if path_result.error:
                return path_result
            result.messages.extend(path_result.messages)
            result.next_action = path_result.next_action
            result.remove_this_player |= path_result.remove_this_player
            if path_result.new_path_id is not None:
                result.new_path_id = path_result.new_path_id
        return result