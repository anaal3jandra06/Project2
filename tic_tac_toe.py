class TicTacToeLogic:
    def __init__(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

    def make_move(self, row: int, col: int) -> bool:
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            return True
        return False

    def check_winner(self) -> str:
        b = self.board
        for i in range(3):
            if b[i][0] == b[i][1] == b[i][2] != "":
                return b[i][0]
            if b[0][i] == b[1][i] == b[2][i] != "":
                return b[0][i]
        if b[0][0] == b[1][1] == b[2][2] != "":
            return b[0][0]
        if b[0][2] == b[1][1] == b[2][0] != "":
            return b[0][2]
        return ""

    def is_full(self) -> bool:
        return all(cell != "" for row in self.board for cell in row)

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def reset_game(self):
        self.__init__()

