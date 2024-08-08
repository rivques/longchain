from longchain.core.actionresolver import ActionResolver
from longchain.core.dataclasses import Player
from longchain.impl.agentaction.message import MessageAgentAction
from longchain.plugins.bag.bag import bag_instance

class StakeActionResolver(ActionResolver):
    def __init__(self, items: list[tuple[str, int]]):
        self.items = items
    
    async def tick(self, player, player_actions):
        # stake_status can be null (in which case we send an offer), "sent_offer" (in which case we wait for the player to accept the offer), or "accepted" (in which case we continue with the quest).
        if "stake_status" not in player.path_states[player.current_path]:
            player.path_states[player.current_path] = {"stake_status": "sent_offer"}
            message = f"This quest requires you to stake some items to play it. Depending on what you do, you may get some, all, or none of them back. Check your DMs with Bag and accept the offer from <@{bag_instance.owner_id}> to continue."
            message += "\n\nItems to stake:"
            for item in self.items:
                message += f"\n{item[1]}x {item[0]}"
            message += "Once you have accepted the offer, send another message here."
            return [MessageAgentAction(message=message)]
        return [MessageAgentAction(message="Staking functionality has not yet been implemented")]