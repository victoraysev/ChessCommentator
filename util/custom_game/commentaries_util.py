from openai import OpenAI
import os

def mock_commentary():
    reader = open('util/custom_game/mock/output_commentaries.txt', 'r')
    # reader = open('output_commentaries.txt', 'r')
    return reader.read()


def get_commentary_list_and_hashtags(pgn, api_key="", debug=False):
    if int(debug):
        raw_commentary = mock_commentary()
    else:
         raw_commentary = generate_commentary(pgn, api_key)
    return parse_as_array_and_hashtags(raw_commentary)

def generate_commentary(pgn, api_key=""):
    #api_key = os.getenv("GPT_API_KEY")
    client = OpenAI(api_key = api_key)
    # Prepare the prompt for OpenAI API
    prompt = (
        f"You are a chess commentator. This is a chess game with the following pgn:\n{pgn}\n"
        "Provide commentary for the most critical 5 moves (they dont have to be consecutive and one of them must be the latest move) and create 3 hashtags after that for the general "
        "game. "
        "Do not make up any moves or details beyond what is provided."
        "Use user names of the players given when commenting.\n"
        "Provide line by line commentary in the following format:\n"
        "<black or white according to user name),<move_number>,<commentary>\n"
        "After the game end, provide 3 hashtags separated by commas.\n"
    )

    # OpenAI API call
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-3.5-turbo",
        temperature=0.7,
        max_tokens=250,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Extract the generated commentary and hashtags
    commentary_and_hashtags = response.choices[0].message.content
    return commentary_and_hashtags



def parse_as_array_and_hashtags(raw_commentary):
    commentary_list = {}
    for line in raw_commentary.strip().split('\n'):
        if not line.strip() or line.startswith('#'):
            continue
        parts = line.split(',', 2)
        move_number = int(parts[1])
        commentary = f"{move_number}: {parts[2]}"
        commentary_list[move_number] = parts[0], commentary

    # Printing the array to verify
    return commentary_list, raw_commentary.strip().split('\n')[-1]



