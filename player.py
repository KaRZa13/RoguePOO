class Player:

    def __init__(self, name, base_hp, base_atk, ):
        self.name = name
        self.max_hp = base_hp
        self.base_atk = base_atk
        self.hp = self.max_hp
        self.atk = self.base_atk
