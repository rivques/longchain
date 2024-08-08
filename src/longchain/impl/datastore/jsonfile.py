from collections.abc import Sequence
import json
import os
from longchain.core.dataclasses import Player
from longchain.core.datastore import Datastore


class JsonFileDatastore(Datastore):
    def __init__(self, path: str):
        self.path = path
        self.players: list[Player] = []
        # try to load the file, and if it doesn't exist, create it
        file_data = ""
        try:
            with open(self.path, 'r') as f:
                file_data = f.read()
        except FileNotFoundError:
            print(f"File not found: {os.path.abspath(self.path)}. Creating...")
            # make sure the directory exists
            os.makedirs(os.path.dirname(self.path), exist_ok=True)
            with open(self.path, 'w') as f:
                f.write('[]')
                file_data = "[]"
        try:
            self.players = [Player(**player_data) for player_data in json.loads(file_data)]
        except json.JSONDecodeError:
            print(f"Error reading JSON from {os.path.abspath(self.path)}")
            raise            
        
    async def save_player(self, player):
        # remove the player if it already exists
        await self.remove_player(player.id)
        self.players.append(player)
        with open(self.path, 'w') as f:
            f.write(json.dumps([player.__dict__ for player in self.players], indent=4))

    async def get_player_by_id(self, player_id):
        for player in self.players:
            if player.id == player_id:
                return player
        return None

    async def get_player_by_interaction_id(self, interaction_id):
        for player in self.players:
            if player.interaction_id == interaction_id:
                return player
        return None

    async def remove_player(self, player_id):
        self.players = [player for player in self.players if player.id != player_id]
        with open(self.path, 'w') as f:
            to_write = json.dumps([player.__dict__ for player in self.players], indent=4)
            f.write(to_write)