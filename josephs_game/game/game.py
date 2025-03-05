from josephs_game.game.inventory import Item
from josephs_game.game.location import Location
from utils.parser import load_data
from game.player import Player
class Game:
    def __init__(self, player_name, data):
        self.player = Player(player_name)
        self.locations = self.load_data(data)

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