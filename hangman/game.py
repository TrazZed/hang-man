class HangmanGame:
    def __init__(self, secret, max_attempts=6):
        self.secret = secret.lower() #Ensure the secret word is in lowercase
        self.max_attempts = max_attempts  
        self.guesses = []
        self.wrong = []

    def guess(self, letter):
        letter = letter.lower()
        if letter in self.guesses:
            return False
        if letter not in self.secret:
            self.wrong.append(letter)
        return letter in self.secret

    def masked(self):
        return ''.join(letter if letter in self.guesses else '_' for letter in self.secret)
    
    def attempts_left(self):
        return self.max_attempts - len(self.wrong)
    
    def is_won(self):
        return all(letter in self.guesses for letter in self.secret)
    
    def is_lost(self):
        return len(self.wrong) >= self.max_attempts
    
    def is_over(self):
        return self.is_won() or self.is_lost()
