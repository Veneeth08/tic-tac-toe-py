from game import Game
from player import HumanPlayer, RandomPlayer, MinimaxPlayer


def choose_player(symbol):
    players = {
        "1": HumanPlayer,
        "2": RandomPlayer,
        "3": MinimaxPlayer
    }

    while True:
        print(f"\nChoose player type for {symbol}:")
        print("1. Human")
        print("2. Random")
        print("3. Minimax")

        choice = input("Enter choice: ")

        if choice in players:
            return players[choice](symbol)

        print("Invalid choice. Try again.")


player_X = choose_player("X")
player_O = choose_player("O")

game = Game(player_X, player_O)
game.play()