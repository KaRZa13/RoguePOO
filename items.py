class Items:
    def __init__(self, name, description, durability, value, drop_chance, tier) -> None:
        self.name = name
        self.durability = durability
        self.description = description
        self.value = value
        self.drop_chance = drop_chance
        self.tier = tier


class Weapons(Items):
    def __init__(self, name, description, durability, value, drop_chance, tier, attack_modifier) -> None:
        super().__init__(name, description, durability, value, drop_chance, tier)
        self.attack_modifier = attack_modifier


class Armor(Items):
    def __init__(self, name, description, durability, value, drop_chance, tier, armor_modifier) -> None:
        super().__init__(name, description, durability, value, drop_chance, tier)
        self.armor_modifier = armor_modifier


class Potion(Items):
    def __init__(self, name, description, durability, value, drop_chance, amount, tier, type_potion) -> None:
        super().__init__(name, description, durability, value, drop_chance, tier)
        self.amount = amount
        self.type_potion = type_potion
        # self.mana = mana
        # self.health = health

