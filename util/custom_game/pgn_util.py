# pgn_util.py
import re

import requests
import streamlit as st


def get_game_data(game_id, api_token):
    pgn = fetch_pgn_data(game_id, api_token)
    return parse_pgn_after_opening(pgn)

def fetch_pgn_data(game_id, api_token):
    url = f"https://lichess.org/game/export/{game_id}"
    headers = {"Authorization": f"Bearer {api_token}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        st.error(f"Failed to fetch PGN data: {response.status_code} {response.reason}")
        return None

def parse_pgn_after_opening(pgn):
    # Define the patterns using regular expressions
    opening_pattern = re.compile(r'(\[Opening ".*"\]\s*.*)', re.DOTALL)
    white_pattern = re.compile(r'\[White "(.*?)"\]')
    black_pattern = re.compile(r'\[Black "(.*?)"\]')

    # Search for the opening pattern in the text
    opening_match = opening_pattern.search(pgn)
    white_match = white_pattern.search(pgn)
    black_match = black_pattern.search(pgn)

    if opening_match and white_match and black_match:
        # Extract the combined opening info and the text after it
        combined_result = opening_match.group(1)
        white_username = white_match.group(1)
        black_username = black_match.group(1)
        return f"{combined_result}\nWhite: {white_username}\nBlack: {black_username}", white_username, black_username
    else:
        print("No opening or usernames found")
        return None, None, None

