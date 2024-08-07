from typing import Literal
from longchain.core.agentaction import AgentAction
from longchain.core.actionresolver import ActionResolver
from longchain.core.dataclasses import Player

# Calls all its arguments in order, then goes to the player (by default.)
# Usually, should end with a ChangePathAction.
class SequentialActionResolver(ActionResolver):
    def __init__(self, *actions: AgentAction):
        self.actions = actions
    async def tick(self, player, player_actions) -> AgentAction:
        if player.current_path not in player.path_states:
            player.path_states[player.current_path] = {"action_number": 0}
        action_number = player.path_states[player.current_path]["action_number"]
        if action_number >= len(self.actions):
            raise ValueError("No more actions to run")
        action = self.actions[action_number]
        player.path_states[player.current_path]["action_number"] += 1
        if action_number < len(self.actions) - 1:
            action.next_action = "agent"
        # ^ call the next agent (ususally us) unless this is the last action and we're supposed to go to the player
        if action_number == len(self.actions) - 1:
            player.path_states[player.current_path]["action_number"] = 0
            # prepare to go back to the start if we're repeating
        print(f"Running action {action_number} of {len(self.actions)} for player {player.name}. The next action is {player.path_states[player.current_path]['action_number']}. The action is {action.__class__.__qualname__}.")
        return action