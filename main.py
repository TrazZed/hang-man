from hangman.ui import start, run_game

def main():
    file_path, max_attempts = start()
    run_game(file_path, max_attempts)

if __name__ == "__main__":
    main()