import json

from util.popular_game.util_popular_games import process


def mock_get_popular_games():
    # Read JSON data from file
    #with open('./mock/db_games.json', 'r') as file:
    with open('./util/popular_game/mock/db_games.json', 'r') as file:
        json_data = json.load(file)
    return process(json_data)
#mock_get_popular_games()