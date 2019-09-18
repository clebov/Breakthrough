import board

mainBoard = board.createBoard()

board.setStartingPieces(mainBoard)

#board.placePiece(mainBoard, 3, 2, '??')
board.printBoard(mainBoard)

#testing movePiece method
board.movePiece(mainBoard, 1, 2, 2, 2) 
board.printBoard(mainBoard)
board.movePiece(mainBoard, 3, 3, 4, 4)
board.printBoard(mainBoard)
board.movePiece(mainBoard, 8, 8, 11, 11)
board.printBoard(mainBoard)

#testing, move each piece forward one
#for i in range(board.row):
#    for j in range(board.col):
 #       if mainBoard[i][j] == board.blackToken:
  #          board.makeMove(mainBoard, i, j, 1, 'F')
   #     if mainBoard[i][j] == board.whiteToken:
    #        board.makeMove(mainBoard, i, j, 0, 'F')
#end for i for j loops

#testing on clean board
testBoard = board.createBoard()
board.setStartingPieces(testBoard)
board.printBoard(testBoard)

#testing makeMove
board.makeMove(testBoard, 6, 6, 'F')

board.printBoard(testBoard)