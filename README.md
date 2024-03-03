Hey there! Are you lonely and want to play tictactoe? Here you go!!
This code implements a Tic Tac Toe game with an AI player using the Minimax algorithm. Here's a breakdown of how it works:

1. **Game Initialization**:
   - The game starts with an empty 3x3 game board (`game_state_custom`) and two players, represented by 'X' and 'O'.

2. **Play Move Function**:
   - `play_move_custom`: This function allows a player to make a move on the game board. It checks if the chosen cell is empty and updates the board with the player's symbol. If the chosen cell is not empty, it prompts the player to choose again.

3. **Copy Game State Function**:
   - `copy_game_state_custom`: This function creates a deep copy of the current game state. It is used to generate possible future game states without modifying the current state.

4. **Check Current State Function**:
   - `check_current_state_custom`: This function checks the current state of the game to determine if a player has won, if the game is a draw, or if the game is still ongoing.

5. **Print Board Function**:
   - `print_board_custom`: This function prints the current state of the game board.

6. **Minimax Algorithm**:
   - `get_best_move_custom`: This function implements the Minimax algorithm to find the best move for the AI player ('O'). It recursively explores all possible future game states up to a certain depth, evaluates them using a scoring function, and selects the move that maximizes the AI's chances of winning and minimizes the opponent's chances.
   
7. **Game Loop**:
   - The game loop allows players to take turns making moves until the game is over. It alternates between the human player ('X') and the AI player ('O').
   - At each turn, the current player selects a move either by human input or by using the Minimax algorithm for the AI player.
   - After each move, the current state of the game is checked to see if there is a winner or if the game is a draw.
   - The game loop continues until the players choose not to play again.

Overall, this code creates a fully functional Tic Tac Toe game where the AI player uses the Minimax algorithm to make optimal moves, ensuring a challenging game for the human player.
