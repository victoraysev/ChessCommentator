import chess
import io
from gtts import gTTS
import streamlit as st


def text_to_speech(text, filename="comment.mp3"):
    tts = gTTS(text=text, lang='en')
    tts.save(filename)
    return filename


def draw_sidebar():
    if st.sidebar.button("Next Move"):
        if st.session_state.move_index < len(list(st.session_state.pgn_game.mainline_moves())):
            st.session_state.move_index += 1
    if st.sidebar.button("Previous Move"):
        if st.session_state.move_index > 0:
            st.session_state.move_index -= 1

    commentary_list = st.session_state.commentary_list
    moves = st.session_state.moves
    move_index = st.session_state.move_index
    st.sidebar.write(f"Move {(move_index + 1) // 2}/ {(len(moves) + 2 - 1) // 2}")
    st.sidebar.write(f"White: {st.session_state.white_user}")
    st.sidebar.write(f"Black: {st.session_state.black_user}")

    if ((move_index + 1) // 2) in commentary_list:
        player, comment = commentary_list[(move_index + 1) // 2]
        if ((move_index + 1) % 2 == 0 and player == "white") or ((move_index + 1) % 2 == 1 and player == "black"):
            st.sidebar.write(f"Comment: {comment}")
            if st.sidebar.button("Play Comment"):
                audio_file = text_to_speech(comment)
                audio_bytes = open(audio_file, 'rb').read()
                st.sidebar.audio(audio_bytes, format='audio/mp3')


def draw_finished_sidebar():
    if st.sidebar.button("Next Move"):
        if st.session_state.move_index < len(list(st.session_state.pgn_game.mainline_moves())) - 1:
            st.session_state.move_index += 1
    if st.sidebar.button("Previous Move"):
        if st.session_state.move_index > 0:
            st.session_state.move_index -= 1

    game = st.session_state.game
    hashtags = st.session_state.hashtags
    result = game.headers["Result"]
    if result == "1-0":
        result_string = f"White:{st.session_state.white_user} wins!"
    elif result == "0-1":
        result_string = f"Black:{st.session_state.black_user} wins!"
    else:
        result_string = "Draw!"
    st.sidebar.write("Game over!")
    st.sidebar.write(result_string)
    st.sidebar.write(hashtags)
