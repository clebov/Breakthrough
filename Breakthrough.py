import board

mainBoard = board.createBoard()

board.setStartingPieces(mainBoard)

#board.placePiece(mainBoard, 3, 2, '??')
board.printBoard(mainBoard)

#testing movePiece method
board.movePiece(mainBoard, 1, 8, 2, 2) 
board.printBoard(mainBoard)
board.movePiece(mainBoard, 3, 3, 4, 4)
board.printBoard(mainBoard)
board.movePiece(mainBoard, 8, 8, 11, 11)
board.printBoard(mainBoard)

#testing makeMove, move each piece forward one
for i in range(board.row):
    for j in range(board.col):
        board.makeMove(mainBoard, i, j, 'F')
        board.printBoard(mainBoard)
#end for i for j loops

#testing on clean board
testBoard = board.createBoard()
board.setStartingPieces(testBoard)
board.printBoard(testBoard)

#testing makeMove
board.makeMove(testBoard, 6, 6, 'F')
for i in range(board.col):
    board.makeMove(testBoard, 6, i, 'F')
    #print("blorg " + str(i) + "\n") 

board.printBoard(testBoard)

#testing left and right parameters of makeMove
testBoard02 = board.createBoard()
board.setStartingPieces(testBoard02)
board.printBoard(testBoard02)

board.makeMove(testBoard02, 1, 1, 'L')
board.printBoard(testBoard02)
board.makeMove(testBoard02, 6, 6, 'L')
board.printBoard(testBoard02)
board.makeMove(testBoard02, 1, 6, 'R')
board.printBoard(testBoard02)
board.makeMove(testBoard02, 6, 2, 'R')
board.printBoard(testBoard02)
board.makeMove(testBoard02, 5, 3, 'L')
board.printBoard(testBoard02)
board.makeMove(testBoard02, 4, 2, 'L')
board.printBoard(testBoard02)
board.makeMove(testBoard02, 3, 1, 'F')
board.printBoard(testBoard02)
board.makeMove(testBoard02, 2, 1, 'R')
board.printBoard(testBoard02)
board.makeMove(testBoard02, 1, 2, 'F')
board.printBoard(testBoard02)



