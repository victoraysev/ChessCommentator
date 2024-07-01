import os

import requests

from util.presaved_game.util_presaved_games import process


def get_presaved_games(number_of_tries = 0):
    url = "https://ic7gx2rb29.execute-api.us-east-1.amazonaws.com/prod/games"
    api_key = os.environ.get("API_GATEWAY_TOKEN")  # Replace with your actual API key

    headers = {
        "x-api-key": api_key
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()  # Assuming the response is in JSON format
        return process(data)
    elif number_of_tries < 3:
        get_presaved_games(number_of_tries + 1)
    else:
        print(f"Failed to retrieve data after {number_of_tries} tries: {response.status_code}")
        return f"Failed to retrieve data: {response.status_code}"


print(get_presaved_games())