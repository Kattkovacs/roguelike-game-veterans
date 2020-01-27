import util
import engine
import ui
import time


PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3

SWORD_ICON = 'S'
SWORD_START_X = 10
SWORD_START_Y = 10

MONSTER_ICON = 'Đ'
MONSTER_START_X = 25
MONSTER_START_Y = 2

BOARD_WIDTH = 30
BOARD_HEIGHT = 20


def create_player():
    '''
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Fell free to extend this dictionary!

    Returns:
    dictionary
    '''
    player = {"icon": PLAYER_ICON, "name": "Lord-el-Melloi", "race": "Human", "health": 100, "coord_y": PLAYER_START_Y, "coord_x" : PLAYER_START_X}
    return player


def create_player_inventory():
    player_inv = {'Sword': {'name': 'Sword', 'quantity': 1, 'hitting_power': 50}}
    # {'Sword': {"name": "Sword", "quantity": 1, "hitting_power": 50}, food: {"name": "food", "quantity": 1; "health": 100}}
    return player_inv


def create_sword():
    sword = {"type": "item", "name": "Sword", "icon": SWORD_ICON, "health": 50, "hitting_power": 50, "coord_y": SWORD_START_Y, "coord_x": SWORD_START_X}
    return sword


def create_monster():
    monster = {"type": "enemy", "name": "Monster", "icon": MONSTER_ICON, "health": 150, "hitting_power": 100, "coord_y": MONSTER_START_Y, "coord_x": MONSTER_START_X}
    return monster


def collect_coordinates_who_is_alive(everyone_in_room1):
    coordinates_who_is_alive = {}
    for name in everyone_in_room1:
        if name['health'] > 0:
            coordinates_who_is_alive[name['icon']] = (name['coord_y'], name['coord_x'])
    return coordinates_who_is_alive


def main():
    util.clear_screen()
    player = create_player()
    player_inv = create_player_inventory()
    sword = create_sword()
    monster = create_monster()

    engine.get_player_stats(player)
    util.clear_screen()

    is_running = True
    while is_running:
        board1 = engine.create_board(gate1=(16, 29), gate2=(16, 0))
        everyone_in_room1 = [sword, monster, player] # player should be the last one(!)
        coordinates_who_is_alive = collect_coordinates_who_is_alive(everyone_in_room1)
        print(coordinates_who_is_alive)
        engine.put_everyone_on_board(board1, coordinates_who_is_alive)
        ui.display_board(board1)
        ui.display_player_stats(player)
        key = util.key_pressed()
        if key == 'q':
            is_running = False
        elif key == 'I':
            x = ""
            while x == "":
                ui.display_inv(player_inv)
                x = util.key_pressed()
        else:
            engine.refresh_player_coord(key, player, player_inv, board1, everyone_in_room1)
        util.clear_screen()


if __name__ == '__main__':
    main()
