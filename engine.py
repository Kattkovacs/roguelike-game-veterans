import time
import os
import random

''' COLORS '''
CBLINK = '\33[5m'
CBOLD = '\33[1m'
CYELLOW2 = '\33[93m'
CRED2 = '\33[91m'
CBLUE2 = '\33[94m'
CGREEN2 = '\33[92m'
CEND = '\33[0m'


''' HEALTH PROPERTIES '''
HEALTH = "+"
HEALTH_HIGH = f"{CGREEN2}{HEALTH}{CEND}"
HEALTH_MIDDLE = f"{CYELLOW2}{HEALTH}{CEND}"
HEALTH_LOW = f"{CRED2}{HEALTH}{CEND}"
HEALTH_UNIT = 20


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
            if creature['type'] == 'item':
                refresh_player_inventory(creature, player_inv)
                collect_item(creature, player)
                return player
            else:
                fighting_with_enemy(player, creature)
                return player


def check_if_wall(board, row, col):
    return board[row][col] == '#'


def check_what_is_it(row, col, everyone_in_room1):
    for creature in everyone_in_room1:
        if creature['coord_y'] == row and creature['coord_x'] == col:
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


def display_health_scale(participant):
    ''' When calling this function you should change 'participant' 
        to 'player' or the name of the enemy'''
    value_of_unit = participant['health'] // HEALTH_UNIT
    actual_health_in_unit = participant["actual_health"] // value_of_unit
    half_health = HEALTH_UNIT // 2
    quarter_health = HEALTH_UNIT // 4

    if actual_health_in_unit > half_health:
        print(f"{participant['icon']}'s health: |{actual_health_in_unit * HEALTH_HIGH}{'|'.rjust(HEALTH_UNIT + 1 - actual_health_in_unit, ' ')} ({participant['actual_health']})")
    elif actual_health_in_unit > quarter_health:
        print(f"{participant['icon']}'s health: |{actual_health_in_unit * HEALTH_MIDDLE}{'|'.rjust(HEALTH_UNIT + 1 - actual_health_in_unit, ' ')} ({participant['actual_health']})")
    else:
        print(f"{participant['icon']}'s health: |{actual_health_in_unit * HEALTH_LOW}{'|'.rjust(HEALTH_UNIT + 1 - actual_health_in_unit, ' ')} ({participant['actual_health']})")


def display_fighting_status(player, enemy, clear='on'):
    print()
    print(f"{CBOLD}*** Player fighting with {enemy['name']}***{CEND}")
    print()
    display_health_scale(player)
    display_health_scale(enemy)
    print()
    if clear == 'on':
        time.sleep(0.6)
        os.system('clear')
    elif clear == 'off':
        pass


def hit_the_enemy(gives_hit, gets_hit):
    hit = random.randint(0, 5) * gives_hit['hitting_power']
    gets_hit["actual_health"] -= hit
    if gets_hit["actual_health"] < 0:
        gets_hit["actual_health"] = 0
    return gets_hit


def fighting_with_enemy(player, enemy):
    os.system('clear')
    player["actual_health"] = player['health']
    enemy["actual_health"] = enemy['health']

    display_fighting_status(player, enemy)

    while True:
        # player hits the enemy
        hit_the_enemy(player, enemy)
        display_fighting_status(player, enemy)
        if enemy["actual_health"] == 0:
            display_fighting_status(player, enemy, clear='off')
            print(f"{CBLINK}{CGREEN2}Player won!{CEND}")
            enemy['health'] = enemy["actual_health"]
            player['health'] = player["actual_health"]
            player["actual_health"] = 0
            print(f"{CGREEN2}@'s health is: {player['health']}{CEND}")
            break
        # now enemy hits the player
        else:
            hit_the_enemy(enemy, player)
            display_fighting_status(player, enemy)
            if player["actual_health"] == 0:
                display_fighting_status(player, enemy, clear='off')
                print(f"{CBLINK}{CRED2}Enemy won! Game over!{CEND}")
                quit()
    print()
    input("Press Enter to continue...")


def get_player_stats(player):
    print("Welcome to the wonderful world of Ilhuan.")
    name = input("Write down your name adventurer: ")
    player["name"] = name
    print("(1)Human\n(2)Elf\n(3)Halfling\n(4)Beastman")
    race = input("Choose your race(1/2/3/4): ")
    if race == "1":
        player["race"] = "Human"
        player["health"] = 400
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
