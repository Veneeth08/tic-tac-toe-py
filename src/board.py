class Board:
    def __init__ (self):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.available = set(range(9))
        self.filled = 0

        self.winning_positions = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6)
        ]

    def display(self):
        print('+---+---+---+')
        print("| %s | %s | %s |" %(self.cells[0], self.cells[1], self.cells[2]))
        print('+---+---+---+')
        print("| %s | %s | %s |" %(self.cells[3], self.cells[4], self.cells[5]))
        print('+---+---+---+')
        print("| %s | %s | %s |" %(self.cells[6], self.cells[7], self.cells[8]))
        print('+---+---+---+')
        
    def undo_move(self, pos):
        if pos in self.available:
            return False
        
        self.cells[pos] = " "
        self.available.add(pos)
        self.filled -= 1
        
        return True

    def make_move(self, pos, symbol):
        if pos not in self.available:
            return False
        
        self.cells[pos] = symbol
        self.available.remove(pos)
        self.filled += 1
        
        return True

    def check_winner(self):
        for a, b, c in self.winning_positions:
            if self.cells[a] == self.cells[b] == self.cells[c] != " ":
                return self.cells[a]
        return None

    def is_full(self):
        return self.filled == 9