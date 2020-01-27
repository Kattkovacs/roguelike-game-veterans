def create_board(gate1, gate2=None, height=20, width=30, ):
    wall = "#"
    space = "."
    gate = " "
    gate1_x, gate1_y = gate1
    if gate2 is not None:
        gate2_x, gate2_y = gate2
    board = []
    for i in range(height):
        row = []
        for j in range(width):
            if i == 0 or i == height - 1 or j == 0 or j == width - 1:
                row.append(wall)            
            else:
                row.append(space)
        board.append(row)
    board[gate1_x][gate1_y] = gate
    board[gate2_x][gate2_y] = gate
    return board


def put_item_on_board(board, item):
    try:
        row = item.get('coord_y')
        col = item.get('coord_x')
        board[row][col] = item['icon']
    except:
        pass


def refresh_player_coord(key, player, board):
    row = player.get('coord_y')
    col = player.get('coord_x')
    if key == 'w':
        row -= 1
    elif key == 's':
        row += 1
    elif key == 'a':
        col -= 1
    elif key == 'd':
        col += 1
    if check_if_wall(board, row, col):
        pass
    else:
        player['coord_y'] = row
        player['coord_x'] = col
        return player


def check_if_wall(board, row, col):
    return board[row][col] == '#'


def get_player_stats(player):
    print("Welcome to the wonderful world of Ilhuan.")
    name = input("Write down your name adventurer: ")
    player["name"] = name
    print("(1)Human\n(2)Elf\n(3)Halfling\n(4)Beastman")
    race = input("Choose your race(1/2/3/4): ")
    if race == "1":
        player["race"] = "Human"
        player["health"] = 100
    elif race == "2":
        player["race"] = "Elf"
        player["health"] = 125
    elif race == "3":
        player["race"] = "Halfling"
        player["health"] = 75
    elif race == "4":
        player["race"] = "Beastman"
        player["health"] = 150
    return player


def check_collectible(player, player_inv, sword):
    player_coord_x = player["coord_x"]
    player_coord_y = player["coord_y"]
    sword_coord_x = sword["coord_x"]
    sword_coord_y = sword["coord_y"]
    if player_coord_x == sword_coord_x and player_coord_y == sword_coord_y:
        if sword["name"] not in player_inv.keys():
            player_inv[sword["name"]] = 1
        else:
            player_inv[sword["name"]] += 1
        sword["icon"] = "."
        sword["coord_y"] = None
        sword["coord_x"] = None
    return player_inv, sword
