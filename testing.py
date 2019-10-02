#testing file to run as main to check external funtions
import board
import brain
import tree

print("\n################### Start testing.py ###################\n")

test1 = board.createBoard()
board.setStartingPieces(test1)
board.printBoard(test1)

currentState = tree.Node(0, test1)
currentState.nextTurns = brain.getPossibleStates(currentState, 0, 0)

print("\n################### Printing Next States Tree ###################\n")
brain.minimax(currentState, 0, 0)
tree.writeTree(currentState)








"""
print("__________")
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

#brain.getHeuristic(progressedBoard)
board.printBoard(progressedBoard)

next02 = tree.Node(0, progressedBoard)
next02.nextTurns = brain.getPossibleStates(next02, 0, 1)
tree.printTree(next02)

#print(test1)
"""
