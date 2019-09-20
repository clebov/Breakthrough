#testing file to run as main to check external funtions
import board
import brain

print("\n################### Start testing.py ###################\n")

test1 = board.createBoard()
board.setStartingPieces(test1)
board.printBoard(test1)

currentState = []
currentState.append(test1)

brain.getPossibleStates(currentState, 0)



#print(test1)

#for eachState in currentState:
#    board.printBoard(eachState)