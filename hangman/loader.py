import os

def load_files(directory='data'):
    if not os.path.exists(directory):
        raise FileNotFoundError(f"The directory {directory} does not exist.")
    files = [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    return files

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