class Board:
    def __init__ (self):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    def display(self):
        print('+---+---+---+')
        print("| %s | %s | %s |" %(self.cells[0], self.cells[1], self.cells[2]))
        print('+---+---+---+')
        print("| %s | %s | %s |" %(self.cells[3], self.cells[4], self.cells[5]))
        print('+---+---+---+')
        print("| %s | %s | %s |" %(self.cells[6], self.cells[7], self.cells[8]))
        print('+---+---+---+')

    def is_available(self, pos):
        return self.cells[pos] == " "

    def make_move(self, pos, symbol):
        if self.is_available(pos):
            self.cells[pos] = symbol
            return True
        return False