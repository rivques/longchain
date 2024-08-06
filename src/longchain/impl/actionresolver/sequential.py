from typing import Literal
from longchain.core.agentaction import AgentAction
from longchain.core.actionresolver import ActionResolver
from longchain.core.dataclasses import Player

# Calls all its arguments in order, then goes to the player (by default.)
# Usually, should end with a ChangePathAction.
class SequentialActionResolver(ActionResolver):
    def __init__(self, *actions: AgentAction, on_end: Literal['go_to_player', 'repeat_from_start'] = 'go_to_player'):
        self.actions = actions
        self.on_end = on_end
    async def tick(self, player, player_actions) -> AgentAction:
        action_number = player.path_states[player.current_path]["action_number"]
        if action_number >= len(self.actions):
            raise ValueError("No more actions to run")
        action = self.actions[action_number]
        player.path_states[player.current_path]["action_number"] += 1
        action.next_action = "agent" if action_number < len(self.actions) - 1 or self.on_end == 'repeat_from_start' else "player"
        # call the next agent (ususally us) unless this is the last action and we're supposed to go to the player
        return action