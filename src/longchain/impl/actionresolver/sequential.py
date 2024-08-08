from typing import Literal
from longchain.core.agentaction import AgentAction
from longchain.core.actionresolver import ActionResolver
from longchain.core.dataclasses import Player

# Calls all its arguments in order, then goes to the player (by default.)
# Usually, should end with a ChangePathAction.
class SequentialActionResolver(ActionResolver):
    def __init__(self, *actions: AgentAction):
        self.actions = actions
    async def tick(self, player, player_actions):
        return list(self.actions)