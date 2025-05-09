import sys
from PyQt6.QtWidgets import QApplication, QWidget
from gui import Ui_Form
from tic_tac_toe import TicTacToeLogic

class TicTacToeGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.logic = TicTacToeLogic()
        self.connect_buttons()
        self.ui.restart_button.clicked.connect(self.restart_game)

    def connect_buttons(self):
        for row in range(3):
            for col in range(3):
                button = self.ui.buttons[row][col]
                button.clicked.connect(lambda _, r=row, c=col: self.handle_move(r, c))

    def handle_move(self, row, col):
        if self.logic.make_move(row, col):
            self.ui.buttons[row][col].setText(self.logic.current_player)
            winner = self.logic.check_winner()
            if winner:
                self.ui.winner_label.setText(f"Player {winner} wins!")
                self.disable_buttons()
            elif self.logic.is_full():
                self.ui.winner_label.setText("It's a draw!")
            else:
                self.logic.switch_player()
                self.ui.status_label.setText(f"Player {self.logic.current_player}'s turn")

    def disable_buttons(self):
        for row in self.ui.buttons:
            for button in row:
                button.setEnabled(False)

    def restart_game(self):
        self.logic.reset_game()
        for row in self.ui.buttons:
            for button in row:
                button.setText("")
                button.setEnabled(True)
        self.ui.status_label.setText(f"Player {self.logic.current_player}'s turn")
        self.ui.winner_label.setText("")

def main():
    app = QApplication(sys.argv)
    window = TicTacToeGUI()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

