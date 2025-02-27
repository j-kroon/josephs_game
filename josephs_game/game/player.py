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

class Game:
    def __init__(self, player_name):
        self.player = Player(player_name)
        self.locations = self.load_locations(location_data)

    def load_locations(self, data):
        locations = {}
        for location in data['locations']:
            items = [Item(**item) for item in location['items']]
            exits = location['exits']
            locations[location['id']] = Location(location['id'], location['name'], location['description'], items, exits)
        return locations

    def start(self):
        self.player.current_location = self.locations['location_1']
        self.player.move_to(self.player.current_location)
        self.main_loop()

    def main_loop(self):
        while True:
            command = input("\nEnter a command: ")
            self.process_command(command)

    def process_command(self, command):
        if command.startswith('move '):
            direction = command.split(' ')[1]
            self.move_player(direction)
        elif command.startswith('pick up '):
            item_name = command.split(' ')[2:]
