from runner import player, actions, result, terminal, utility, winner, minimax

# player was tested and found to be functional
# actions was tested and found to be functional (returns a list of possible moves and -1 if it is a terminal board)
# result was tested and found to be functional (returns a copy of the board with the action applied. If the action isn't legal it returns -1)
# terminal was tested and found to be functional (returns True if the board is functional and False if the game is still in play)
# utility was found to be functional
# small bug fix on winner, now is functional
# bug fix on minimax functions. The function is now functional.
#TODO  add a database that will store all the stats and make functions to calculate basic stats, such as wins/losses when playing as x/o and percentages.

board = [
["x", "x", "o"], 
["o", "o", "x"], 
["x", "o", "x"]]

print(minimax(board))