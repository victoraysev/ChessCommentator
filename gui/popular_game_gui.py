from initializer import initialize_game
from util.popular_game.api_popular_games import get_popular_games
import streamlit as st



def tab_popular_game(tab):
    with tab:
        st.write("Select a popular game:")
        #games_mock = mock_get_popular_games()
        if "game_from_api" not in st.session_state:
            games = get_popular_games()
            st.session_state.game_from_api = games
        else:
            games = st.session_state.game_from_api
        game_options = {
            f"{game[1]} vs {game[2]} ({game[0].headers._tag_roster['Date']})": game[0].headers._tag_roster["Event"] for
            game in games}
        selected_game = st.selectbox("Popular Games", options=list(game_options.keys()))
        if st.button("Show Selected Game"):
            selected_game_id = game_options[selected_game]
            game_res = {}
            for game in games:
                if game[0].headers._tag_roster['Event'] == selected_game_id:
                    game_res = game
                    break
            initialize_game(game_res[0], game_res[1], game_res[2], game_res[4], game_res[3])
