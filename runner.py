from board import draw_board
from stats import reset, update, print_stats
from copy import deepcopy

board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

# TODO fix the play_game function so after each game it asks you which player you would like to be and offers you an option to quit.

def player(board):
    """
    This function takes in a board list and returns which player's turn it is. (x goes first)
    """
    # Count how many squares are taken and see if it is an odd or even number
    count = 0
    for i in board:
        for h in i:
            if h != " ":
                count += 1
    if count % 2 == 0:
        return "x"
    else:
        return "o"

def actions(board):
    """
    This function takes in a board list and returns all possible moves in a list of tuples, where each tuple represents a move with two index positions. This function returns -1 if the game is terminal.
    """
    if terminal(board):
        return -1
    moves = []
    for i in range(3):
        for h in range(3):
            if board[i][h] == " ":
                moves.append((i, h))
    return moves



def result(board, action):
    """
    This function takes a board list and an action tuple and returns the resulting board without modifying the original board. If the move is invalid then the function returns -1.
    """
    # Make a deep copy of the board list so that the original list won't be modified
    new_board = deepcopy(board)
    if new_board[action[0]][action[1]] != " ":
        return -1
    
    current_player = player(board)
    new_board[action[0]][action[1]] = current_player
    return new_board

def winner(board):
    """
    This function takes in a board list and returns x or o if there is a winner, if there is no winner (either because the game is not over or it is a tie) it returns None
    """
    game_over = terminal(board)
    if game_over == True:
        win = utility(board)
        if win == 1:
            return "x"
        elif win == -1:
            return "o"
        else:
            return None
    return None

def terminal(board):
    """
    This function takes in the board list and returns True if the game is over and False if the game is not over
    """
    # Check the horizontal
    for i in board:
        if i[0] != " " and i[0] == i[1] and i[1] == i[2]:
            return True

    # Check the vertical
    for i in range(3):
        if board[0][i] != " " and board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            return True

    # Check diagnol
    if board[0][0] != " " and board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return True
    elif board[0][2] != " " and board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return True

    # Check if the board is full
    for i in board:
        for h in i:
            if h == " ":
                return False
    return True


def utility(board):
    """
    This function takes in the board list (of a terminal board) and returns 1 if X won, -1 if O won, and 0 if it was a tie.
    """ 
    
    # Check the horizontal
    for i in board:
        if i[0] != " " and i[0] == i[1] and i[1] == i[2]:
            if i[0] == "x":
                return 1
            else:
                return -1

    # Check the vertical
    for i in range(3):
        if board[0][i] != " " and board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            if board[0][i] == "x":
                return 1
            else:
                return -1

    # Check diagnol
    if board[0][0] != " " and board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        if board[0][0] == "x":
            return 1
        else:
            return -1
    elif board[0][2] != " " and board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        if board[0][2] == "x":
            return 1
        else:
            return -1
    return 0



def minimax(board):
    """
    This function takes in the board list and returns the optimal next move for the current player's turn.
    """
    if player(board) == "x":
        # Get all the possible actions
        moves = actions(board)
        utilities = {}
        # Loop through all the possible moves and get the lowest utility from the min_value function
        for i in range(len(moves)):
            u = min_value(result(board, moves[i]))
            if u == 1:
                return moves[i]
            else:
                utilities[i] = u

        if 0 in utilities.values():
            for k, v in utilities.items():
                if v == 0:
                    return moves[k]
        else:
            for k, v in utilities.items():
                if v == -1:
                    return moves[k]


    else:
        # Loop through all possible actions and choose the highest utility from the max_value function
        moves = actions(board)
        utilities = {}
        for i in range(len(moves)):
            #print(moves[i])
            u = max_value(result(board, moves[i]))
            if u == -1:
                return moves[i]
            else:
                utilities[i] = u

        if 0 in utilities.values():
            for k, v in utilities.items():
                if v == 0:
                    return moves[k]
        else:
            for k, v in utilities.items():
                if v == 1:
                    return moves[k]




def max_value(board):
    """
    This function loops through all possible actions and recursively assigns a utility to it by picking the highest action from the lowest actions that the min_value returns
    """
    if terminal(board):
        return utility(board)
    else:
        v = -100
        for i in actions(board):
            v = max(v, min_value(result(board, i)))
        return v


def min_value(board):
    """
    This function loops through all possible actions and recursively assigns a utility to it by picking the lowest action from the highest actions that the max_value returns
    """
    if terminal(board):
        return utility(board)
    else:
        v = 100
        for i in actions(board):
            v = min(v, max_value(result(board, i)))
        return v


def play_game(board):
    """
    This function is a menu which excepts input from the user to control the menu options and call the appropriate functions and run the game.
    """
    while True:
        print("Play as x (x) or o (o)? (Enter q to quit)")
        answer = input().lower()
        if answer == "q":
            print("Goodbye")
            quit()
        elif answer == "x":
            opponent = "x"
            draw_board(board)
            break
        elif answer == "o":
            opponent = "o"
            draw_board(board)
            break
        else:
            print("Please enter a valid option")

        

    while True:
        turn = player(board)
        if turn == opponent:
            # Get the user's move and validate it to make sure it is valid.
            while True:
                print("Enter your move (1 - 9)")
                attempt = input()
                try:
                    attempt = int(attempt) - 1
                except ValueError:
                    print("Invalid Entry")
                    continue
                if attempt < 0 or attempt > 8:
                    print("Invalid Entry")
                    continue

                if attempt < 3:
                    row = 0
                elif attempt < 6:
                    row = 1
                else:
                    row = 2

                column = attempt - (row * 3)
                if board[row][column] != " ":
                    print("This space was already taken")
                    continue
                else:
                    move = (row, column)

                break
            
            board = result(board, move)
        
        elif turn != opponent:
            move = minimax(board)
            board = result(board, move)

        draw_board(board)
        
        if terminal(board):
            w = winner(board)
            if w == "o":
                print("game over. O wins!")
            elif w == "x":
                print("game over. X wins!")
            else:
                print("game over. Tie game")

            # Update the database
            if w == None:
                update(0, opponent)
            elif w == opponent:
                update(1, opponent)
            else:
                update(-1, opponent)

            
            # Print stats
            print_stats()
            break

def runner():
    """
    This function first resets the board and then calls the play_game function. It continues in an infinite loop.
    """
    while True:
        for i in range(3):
            for j in range(3):
                board[i][j] = " "
        play_game(board)
        

if __name__ == "__main__":
    runner()
            


        