
# The board positions are represented as a list of 3 lists, each with three items representing the three rows in a tic tac toe board
board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

def draw_board(board):
    """
    This function takes in a board list, and prints a console based representation of the board
    """
    print("")
    print("     |     |     ")
    print(" " + board[0][0] + "   |  " + board[0][1] + "  |  " + board[0][2] + "  ")
    print("     |     |     ")
    print("___________________")

    print("     |     |     ")
    print(" " + board[1][0] + "   |  " + board[1][1] + "  |  " + board[1][2] + "  ")
    print("     |     |     ")
    print("___________________")

    print("     |     |     ")
    print(" " + board[2][0] + "   |  " + board[2][1] + "  |  " + board[2][2] + "  ")
    print("     |     |     ")
    print("")

if __name__ == "__main__":
    draw_board(board)