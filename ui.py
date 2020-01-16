def display_board(board):
    '''
    Displays complete game board on the screen

    Returns:
    Nothing
    '''
    for i in range(len(board)):
        for j in range(len(board[i])):
            if i == 0 or i == len(board) - 1:
                board[i][j] = '#'
            elif j == 0:
                board[i][j] = '#'
            elif j == len(board[i]) - 1:
                if i == 16:  # This is the place of the gate
                    board[i][j] = ' '  # This is the icon of the gate
                else:
                    board[i][j] = '#'
            else:
                board[i][j] = board[i][j]
        print(*board[i])


def display_player_stats(player):
    print(player["name"] + "   " + "Race: " + player["race"] + "   Health: " + str(player["health"]))