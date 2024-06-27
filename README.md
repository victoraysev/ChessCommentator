# Chess Commentator

Welcome to Chess Commentator, a Python-based application built with Streamlit that provides insightful commentary on chess games. This project uses the Lichess API to fetch game data, the ChatGPT API to generate commentary, and a Spring Boot application deployed on AWS Lambda to fetch popular chess games and their commentaries.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **Game Analysis**: Fetch and analyze chess games using the Lichess API.
- **Insightful Commentary**: Receive detailed commentary on the strategic aspects of the game, generated by the ChatGPT API.
- **Popular Games**: Fetch popular chess games and their commentaries from a Spring Boot application deployed on AWS Lambda.
- **Easy to Use**: Simple and user-friendly interface built with Streamlit.
- **Extensible**: Easily extendable to support more features in the future.

## Installation

### Prerequisites

- Python 3.7 or higher
- pip
- OpenAI API key

### Steps

1. **Clone the repository**:
    ```bash
    git clone https://github.com/utkuaysev/ChessCommentator.git
    cd ChessCommentator
    ```

2. **Create and activate a virtual environment (optional but recommended)**:
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up your environment variables**:
    - Create a `.env` file in the root directory of the project and add your OpenAI API key:
      ```plaintext
      API_GATEWAY_TOKEN=<>
      LICHESS_API_TOKEN=<>
      ```

## Usage

1. **Run the Streamlit app**:
    ```bash
    streamlit run app.py
    ```

2. **Fetch a Chess Game**:
    - Use the app interface to enter game ID to fetch and analyze the game.

3. **Fetch Popular Games**:
    - Use the app interface to fetch popular chess games and their commentaries from the AWS Lambda,DynamoDB powered Spring Boot application.

4. **View Commentary**:
    - The application will provide detailed commentary for each move in the game, generated by the ChatGPT API.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

### Steps to Contribute

1. **Fork the repository**.

2. **Create a new branch**:
    ```bash
    git checkout -b feature/YourFeatureName
    ```

3. **Make your changes**.

4. **Commit your changes**:
    ```bash
    git commit -m "Add your feature description"
    ```

5. **Push to the branch**:
    ```bash
    git push origin feature/YourFeatureName
    ```

6. **Open a pull request**.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please reach out to:

- Utku Aysev
- [GitHub Profile](https://github.com/utkuaysev)
