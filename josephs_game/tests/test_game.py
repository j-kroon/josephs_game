import pytest
from unittest.mock import MagicMock, patch

# Assuming Player, Item, Location, utils are defined in the same module as Game
from josephs_game.game import player, inventory, location, runner
from utils.parser import load_data

@pytest.fixture
def some_game():
    mock_player = MagicMock(spec=player.Player)
    mock_load_data = patch('utils.parser.load_data', return_value={
        'locations': [
            {
                'id': 'location_1',
                'name': 'Starting Point',
                'description': 'The beginning of the adventure.',
                'items': [],
                'exits': []
            }
        ]
    }).start()
    some_game = runner.Runner('Player1', 'data_file')
    yield some_game
    patch.stopall()

def test_init(some_game):
    assert isinstance(runner.player, player.Player)
    assert 'location_1' in runner.locations

def test_load_locations(some_game):
    data = {
        'locations': [
            {
                'id': 'location_2',
                'name': 'Second Place',
                'description': 'Another location.',
                'items': [{'name': 'item1', 'description': 'Item 1 description'}],
                'exits': []
            }
        ]
    }
    locations = some_game.load_locations(data)
    assert 'location_2' in locations
    assert isinstance(locations['location_2'], location.Location)

@patch('builtins.input', side_effect=['move north', 'pick up item'])
@patch.object(runner.Runner, 'process_command', wraps=runner.Runner.process_command)
def test_main_loop(mock_input, mock_process_command, some_game):
    some_game.main_loop()
    assert mock_process_command.call_count == 2

def test_process_command(some_game):
    some_game.move_player = MagicMock()
    some_game.process_command('move north')
    some_game.move_player.assert_called_with('north')