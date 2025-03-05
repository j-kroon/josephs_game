from josephs_game.game.runner import Game
def main():
    print("Welcome to the Adventure Game!")
    location_data = "./josephs_game/data/location_data.json"
    game = Game("Joseph", location_data)
    game.start()

if __name__ == "__main__":
    main()
