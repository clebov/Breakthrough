import board

#COMMENT YOUR CODE CHRIS!!!
#print("Hello World")
#print("is this thing on?")

mainBoard = board.createBoard()

board.setStartingPieces(mainBoard)

board.placePiece(mainBoard, 3, 2, '??')

board.printBoard(mainBoard)

