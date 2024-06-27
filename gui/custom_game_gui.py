import io
import os

import chess
import streamlit as st

from initializer import initialize_game
from util.custom_game.commentaries_util import get_commentary_list_and_hashtags
from util.custom_game.pgn_util import get_game_data

def tab_custom_game(tab):
    debug = os.environ.get("DEBUG", False)
    with tab:
        st.write("Enter the game ID:")
        game_id = st.text_input("Game ID", value="JnpPNq5i")
        lichess_api_token = os.getenv("LICHESS_API_TOKEN")

        gpt_api_token = None
        if st.checkbox("Show commentary analysis", value=True):
            st.write("Enter the API token (OPENAI):")
            gpt_api_token = st.text_input("API token")

        if st.button("Fetch and Show Game"):
            if not lichess_api_token:
                st.error("API token is missing. Please set the LICHESS_API_TOKEN environment variable.")
            else:
                pgn_data, white_user, black_user = get_game_data(game_id, lichess_api_token)
                pgn_game = chess.pgn.read_game(io.StringIO(pgn_data))

                commentary_list, hashtags = get_commentary_list_and_hashtags(pgn_data, gpt_api_token, debug)
                if pgn_data:
                    initialize_game(pgn_game, white_user, black_user, commentary_list, hashtags)
                else:
                    st.error("Failed to fetch PGN data. Please check the game ID and try again.")
