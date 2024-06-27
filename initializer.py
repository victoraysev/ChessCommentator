import chess
import streamlit as st
import io
def initialize_game(pgn_game, white_user, black_user, commentary_list, hashtags):
    st.session_state.pgn_game = pgn_game
    st.session_state.white_user = white_user
    st.session_state.black_user = black_user
    st.session_state.commentary_list = commentary_list
    st.session_state.hashtags = hashtags
    st.session_state.move_index = 0
    st.rerun()

def initialize_board():
    game = st.session_state.pgn_game
    st.session_state.board = game.board()
    st.session_state.moves = list(game.mainline_moves())
    st.session_state.game = game
