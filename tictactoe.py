from math import inf as infinity

game_state_custom = [[' ',' ',' '],
                    [' ',' ',' '],
                    [' ',' ',' ']]
players_custom = ['X','O']

def play_move_custom(state, player, block_num):
    if state[int((block_num-1)/3)][(block_num-1)%3] == ' ':
        state[int((block_num-1)/3)][(block_num-1)%3] = player
    else:
        block_num = int(input("Block is not empty, choose again: "))
        play_move_custom(state, player, block_num)
    
def copy_game_state_custom(state):
    new_state = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    for i in range(3):
        for j in range(3):
            new_state[i][j] = state[i][j]
    return new_state
    
def check_current_state_custom(game_state):
    
    
    # Check horizontals
    if (game_state[0][0] == game_state[0][1] and game_state[0][1] == game_state[0][2] and game_state[0][0] != ' '):
        return game_state[0][0], "Done"
    if (game_state[1][0] == game_state[1][1] and game_state[1][1] == game_state[1][2] and game_state[1][0] != ' '):
        return game_state[1][0], "Done"
    if (game_state[2][0] == game_state[2][1] and game_state[2][1] == game_state[2][2] and game_state[2][0] != ' '):
        return game_state[2][0], "Done"
    
    # Check verticals
    if (game_state[0][0] == game_state[1][0] and game_state[1][0] == game_state[2][0] and game_state[0][0] != ' '):
        return game_state[0][0], "Done"
    if (game_state[0][1] == game_state[1][1] and game_state[1][1] == game_state[2][1] and game_state[0][1] != ' '):
        return game_state[0][1], "Done"
    if (game_state[0][2] == game_state[1][2] and game_state[1][2] == game_state[2][2] and game_state[0][2] != ' '):
        return game_state[0][2], "Done"
    
    # Check diagonals
    if (game_state[0][0] == game_state[1][1] and game_state[1][1] == game_state[2][2] and game_state[0][0] != ' '):
        return game_state[1][1], "Done"
    if (game_state[2][0] == game_state[1][1] and game_state[1][1] == game_state[0][2] and game_state[2][0] != ' '):
        return game_state[1][1], "Done"
    
    # Check if draw
    draw_flag = 0
    for i in range(3):
        for j in range(3):
            if game_state[i][j] == ' ':
                draw_flag = 1
    if draw_flag == 0:
        return None, "Draw"
    
    return None, "Not Done"

def print_board_custom(game_state):
    print('----------------')
    print('| ' + str(game_state[0][0]) + ' || ' + str(game_state[0][1]) + ' || ' + str(game_state[0][2]) + ' |')
    print('----------------')
    print('| ' + str(game_state[1][0]) + ' || ' + str(game_state[1][1]) + ' || ' + str(game_state[1][2]) + ' |')
    print('----------------')
    print('| ' + str(game_state[2][0]) + ' || ' + str(game_state[2][1]) + ' || ' + str(game_state[2][2]) + ' |')
    print('----------------')
    
    
def get_best_move_custom(state, player):
    '''
    Minimax Algorithm
    '''
    winner_loser , done = check_current_state_custom(state)
    if done == "Done" and winner_loser == 'O': # If AI won
        return (1,0)
    elif done == "Done" and winner_loser == 'X': # If Human won
        return (-1,0)
    elif done == "Draw":    # Draw condition
        return (0,0)
        
    moves = []
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if state[i][j] == ' ':
                empty_cells.append(i*3 + (j+1))
    
    for empty_cell in empty_cells:
        move = {}
        move['index'] = empty_cell
        new_state = copy_game_state_custom(state)
        play_move_custom(new_state, player, empty_cell)
        
        if player == 'O':    # If AI
            result,_ = get_best_move_custom(new_state, 'X')    # make more depth tree for human
            move['score'] = result
        else:
            result,_ = get_best_move_custom(new_state, 'O')    # make more depth tree for AI
            move['score'] = result
        
        moves.append(move)

    # Find best move
    best_move = None
    if player == 'O':   # If AI player
        best = -infinity
        for move in moves:            
            if move['score'] > best:
                best = move['score']
                best_move = move['index']
    else:
        best = infinity
        for move in moves:
            if move['score'] < best:
                best = move['score']
                best_move = move['index']
                
    return (best, best_move)

# PLaying
play_again_custom = 'Y'
while play_again_custom == 'Y' or play_again_custom == 'y':
    game_state_custom = [[' ',' ',' '],
              [' ',' ',' '],
              [' ',' ',' ']]
    current_state_custom = "Not Done"
    print("\nNew Game!")
    print_board_custom(game_state_custom)
    player_choice_custom = input("Choose which player goes first - X (You - the petty human) or O(The mighty AI): ")
    winner_custom = None
    
    if player_choice_custom == 'X' or player_choice_custom == 'x':
        current_player_idx_custom = 0
    else:
        current_player_idx_custom = 1
        
    while current_state_custom == "Not Done":
        if current_player_idx_custom == 0: # Human's turn
            block_choice_custom = int(input("Oye Human, your turn! Choose where to place (1 to 9): "))
            play_move_custom(game_state_custom ,players_custom[current_player_idx_custom], block_choice_custom)
        else:   # AI's turn
            _,block_choice_custom = get_best_move_custom(game_state_custom, players_custom[current_player_idx_custom])
            play_move_custom(game_state_custom ,players_custom[current_player_idx_custom], block_choice_custom)
            print("AI plays move: " + str(block_choice_custom))
        print_board_custom(game_state_custom)
        winner_custom, current_state_custom = check_current_state_custom(game_state_custom)
        if winner_custom is not None:
            print(str(winner_custom) + " won!")
        else:
            current_player_idx_custom = (current_player_idx_custom + 1)%2
        
        if current_state_custom == "Draw":
            print("Draw!")
            
    play_again_custom = input('Wanna try again?(Y/N) : ')
    if play_again_custom == 'N':
        print('GG!')