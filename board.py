#this file contains methods to create, populate, and print a board
#   it also contains methods to place, move, and remove pieces



#size of board, number of squares on each side and 
row = 8
col = 8

#character token to represent an empty space on the board
blankSpace = '[]'
#character token to represent spaces occupied by player pieces
blackToken = 'BB'
whiteToken = 'WW'



#initialize the board with [] to represent squares
def createBoard():
    fBoard = [[blankSpace for i in range(col)]for j in range(row)]
    printBoard(fBoard)
    return fBoard
#end createBoard



#print the board
def printBoard(fBoard):
    for row in fBoard:
        print(*row) 
    print("\n")
#end printBoard



#place one piece on the board
#   fToken is the character string to be placed on board
def placePiece(fBoard, row, col, fToken):
    fBoard[row][col] = fToken 
#end place piece



#place the starting pieces on the board
#   BB is a black piece and WW is a white piece
def setStartingPieces(fBoard):
    for i in range(col):
        fBoard[0][i] = blackToken
    for j in range(col):
        fBoard[1][j] = blackToken
    for k in range(col):
        fBoard[row-1][k] = whiteToken
    for l in range(col):
        fBoard[row-2][l] = whiteToken
#end setStartingPieces 



#check if a location is on the board
def isOnBoard(fRow, fCol):
    if (fRow >= 0 and fRow < row and fCol >= 0 and fCol < col):
        return True
    else:
        return False
#end isValid



#move a piece from one location to another
def movePiece(fBoard, oldRow, oldCol, newRow, newCol):

    if (isOnBoard(newRow, newCol) and isOnBoard(oldRow, oldCol)):

        if (fBoard[oldRow][oldCol] != blankSpace):
           ## sets the previous position the piece move from to old location
            fBoard[newRow][newCol] = fBoard[oldRow][oldCol]

        else:
            print("Error, movePiece: cannot target a blank space.\n")

    else:
        print("Error, movePiece: proposed move not on board.\n") 
#end move piece



#make a valid move, follows game rules for Breakthrough
#   player will be 0 for White, or 1 for Black
#   move refers to a character, L, F, or R, to reference a left, forward, or right move
#   left and right flip orientation depending on the player
#       (black is at the top facing down, white is at the bottom facing up)
def makeMove(fBoard, oldRow, oldCol, move):
    
    #check that valid space is being targeted
    if (not(isOnBoard(oldRow, oldCol))):
        print("Error, makeMove: targeted space is not on the board.")
        return

    #determine if a piece is being targeted and which player
    fPlayer = -1
    if fBoard[oldRow][oldCol] == blankSpace:
        print("Error, makeMove: please target a piece, not an empty space.\n")
        return
    
    if fBoard[oldRow][oldCol] == whiteToken:
        fPlayer = 0
        #print("Player Number: " + str(fPlayer) + ".\n")
    elif fBoard[oldRow][oldCol] == blackToken:
        fPlayer = 1
        #print("Player Number: " + str(fPlayer) + ".\n")
    else:
        print("Error, makeMove: improper piece at (" + str(oldRow) + ", " + str(oldCol) + ").\n") 
        return

    #determine vertical direction, up or down
    #   remember the list indeces for the vertical movement are reversed
    #       0 at top and 8 or row at bottom
    vert = 0
    if fPlayer == 0:    #white
        vert = -1
    elif fPlayer == 1:  #black
        vert = 1
    else:
        print("Error, makeMove: please enter valid player (0 or 1).\n")
        return

    #determine horizontal direction if any, left or right
    horiz = 0
    if move == 'F':     #forward
        pass
    elif move == 'L':   #left
        horiz = vert
    elif move == 'R':   #right
        horiz = 0-vert
    else:
        print("Error, makeMove: please enter a valid move (L, F, or R)\n")
        return

    #candidate coordinates for new move
    newRow = oldRow + vert
    newCol = oldCol + horiz

    #determine if potential move is on board
    if(not(isOnBoard(newRow, newCol))):
        print("Error, makeMove: candidate move goes off the board.\n")
        return

    #get token of players
    playerToken = ''
    enemyToken = ''
    if fPlayer == 0:    #white
        playerToken = whiteToken
        enemyToken = blackToken
    elif fPlayer == 1:  #black
        playerToken = blackToken
        enemyToken = whiteToken
    else:
        print("Error, makeMove: please enter valid player (0 or 1)\n")
        return

    #determine if potential move is blocked
    #blocked by a friendly piece
    if(fBoard[newRow][newCol] == playerToken):
        print("Error, makeMove: cannot move into friendly piece " + playerToken + 
              " at (" + str(newRow) + ", " + str(newCol) + "): " +
              fBoard[newRow][newCol] + ".\n")
        return

    #blocked by enemy piece in front of player
    if(move == 'F' and (fBoard[newRow][newCol] != blankSpace)):
        print("Error, makeMove: cannot move directly forward into enemy piece " + 
              enemyToken + " at (" + str(newRow) + ", " + str(newCol) + ").\n")
        return

    #at this point, the new move is:
    #   on the board
    #   is not blocked by a friendly piece at all
    #   is not block by an enemy piece if it is a forward move
    #therefore move piece
    print("makeMove: moving piece " + fBoard[oldRow][oldCol] + " to (" + 
          str(newRow) + ", " + str(newCol) + ").") 
    fBoard[newRow][newCol] = playerToken
    fBoard[oldRow][oldCol] = blankSpace

#end makeMove

