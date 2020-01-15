def create_board(width, height):
    '''
    Creates a new game board based on input parameters.

    Args:
    int: The width of the board
    int: The height of the board

    Returns:
    list: Game board
    '''
    board = []
    for i in range(height):
        board.append(list('.'*width))
    return board


def put_player_on_board(board, player):
    '''
    Modifies the game board by placing the player icon at its coordinates.

    Args:
    list: The game board
    dictionary: The player information containing the icon and coordinates

    Returns:
    Nothing
    '''
    row = player.get('coord_y')
    col = player.get('coord_x')
    board[row][col] = player['player_icon']


# def check_if_wall(board, player, key):
#     row = player.get('coord_y')
#     col = player.get('coord_x')
#     if key == 'w':
#         row -= 1
#     elif key == 's':
#         row += 1
#     elif key == 'a':
#         col -= 1
#     elif key == 'd':
#         col += 1
#     if board[row][col] == '#':
#         return player['coord_y'], player['coord_x']
#     else:
#         return row, col


# def refresh_player_coord(key, player, board):
#     row, col = check_if_wall(board, player, key)
#     player['coord_y'] = row
#     player['coord_x'] = col
#     return player



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
