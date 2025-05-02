from hangman.game import HangmanGame
from hangman.loader import load_files, load_words

def start():
    """
    Start the game by loading available word list files and getting user input for the selected file and maximum attempts.

    Returns:
    - file_path: The path to the selected word list file.
    - max_attempts: The maximum number of attempts allowed for the game.
    """
    files = load_files()
    print("Available word list files:")
    for i, file in enumerate(files):
        print(f"{i + 1}: {file}")
    choice = int(input("Choose a file by number: ")) - 1
    while choice < 0 or choice >= len(files):
        print("Invalid choice.")
        choice = int(input("Choose a file by number: ")) - 1
    file_path = files[choice]
    print(f"Selected file: {file_path}")
    max_attempts = int(input("Enter the maximum number of attempts: ").strip())
    return file_path, max_attempts

def run_game(file_path, max_attempts):
    """
    Run the Hangman game with the specified word list file and maximum attempts.
    
    Arguments:
    - file_path: The path to the word list file.
    - max_attempts: The maximum number of attempts allowed for the game.
    """
    words = load_words(file_path)
    game = HangmanGame(words, max_attempts)
    while not game.is_over():
        print(game.masked())
        print(f"Wrong Answers: {', '.join(game.wrong)}")
        print(f"Attempts left: {game.attempts_left()}")
        letter = input("Guess a letter: ").strip().lower()
        game.process_guess(letter)
    if game.is_won():
        print(f"Congratulations! You won. The word was '{game.secret}'.")
    else:
        print(f"Game over. You lost. The word was '{game.secret}'.")
