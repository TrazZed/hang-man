class HangmanGame:
    """
    A class representing the Hangman game.
    
    Attributes:
    - secret: The secret word to guess.
    - max_attempts: The maximum number of incorrect attempts allowed.
    - guesses: A list of letters guessed by the player.
    - wrong: A list of incorrect guesses.
    """
    def __init__(self, secret, max_attempts):
        """
        Initialize the Hangman game with a secret word and maximum attempts.
        
        Arguments:
        - secret: The secret word to guess.
        - max_attempts: The maximum number of incorrect attempts allowed.
        """
        self.secret = secret.lower() #Ensure the secret word is in lowercase
        self.max_attempts = max_attempts  
        self.guesses = []
        self.wrong = []

    def guess(self, letter):
        """
        Check if the guessed letter is in the secret word.

        Arguments:
        - letter: The letter guessed by the player.

        Returns:
        - True if the letter is in the secret word, False otherwise.
        - If the letter has already been guessed, return False.
        """
        letter = letter.lower()
        if letter in self.guesses:
            return False
        if letter not in self.secret:
            self.wrong.append(letter)
        return letter in self.secret

    def masked(self):
        """
        Return a masked version of the secret word, showing guessed letters and underscores for unguessed letters.

        Returns:
        - A string representing the masked word, with guessed letters revealed and unguessed letters replaced by underscores.
        """
        return ''.join(letter if letter in self.guesses else '_' for letter in self.secret)
    
    def attempts_left(self):
        """
        Return the number of attempts left.

        Returns:
        - An integer representing the number of incorrect attempts left.
        """
        return self.max_attempts - len(self.wrong)
    
    def is_won(self):
        """
        Return True if the player has guessed all letters in the secret word.

        Returns:
        - True if all letters in the secret word have been guessed, False otherwise.
        """
        return all(letter in self.guesses for letter in self.secret)
    
    def is_lost(self):
        """
        Return True if the player has used up all attempts.

        Returns:
        - True if the number of incorrect attempts has reached the maximum allowed, False otherwise.
        """
        return len(self.wrong) >= self.max_attempts
    
    def is_over(self):
        """
        Return True if the game is over (either won or lost).

        Returns:
        - True if the game is over (either won or lost), False otherwise.
        """
        return self.is_won() or self.is_lost()
