import os
from board import Board

class Game:
    def __init__(self):
        self.board = Board()
        self.current_symbol = "X"

    def display_title(self):
        print("========================")
        print("      TIC TAC TOE")
        print("========================")

    def get_move(self):
        while True:
            try:
                pos = int(
                    input(
                        f"Player {self.current_symbol}, "
                        "choose a position (1-9): "
                    )
                )
            except ValueError:
                print("Invalid input. Please enter a number from 1 to 9")
                continue

            if pos < 1 or pos > 9:
                print("Invalid position. Please enter a number from 1 to 9")
                continue

            pos -= 1

            if not self.board.make_move(pos, self.current_symbol):
                print("Position already occupied")
                continue

            return

    def switch_player(self):
        if self.current_symbol == "X":
            self.current_symbol = "O"
        else:
            self.current_symbol = "X"

    def play(self):
        while True:
            os.system("clear")
            self.display_title()
            self.board.display()

            self.get_move()

            winner = self.board.check_winner()

            if winner is not None:
                os.system("clear")
                self.display_title()
                self.board.display()
                print(f"Player {winner} wins!")
                break

            if self.board.is_full():
                os.system("clear")
                self.display_title()
                self.board.display()
                print("It's a draw!")
                break

            self.switch_player()