def display_board(board):
    for row in board:
        print(*row)

def display_player_stats(player):
    print(player["name"] + "   " + "Race: " + player["race"] + "   Health: " + str(player["health"]))


def display_inv(player_inv):
    print("Your inventory: ", player_inv)