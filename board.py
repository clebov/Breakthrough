#this file contains methods to create, populate, and print a board
#   it also contains methods to place, move, and remove pieces



#size of board, number of squares on each side and 
row = 5
col = 5

#character token to represent an empty space on the board
blankSpace = '[]'
#character token to represent spaces occupied by player pieces
blackToken = 'BB'
whiteToken = 'WW'

#char list of possible moves, left, forward, right, for looping. 
moves = {'L', 'F', 'R'}

#initialize the board with [] to represent squares
def createBoard():
    fBoard = [[blankSpace for i in range(col)]for j in range(row)]
    #printBoard(fBoard)
    return fBoard
#end createBoard




#create a board object
class board(object):
    def __init__(self, row, col, blank, moves):
        self.row = row
        self.col = col
        self.blank = blank
        self.moves = moves
        self.field = [[blank for i in range(col)]for j in range(row)]

    def print(self):
        printBoard(self.field)
#end board class


#print the board
def printBoard(fBoard):
    for row in fBoard:
        print(*row) 
    print("\n")
#end printBoard


#write the board to a text file
def writeBoard(fBoard, fFile):
    for i in range(row):
        for j in range(col):
            fFile.write(fBoard[i][j]+" ") 
        fFile.write("\n")
    fFile.write("\n")
#end writeBoard


#place one piece on the board
#   fToken is the character string to be placed on board
def placePiece(fBoard, row, col, fToken):
    fBoard[row][col] = fToken 
#end place piece



#place the starting pieces on the board
#   BB is a black piece and WW is a white piece
def setStartingPieces(fPlayer):
    #if first player
    if fPlayer.turn == 0:
        for i in range(fPlayer.board.col):
            fPlayer.board.field[fPlayer.board.row-1][i] = fPlayer.token
            fPlayer.board.field[fPlayer.board.row-2][i] = fPlayer.token
    #if first player
    elif fPlayer.turn == 1:
        for i in range(fPlayer.board.col):
            fPlayer.board.field[0][i] = fPlayer.token
            fPlayer.board.field[1][i] = fPlayer.token
    else:
        print("Error: board.py: setStartingPieces: " +
              "player has invalid turn order: "+str(fPlayer))
#end setStartingPieces 


#check if a location is on the board
def isOnBoard(fBoard, fRow, fCol):
    if (fRow >= 0 and fRow < fBoard.row and fCol >= 0 and fCol < fBoard.col):
        return True
    else:
        return False
#end isValid



#move a piece from one location to another
def movePiece(fBoard, oldRow, oldCol, newRow, newCol):
    if (isOnBoard(newRow, newCol) and isOnBoard(oldRow, oldCol)):
        if (fBoard[oldRow][oldCol] != blankSpace):
            tempToken = fBoard[oldRow][oldCol]
            fBoard[newRow][newCol] = tempToken
            fBoard[oldRow][oldCol] = blankSpace
        else:
            None
            #print("Error, movePiece: cannot target a blank space.\n")
    else:
        None
        #print("Error, movePiece: proposed move not on board.\n") 
#end move piece



#make a valid move, follows game rules for Breakthrough
#   returns true if a move was made or false if an error was found
#   player will be 0 for White, or 1 for Black
#   move refers to a character, L, F, or R, to reference a left, forward, or right move
#   left and right flip orientation depending on the player
#       (black is at the top facing down, white is at the bottom facing up)
def makeMove(fBoard, fPlayer, oldRow, oldCol, move):
    
    #check that valid space is being targeted
    if (not(isOnBoard(fPlayer.board, oldRow, oldCol))):
        #print("Error, makeMove: targeted space is not on the board.")
        return False

    #determine if a piece is being targeted and which player
    if fBoard[oldRow][oldCol] == fPlayer.board.blank:
        #print("Error, makeMove: please target a piece, not an empty space.\n")
        return False
    
    """
    if fBoard[oldRow][oldCol] == whiteToken:
        fPlayer = 0
        #print("Player Number: " + str(fPlayer) + ".\n")
    elif fBoard[oldRow][oldCol] == blackToken:
        fPlayer = 1
        #print("Player Number: " + str(fPlayer) + ".\n")
    else:
        #print("Error, makeMove: improper piece at (" + str(oldRow) + ", " + str(oldCol) + ").\n") 
        return False
    """

    #determine vertical direction, up or down
    #   remember the list indeces for the vertical movement are reversed
    #       0 at top and 8 or row at bottom
    vert = 0
    if fPlayer.turn == 0:    #white
        vert = -1
    elif fPlayer.turn == 1:  #black
        vert = 1
    else:
        #print("Error, makeMove: please enter valid player (0 or 1).\n")
        return False

    #determine horizontal direction if any, left or right
    horiz = 0
    if move == 'F':     #forward
        None
    elif move == 'L':   #left
        horiz = vert
    elif move == 'R':   #right
        horiz = 0-vert
    else:
        #print("Error, makeMove: please enter a valid move (L, F, or R)\n")
        return False

    #candidate coordinates for new move
    newRow = oldRow + vert
    newCol = oldCol + horiz

    #determine if potential move is on board
    if(not(isOnBoard(fPlayer.board, newRow, newCol))):
        #print("Error, makeMove: candidate move goes off the board.\n")
        return False
    
    """
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
        #print("Error, makeMove: please enter valid player (0 or 1)\n")
        return False
    """
    
    #determine if potential move is blocked
    #blocked by a friendly piece
    if(fBoard[newRow][newCol] == fPlayer.token):
        #print("Error, makeMove: cannot move into friendly piece " + playerToken + 
        #      " at (" + str(newRow) + ", " + str(newCol) + "): " +
        #      fBoard[newRow][newCol] + ".\n")
        return False

    #blocked by enemy piece in front of player
    if(move == 'F' and (fBoard[newRow][newCol] != fPlayer.board.blank)):
        #print("Error, makeMove: cannot move directly forward into enemy piece " + 
        #      enemyToken + " at (" + str(newRow) + ", " + str(newCol) + ").\n")
        return False

    #at this point, the new move is:
    #   on the board
    #   is not blocked by a friendly piece at all
    #   is not block by an enemy piece if it is a forward move
    #therefore move piece
    #print("makeMove: moving piece " + fBoard[oldRow][oldCol] + " from (" +
    #      str(oldRow) + ", " + str(oldCol) + ") to (" + 
    #      str(newRow) + ", " + str(newCol) + ").") 
    fBoard[newRow][newCol] = fPlayer.token
    fBoard[oldRow][oldCol] = fPlayer.board.blank
    return True

#end makeMove


#check for win condition and return
def endGame(fBoard):
    win = False
    for i in range(col):
        if (fBoard[0][i] == whiteToken) or (fBoard[row-1][i] == blackToken):
            win = True
    return win
#end endGame