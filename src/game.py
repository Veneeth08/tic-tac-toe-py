import os
from board import Board
from player import HumanPlayer

class Game:
    def __init__(self):
        self.board = Board()
        self.player_X = HumanPlayer("X")
        self.player_O = HumanPlayer("O")
        self.current_player = self.player_X

    def display_title(self):
        print("========================")
        print("      TIC TAC TOE")
        print("========================")

    def get_move(self):
        while True:
            pos = self.current_player.get_move(self.board)

            pos -= 1

            if not self.board.make_move(pos, self.current_player.symbol):
                print("Position already occupied")
                continue

            return

    def switch_player(self):
        if self.current_player == self.player_X:
            self.current_player = self.player_O
        else:
            self.current_player = self.player_X

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