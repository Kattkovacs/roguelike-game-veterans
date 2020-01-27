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
    player_inv = {}
    player = {"icon": PLAYER_ICON, "name": "Lord-el-Melloi", "race": "Human", "health": 100, "coord_y": PLAYER_START_Y, "coord_x" : PLAYER_START_X}
    return player, player_inv


def create_sword():
    sword = {"type": "collectible", "name": "Sword", "icon": SWORD_ICON, "health": 50, "hitting_power": 50, "coord_y": SWORD_START_Y, "coord_x": SWORD_START_X}
    return sword


def create_monster():
    monster = {"type": "enemy", "name": "Monster", "icon": MONSTER_ICON, "health": 150, "hitting_power": 100, "coord_y": MONSTER_START_Y, "coord_x": MONSTER_START_X}
    return monster


def main():
    player, player_inv = create_player()
    sword = create_sword()
    monster = create_monster()

    board1 = engine.create_board(gate1=(16, 29), gate2=(16, 0))

    util.clear_screen()

    engine.get_player_stats(player)

    util.clear_screen()

    is_running = True
    while is_running:
        engine.put_item_on_board(board1, sword)
        engine.put_item_on_board(board1, monster)
        engine.put_item_on_board(board1, player)
        ui.display_board(board1)
        ui.display_player_stats(player)
        key = util.key_pressed()
        if key == 'q':
            is_running = False
        elif key == 'I':
            x= ""
            while x == "":
                ui.display_inv(player_inv)
                x = util.key_pressed()        
        else:
            engine.refresh_player_coord(key, player, board1)
            board1 = engine.create_board(gate1=(16, 29), gate2=(16, 0))
            player_inv, weapon = engine.check_collectible(player, player_inv, sword)
        util.clear_screen()


if __name__ == '__main__':
    main()
