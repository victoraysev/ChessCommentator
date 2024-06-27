import io
import chess.pgn
import chess.svg
import streamlit as st


def draw_board():
    board = st.session_state.board
    moves = st.session_state.moves
    move_index = st.session_state.move_index
    move_index = move_index + 1 if move_index == len(moves) else move_index
    for move in moves[:move_index]:
        board.push(move)
    board_svg = chess.svg.board(board=board)
    st.markdown(f'<div style="text-align: center;">{board_svg}</div>', unsafe_allow_html=True)


