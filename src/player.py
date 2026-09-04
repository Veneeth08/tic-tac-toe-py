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

class MinimaxPlayer(Player):
    def __init__(self, symbol):
        super().__init__(symbol)
        self.opponent_symbol = "O" if symbol == "X" else "X"
        
    def min_player(self, board):
        winner = board.check_winner()
        if winner is not None:
            if winner == self.symbol: return 1, None
            return -1, None
        
        if board.is_full(): return 0, None

        available = list(board.available)
        min = 1
        p = available[0]
        
        for pos in available:
            board.make_move(pos, self.opponent_symbol)
            
            x, best_pos = self.max_player(board)
            if x < min:
                min = x
                p = pos
            
            board.undo_move(pos)
            
        return min, p
            
    def max_player(self, board):
        winner = board.check_winner()
        if winner is not None:
            if winner == self.symbol: return 1, None
            return -1, None
        
        if board.is_full(): return 0, None
        
        available = list(board.available)
        max = -1
        p = available[0]
        
        for pos in available:
            board.make_move(pos, self.symbol)
            
            x, best_pos = self.min_player(board)
            if x > max:
                max = x
                p = pos
                
            board.undo_move(pos)
            
        return max, p

    def get_move(self, board):
        return self.max_player(board)[1]