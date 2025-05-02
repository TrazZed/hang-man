import os


def load_files(directory='data'):
    """
    Load all files from the specified directory.
    Arguments:
    - directory: The directory to load files from. Default is 'data'.

    Returns:
    - A list of file paths in the specified directory.

    Raises:
    - FileNotFoundError: If the directory does not exist.
    """
    if not os.path.exists(directory):
        raise FileNotFoundError(f"The directory {directory} does not exist.")
    files = [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    return files

def load_words(file_path):
    """
    Load words from a specified file.

    Arguments:
    - file_path: The path to the file containing words.

    Returns:
    - A list of words loaded from the file.

    Raises:
    - FileNotFoundError: If the file does not exist.
    """
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