import chess.pgn
import io

def process(json_data):
    # Assuming json_data contains a single game, extract the necessary data
    games_data = json_data  # Since json_data is now the dictionary itself, not a list

    # Extract PGN data and convert it to a chess.pgn.Game object
    result = []
    for game in games_data:
        pgn_data = game["pgn"]
        pgn_game = chess.pgn.read_game(io.StringIO(pgn_data.replace("\\n", "\n").replace('\\"', '"')))

        # Extract players
        white_player = game["players"]["white"]
        black_player = game["players"]["black"]

        # Extract hashtags
        hashtags = game["hashtags"]

        # Parse the commentaries
        commentaries_list = game["commentaries"]
        converted_commentaries_dict = {int(comment["number"]): [comment["color"], comment["text"]] for comment in commentaries_list}

        # Print the resulting variables
        result.append((pgn_game, white_player, black_player, hashtags, converted_commentaries_dict))
    return result
