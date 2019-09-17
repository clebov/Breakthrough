#this file contains methods to create, populate, and print a board



#size of board, number of squares on each side and 
row, col = (8, 8)



#initialize  the board with [] to represent squares
def createBoard():
    fBoard = [['[]' for i in range(col)]for j in range(row)]
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
def placePiece(fBoard, fX, fY, fToken):
    fBoard[fX][fY] = fToken 
#end place piece



#place the starting pieces on the board
#   BB is a black piece and WW is a white piece
def setStartingPieces(fBoard):
    for i in range(col):
        fBoard[0][i] = 'BB'
    for j in range(col):
        fBoard[1][j] = 'BB'
    for k in range(col):
        fBoard[row-1][k] = 'WW'
    for l in range(col):
        fBoard[row-2][l] = 'WW' 
#end setStartingPieces 


#