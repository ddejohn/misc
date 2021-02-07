import re
from random import shuffle, randint


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


class TicTacToe:
    """An nxn Tic-Tac-Toe game"""
    def __init__(self, size=4):
        self.size = size
        self.board = [["."]*size for _ in range(size)]
        self.coords = [(i, j) for i in range(size) for j in range(size)]
        self.player = self.xo_switch()

    def __str__(self):
        header = "   " + "  ".join(str(i) for i in range(self.size))
        board = "\n".join(f"{i}".ljust(3) + "  ".join(r) for i, r in enumerate(self.board))
        return f"\n{header}\n{board}\n"

    def xo_switch():
        """Switches between 'X' and 'O'"""
        switch = 88
        while True:
            yield chr(switch)
            switch = switch ^ (79 ^ 88)

    def winner(self) -> tuple:
        n = self.size
        X = ["X"]*n
        O = ["O"]*n

        rows = self.board.copy()
        cols = [[rows[i][j] for i in range(n)] for j in range(n)]
        prim_diag = [rows[i][i] for i in range(n)]
        sec_diag = [rows[n-1-i][i] for i in range(n)]
        all_conds = [*rows, *cols, prim_diag, sec_diag]

        if X in all_conds:
            return "X"
        elif O in all_conds:
            return "O"
        return ""


    def place_piece(self, row, col) -> bool:
        if row > self.size - 1 or col > self.size - 1:
            print("\nThe board isn't that big!")
        elif (row, col) not in self.coords:
            print("\nThat spot is already filled!")
        else:
            self.board[row][col] = next(self.player)
            self.coords.remove((row, col))
            print(self)
            winner = self.winner()
            if winner:
                print(f"Game over! Winner: {winner}!")
                return True

        if not self.coords:
            print("Game over!")
            return True
        return False


    def get_input():
        while True:
            coord = input("Choose coordinates as row, col or quit (q)\n > ")
            if coord == "q":
                quit()
            try:
                row, col = coord.split(",")
                return int(row), int(col)
            except ValueError:
                print("Invalid input!\n")


def get_dice() -> str:
    print("Input dice roll as <num dice>d<num sides>\ne.g.: 2d6 to roll a six-sided die twice.")
    while True:
        roll = input("\n > ").strip()
        if re.match("^0d0$", roll):
            print("That's not how that works! That's not how any of this works!")
            continue
        elif re.match(r"0{1}d\d*", roll):
            print("You rolled zero dice. Outstanding move!")
            continue
        elif re.match(r"\d*d[01]{1}$", roll):
            _, d = roll.split("d")
            print(f"There's no such thing as a {d}-sided die, you absolute walnut.")
            continue
        elif not re.match(r"[1-9]+\d*d[1-9]+\d*", roll):
            print("Invalid roll! Must be of the form <num dice>d<num sides>, like 5d20, or 1d6.")
            continue
        return roll


def dice_roller():
    roll = get_dice()
    n, d = map(int, roll.split("d"))
    if d == 2:
        total = sum(randint(1, d) - 1 for _ in range(n))
        coin_coins = "coin" if n == 1 else "coins"
        print(f"\nYou flipped {n} {coin_coins}\nHeads: {total}\nTails: {n - total}")
    else:
        total = sum(randint(1, d) for _ in range(n))
        die_dice = "die" if n == 1 else "dice"
        print(f"\nYou rolled {n} {d}-sided {die_dice}\nTotal: {total}")
    return total


if __name__ == "__main__":
    games = {
        "hangman": Hangman,
        "tic-tac-toe": TicTacToe
    }

    # while True:
    #     size = input("Choose board size (2-10):\n > ")
    #     try:
    #         size = int(size)
    #         if size in range(2, 11):
    #             break
    #         print("Invalid board size!")
    #     except ValueError:
    #         print("Invalid input!")

    # B = TicTacToe(size)
    # game_over = False

    # while not game_over:
    #     row, col = B.get_input()
    #     game_over = B.place_piece(row, col)
