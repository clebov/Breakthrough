#testing file to run as main to check external funtions
import board
import brain
import Tree

print("\n################### Start testing.py ###################\n")

test1 = board.createBoard()
board.setStartingPieces(test1)
board.printBoard(test1)

currentState = []
currentState.append(test1)

nextStates = brain.getPossibleStates(currentState, 0)

print("\n################### Printing Next States Tree ###################\n")
Tree.printTree(nextStates)


print("__________")
board.printBoard(currentState[0])
board.printBoard(test1)


#print(test1)

#for eachState in currentState:
#    board.printBoard(eachState)