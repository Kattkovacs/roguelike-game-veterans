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


def put_everyone_on_board(board, coordinates_who_is_alive):
    for element in coordinates_who_is_alive:
        row, col = coordinates_who_is_alive[element]
        board[row][col] = element
    return board


def refresh_player_coord(key, player, player_inv, board, everyone_in_room1):
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
        if board[row][col] != '.':
            creature = check_what_is_it(row, col, everyone_in_room1)
            print('creature: ', creature)
            if creature['type'] == 'item':
                refresh_player_inventory(creature, player_inv)
                collect_item(creature, player)
                return player


def check_if_wall(board, row, col):
    return board[row][col] == '#'


def check_what_is_it(row, col, everyone_in_room1):
    for creature in everyone_in_room1:
        if creature['coord_y'] == row and creature['coord_x'] == col and creature != 'player':
            return creature


def refresh_player_inventory(creature, player_inv):
    if creature['name'] not in player_inv.keys():
        player_inv[creature['name']] = {'name': creature['name'], 'quantity': 1, 'hitting_power': creature['hitting_power']}
    else:
        player_inv[creature['name']]['quantity'] += 1
        return player_inv


def collect_item(creature, player):
    player['health'] += creature['health']
    creature['health'] = 0
    return creature


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
