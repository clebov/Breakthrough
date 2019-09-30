#testing file to run as main to check external funtions
import board
import brain
import tree

print("\n################### Start testing.py ###################\n")

test1 = board.createBoard()
board.setStartingPieces(test1)
board.printBoard(test1)

currentState = []
currentState.append(test1)

nextStates = brain.getPossibleStates(currentState, 0)

print("\n################### Printing Next States Tree ###################\n")
tree.printTree(nextStates)


print("__________")
board.printBoard(currentState[0])
board.printBoard(test1)


progressedBoard = board.createBoard()
board.placePiece(progressedBoard, 2, 3, board.whiteToken)
board.placePiece(progressedBoard, 5, 4, board.whiteToken)
board.placePiece(progressedBoard, 2, 7, board.whiteToken)
board.placePiece(progressedBoard, 3, 3, board.whiteToken)
board.placePiece(progressedBoard, 7, 1, board.whiteToken)
board.placePiece(progressedBoard, 1, 0, board.whiteToken)
board.placePiece(progressedBoard, 6, 6, board.blackToken)
board.placePiece(progressedBoard, 4, 4, board.blackToken)
board.placePiece(progressedBoard, 2, 0, board.blackToken)

brain.getHeuristic(progressedBoard)
board.printBoard(progressedBoard)

#print(test1)

#for eachState in currentState:
#    board.printBoard(eachState)