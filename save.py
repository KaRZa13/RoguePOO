import json
from character import *
from init import *

class Save:
    def __init__(self, file_name) -> None:
        self.file_name = file_name

    @staticmethod
    def get_attack(name):
        return all_attacks["attack1"].get(name) and all_attacks["attack2"].get(name)

    def save_run(self, player):
        data_player = {
            "name": player.name,
            "hp": player.hp,
            "max_hp": player.max_hp,
            "armor": player.armor,
            "attack1": player.attack1,
            "attack2": player.attack2,
            "gold": player.gold,
            "char_class": player.char_class,
            "inventaire": [item.__dict__ for item in player.inventory.items]
        }
        with open(self.file_name, 'w') as f:
            json.dump(data_player, f, indent=4)

    def load_save(self):
        with open(self.file_name, 'r') as f:
            data_player = json.load(f)

        player = globals()[data_player["char_class"]](
            data_player["name"],
            data_player["max_hp"],
            data_player["armor"],
            data_player["gold"],)

        attack1 = self.get_attack(data_player["attack1"])
        attack2 = self.get_attack(data_player["attack2"])
        player.attack1 = attack1
        player.attack2 = attack2

        player.hp = data_player["hp"]

        for item_data in data_player["inventaire"]:
            item_class = globals()[item_data["class"]]
            item = item_class(**item_data)
            player.inventory.add_item(item)

        return player