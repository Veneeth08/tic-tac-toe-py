from board import Board

board = Board()
current_symbol = "X"

while True:
    board.display()

    try:
        pos = int(input(f"Player {current_symbol}, choose a position (1-9): "))
    except ValueError:
        print("Invalid input. Please enter a number from 1 to 9")
        continue

    if pos < 1 or pos > 9:
        print("Invalid position. Please enter a number from 1 to 9")
        continue

    pos -= 1

    if board.make_move(pos, current_symbol):
        if current_symbol == "X":
            current_symbol = "O"
        else:
            current_symbol = "X"
    else:
        print("Position already occupied")