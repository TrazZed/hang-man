# Hangman Game

A simple terminal-based Hangman game written in Python. The game selects a random word from a list of common English words and allows the user to guess letters until the word is revealed or guesses run out.

## Features

- Random word selection from a curated list of common English words
- Interactive command-line UI
- Modular code structure with separate components for game logic, word loading, and UI

## Project Structure
    data/
      5000-more-common.txt         # Word list used for gameplay
    hangman/
      game.py                      # Core game logic
      loader.py                    # Word list loader
      ui.py                        # Text-based user interface
    main.py                        # Entry point of the application

## Usage

To start the game, run:

```bash
python main.py
```

## References
Word list - https://github.com/MichaelWehar/Public-Domain-Word-Lists
