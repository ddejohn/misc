from random import shuffle


class Hangman:
    """A simple hangman game"""
    def __init__(self):
        self.wordlist = self.load_wordlist()
        self.lives: int
        self.secret: str
        self.hidden_word: str
        self.guessed: str
        self.new_game()

    def new_game(self):
        self.lives = 6
        self.secret = self.get_new_word()
        self.hidden_word = "_" * len(self.secret)
        self.guessed = ""
        self.game_loop()

    def game_loop(self):
        while True:
            guess = self.get_input()
            self.verify_guess(guess)
            if self.hidden_word == self.secret or not self.lives:
                break
        if self.game_over():
            self.new_game()
        else:
            print("Thanks for playing!")

    def load_wordlist(self):
        with open("hangman/wordlist.txt") as words:
            wordlist = words.read().split()
            shuffle(wordlist)
        return wordlist

    def get_new_word(self):
        return self.wordlist.pop()

    def game_over(self):
        if not self.lives:
            print("Game over!\n")
        elif self.hidden_word == self.secret:
            print(f"\nYou won! The word was {self.secret}!")

        while True:
            choices = {"y": True, "n": False}
            play_again = input("Would you like to play again? (y/n)\n > ")
            new_game = choices.get(play_again, 9999)
            if new_game == 9999:
                print("Invalid input!\n")
                continue
            return new_game

    def get_indices(self, letter):
        return [idx for idx, char in enumerate(self.secret) if letter == char]

    def fill_letter(self, letter, indices):
        enum = enumerate(self.hidden_word)
        chars = [letter if idx in indices else char for idx, char in enum]
        self.hidden_word = "".join(chars)

    def get_input(self):
        while True:
            guess = input("Guess a letter\n > ")
            if not guess.isalpha() or len(guess) != 1:
                print("\nThat is not a valid alphabetic character!\n")
                continue
            elif guess in self.guessed:
                print("\nYou already guessed that letter!")
                print(f"Guessed letters: {self.guessed}\n")
                continue
            return guess

    def verify_guess(self, guess):
        if guess in self.secret:
            self.fill_letter(guess, self.get_indices(guess))
            print(f"\nGood guess! Hidden word: {self.hidden_word}\n")
        else:
            self.guessed += guess
            self.lives -= 1
            print(f"\nSorry, '{guess}' is not in the secret word!'")
            print(f"You have {self.lives} lives left!")
            print(f"Guessed letters: {self.guessed}\n")
