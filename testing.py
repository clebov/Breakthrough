#testing file to run as main to check external funtions
import board
import brain
import tree

print("\n################### Start testing.py ###################\n")

test1 = board.createBoard()
board.setStartingPieces(test1)
board.printBoard(test1)

currentState = tree.Node(0, test1)
#currentState.append(test1)

currentState.nextTurns = brain.getPossibleStates(currentState, 0, 0)

#for i in range(len(currentState.nextTurns)):
#    currentState.nextTurns[i].nextTurns = brain.getPossibleStates(currentState.nextTurns[i], 1, 0)


print("\n################### Printing Next States Tree ###################\n")
tree.printTree(currentState)
#for i in range(len(currentState.nextTurns)):
#    tree.printTree(currentState.nextTurns[1]) 

"""
print("__________")
#board.printBoard(currentState[0])
#board.printBoard(test1)



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

brain.getHeuristic(progressedBoard)
board.printBoard(progressedBoard)
"""
#print(test1)

#for eachState in currentState:
#    board.printBoard(eachState)