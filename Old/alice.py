#this file is designed to show one game using only minimax search (no alpha beta) 
#   with the white player going first, using a defensive strategy,
#   and the black player going second, using an offensive strategy.

import board
import tree
import brain
import copy


print("\n################### Start alice.py ###################\n")


turnCounter = 0
mainBoard = board.createBoard()
board.setStartingPieces(mainBoard)

print("Turn: " + str(turnCounter))
board.printBoard(mainBoard)




while(not(board.endGame(mainBoard))):

    #debugging
    #print("##########from turn " + str(turnCounter) + " ##########\n")

    #pick a move, get possible moves
    currentState = tree.Node(0, copy.deepcopy(mainBoard))

    #debugging
    #print("currentState tree:")
    #tree.printTree(currentState)

    currentState.nextTurns = brain.getPossibleStates(currentState, turnCounter, 0)
    brain.minimax(currentState, turnCounter, 0)

    #print("tree after minimax:")
    #tree.printTree(currentState)

    #make move based off current player
    if turnCounter % 2 == 0:        #white's turn
        print("White's Turn...")
        for i in range(len(currentState.nextTurns)):
            if currentState.heuristic == tree.maxHeuristic(currentState.nextTurns[i]):
                mainBoard = currentState.nextTurns[i].state
                break

    elif turnCounter % 2 == 1:        #black's turn
        print("Black's Turn...")
        for j in range(len(currentState.nextTurns)):
            if currentState.heuristic == tree.minHeuristic(currentState.nextTurns[j]):
                mainBoard = currentState.nextTurns[j].state
                break

    turnCounter += 1

    print("Turn: " + str(turnCounter))
    print("Selected Heuristic: " + str(currentState.heuristic))
    board.printBoard(mainBoard)

    currentState = None

    #print("end turn tree:")
    #tree.printTree(currentState) 

#end while not endGame

print("\n\n\n##### GAME OVER #####")
print("Turns made: " + str(turnCounter) + ".\n")
print("Final state of board:\n")
board.printBoard(mainBoard)
