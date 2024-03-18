
class Inventory:
    def __init__(self) -> None:
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)


    def display_inventory(self):
        if not self.items:
            print("Your inventory is empty.")
        else:
            print("Inventory :")
            for item in self.items:
                print(f"- {item.name} : {item.description}")

class Shop_Category(Inventory):
    def __init__(self) -> None:
        super().__init__()

    def display_inventory(self):
        i = 0
        if not self.items:
            print("The shop is empty.")
        else:
            print("Shop :")
            for item in self.items:
                i += 1
                print(f"{i}.  {item.name} : {item.description} price = {item.value} golds")

class Chest(Inventory):
    def __init__(self) -> None:
        super().__init__()
