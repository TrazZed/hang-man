import os

def load_words(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    with open(file_path, 'r') as file:
        words = file.read().splitlines()
    return words

if __name__ == "__main__":
    # Test the loader
    file_path = 'data/5000-more-common.txt'
    try:
        words = load_words(file_path)
        print(f"Loaded {len(words)} words.")
    except FileNotFoundError as e:
        print(e)