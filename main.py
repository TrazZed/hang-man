from hangman.loader import load_files
from hangman.ui import run_game

def main():
    files = load_files()
    print("Available word list files:")
    for i, file in enumerate(files):
        print(f"{i + 1}: {file}")
    choice = int(input("Choose a file by number: ")) - 1
    if choice < 0 or choice >= len(files):
        print("Invalid choice.")
        return
    file_path = files[choice]
    print(f"Selected file: {file_path}")
    max_attempts = int(input("Enter the maximum number of attempts: ").strip())
    run_game(file_path, max_attempts)

if __name__ == "__main__":
    main()