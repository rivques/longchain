from longchain.core.agentaction import AgentAction
from longchain.core.dataclasses import PathResult


class ChangePathAction(AgentAction):
    async def __init__(self, dest: str) -> None:
        self.next_action = "player"
        self.dest = dest
        
    async def run(self, path, player, player_actions):
        return PathResult(next_action=self.next_action, new_path_id=self.dest, messages=[])