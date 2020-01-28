def display_board(board):
    for row in board:
        print(' '*11, *row)


def display_player_info_and_control_info(player):
    print(f" {'-'*37}{' '*4}", end="")
    print(f" {'-'*37}")
    print(f"| {'PLAYER INFO'.center(35)} |{' '*3}", end="")
    print(f"| {'CONTROL INFO'.center(35)} |")
    print(f" {'-'*37}{' '*4}", end="")
    print(f" {'-'*37}")
    print(f"| {'Name:'.ljust(7)}{player['name'].ljust(13)} | {'Icon:'.ljust(8)}{player['icon'].ljust(5)}|{' '*3}", end="")
    print(f"| {'Move:'.ljust(23)}[a][d][s][w]{'|'.rjust(2)}")
    print(f"| {'Race:'.ljust(7)}{player['race'].ljust(13)} | {'Health:'.ljust(8)}{str(player['health']).ljust(5)}|{' '*3}", end="")
    print(f"| {'Check your inventory:'.ljust(23)}[Shift + i]{'|'.rjust(3)}")
    print(f"| {'Hitting power:'.ljust(15)}{str(player['hitting_power']).ljust(5)} | {'|'.rjust(14)}{' '*3}", end="")
    print(f"| {'Quit the Game:'.ljust(23)}[q]{'|'.rjust(11)}")
    print(f" {'-'*37}{' '*4}", end="")
    print(f" {'-'*37}")
    print()


def display_inv(player_inv):
    print()
    print("Your inventory: ", player_inv)
