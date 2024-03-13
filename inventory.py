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

