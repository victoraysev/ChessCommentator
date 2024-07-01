import json

from util.presaved_game.util_presaved_games import process


def mock_get_presaved_games():
    # Read JSON data from file
    #with open('./mock/db_games.json', 'r') as file:
    with open('./util/presaved_game/mock/db_games.json', 'r') as file:
        json_data = json.load(file)
    return process(json_data)
#mock_get_presaved_games()