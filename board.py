#this file contains methods to create, populate, and print a board

#size of board, number of squares on each side
boardSize = 8

#initialize the board
def createBoard(fBoard):
    for i in range(boardSize):
        fBoard.append(0)
    for j in range(len(fBoard)):
        for k in range(boardSize):
            fBoard[j].append(0)
#end createBoard

#print board
def printBoard(fBoard):
    print(fBoard)
#end print board

