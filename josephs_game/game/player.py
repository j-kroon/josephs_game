class Player:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        self.inventory = []
        self.current_location = None

    def move_to(self, new_location):
        self.current_location = new_location
        print(f"{self.name} moves to {new_location.name}")
        print(new_location.description)

    def pick_up(self, item):
        if item in self.current_location.items:
            self.inventory.append(item)
            self.current_location.items.remove(item)
            print(f"{self.name} picks up {item.name}")
        else:
            print(f"{item.name} is not here")

    def use_item(self, item):
        if item in self.inventory:
            print(f"{self.name} uses {item.name}")
            # Apply item effects here
            self.inventory.remove(item)
        else:
            print(f"{item.name} is not in the inventory")

    def examine_item(self, item):
        if item in self.inventory:
            print(f"Examining {item.name}: {item.description}")
        else:
            print(f"{item.name} is not in the inventory")

    def show_inventory(self):
        if self.inventory:
            print(f"{self.name}'s inventory:")
            for item in self.inventory:
                print(f"- {item.name}: {item.description}")
        else:
            print(f"{self.name}'s inventory is empty")


