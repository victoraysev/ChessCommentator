import os

import streamlit as st
from gui.board_gui import draw_board
from gui.custom_game_gui import tab_custom_game
from gui.popular_game_gui import tab_popular_game
from gui.sidebar_gui import draw_sidebar, draw_finished_sidebar
from initializer import initialize_board


def main():
    st.session_state.debug = os.environ.get("DEBUG", False)
    if "pgn_game" not in st.session_state:
        st.title("Chess Game Viewer")
        # Create tabs
        tab1, tab2 = st.tabs(["Custom Game", "Popular Game"])
        # calls initialize_game function
        tab_custom_game(tab1)
        tab_popular_game(tab2)
    else:
        # calls initialize_board function
        initialize_board()
        move_index = st.session_state.move_index
        moves = st.session_state.moves
        if move_index > len(moves) - 1:
            draw_finished_sidebar()
        else:
            draw_sidebar()
        draw_board()
if __name__ == "__main__":
    main()
