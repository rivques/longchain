from longchain.core.agentaction import AgentAction
from longchain.core.dataclasses import NextAction, PathResult


class ChangePathAction(AgentAction):
    def __init__(self, dest: str, next_action: NextAction = 'player') -> None:
        self.next_action = next_action
        self.dest = dest
        
    async def run(self, path, player, player_actions):
        return PathResult(next_action=self.next_action, new_path_id=self.dest, messages=[])

class RemovePlayerAction(AgentAction):
    async def run(self, path, player, player_actions):
        return PathResult(next_action='player', new_path_id=None, messages=[], remove_this_player=True)