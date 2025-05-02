import random
from hangman.game import HangmanGame
from hangman.loader import load_words

def run_game(file_path, max_attempts):
    words = load_words(file_path)
    secret = random.choice(words)
    game = HangmanGame(secret, max_attempts)
    while not game.is_over():
        print(game.masked())
        print(f"Wrong Answers: {', '.join(game.wrong)}")
        print(f"Attempts left: {game.attempts_left()}")
        letter = input("Guess a letter: ").strip().lower()
        if len(letter) != 1:
            print("Enter exactly one letter.")
            continue
        if letter in game.guesses:
            print("You've already guessed that letter.")
            continue
        correct = game.guess(letter)
        game.guesses.append(letter)
        print("Correct!" if correct else "Wrong!")

    if game.is_won():
        print(f"Congratulations! You won. The word was '{game.secret}'.")
    else:
        print(f"Game over. You lost. The word was '{game.secret}'.")
