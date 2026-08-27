import numpy as np

class Player:
    def __init__ (self, symbol):
        self.symbol = symbol

    def get_move(self, board):
        raise NotImplementedError("This method should be overridden by subclasses")

class HumanPlayer(Player):
    def get_move(self, board):
        while 1:
            try:
                pos = int(
                    input(
                        f"Player {self.symbol}, "
                        "choose a position (1-9): "
                    )
                )
            except ValueError:
                print("Invalid input. Please enter a number from 1 to 9")
                continue
            
            if pos < 1 or pos > 9:
                print("Invalid position. Please enter a number from 1 to 9")
                continue
    
            return pos-1

class RandomPlayer(Player):
    def get_move(self, board):
        return np.random.choice(list(board.available))