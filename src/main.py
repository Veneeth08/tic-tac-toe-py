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

    if not board.make_move(pos, current_symbol):
        print("Position already occupied")
        continue

    winner = board.check_winner()

    if winner is not None:
        board.display()
        print(f"Player {winner} wins!")
        break

    if board.is_full():
        board.display()
        print("It's a draw!")
        break

    if current_symbol == "X":
        current_symbol = "O"
    else:
        current_symbol = "X"