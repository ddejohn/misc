"""An nxn Tic-Tac-Toe game"""


class TicTacToe:
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
