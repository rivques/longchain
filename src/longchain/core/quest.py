from collections.abc import Sequence
from longchain.core.dataclasses import Message, PathResult, Player, PlayerAction
from longchain.core.datastore import Datastore
from longchain.core.messager import Messager
from longchain.core.path import Path

class Quest:
    def __init__(self, name: str, paths: Sequence[Path], message_sender: Messager, datastore: Datastore):
        self.name = name
        self.first_path = paths[0].id
        self.paths = {path.id: path for path in paths}
        self.messager = message_sender
        self.datastore = datastore
        if not paths[0].starts_without_player_action:
            raise ValueError("The first path in a quest must start without a player action")
    
    async def tick(self, player: Player, player_actions: Sequence[PlayerAction]):
        ready_to_end = False
        messages: list[Message] = []
        while not ready_to_end: # loop until a path asks for a player action
            current_path = self.paths[player.current_path] # get the path the player is on
            path_result: PathResult = await current_path.tick(player, player_actions) # run that path
            messages.extend(path_result.messages) # add any messages it generated to the queue
            ready_to_end = path_result.next_action == 'player' # if the path asks for a player action, we're done
            if path_result.new_path_id: # if the path changed:
                # check that the new path exists
                if path_result.new_path_id not in self.paths:
                    messages.append(Message(text=f"Error: tried to switch to new path {path_result.new_path_id}, but it does not exist", interaction_id=player.interaction_id))
                    ready_to_end = True
                    break
                player.current_path = path_result.new_path_id # update the player's current path
                if self.paths[player.current_path].starts_without_player_action:
                    # this path needs a player action to start, so we don't care if the previous path asked for anther agent turn
                    ready_to_end = True
        await self.messager.send_messages(messages)
        self.datastore.save_player(player)
    
    async def start_interaction(self, player: Player):
        player.current_path = self.first_path
        await self.tick(player, [])

    async def run(self):
        await self.messager.start(self.tick, self.start_interaction)