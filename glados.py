import board
import player
import brainV2
import tree
import copy
import math
import AlphaBeta
import minimax

from timeit import default_timer as timer
from datetime import timedelta

print("\n################### Start glados.py ###################\n")

winCounter = [0, 0]
printTurns = True
numGames = 1
setMinimax = False
turnCap = math.inf

for i in range(numGames):

    print("\n##### Start glados GAME #####\n")
    
    mainBoard = board.board(8, 8, '[]', ['L', 'F', 'R'])

    player01 = player.player('WW', 0, 1, {player.runForward}, mainBoard)
    player02 = player.player('BB', 1, 1, {player.runForward}, mainBoard)    
    player.setOpponents(player01, player02)
    board.setStartingPieces(player01)
    board.setStartingPieces(player02)
    board.printBoard(mainBoard.field)

    currentPlayer = player01
    turnCounter = 0

    while(not(brainV2.endGame(mainBoard.field, currentPlayer.opponent)) and turnCounter <= turnCap):

        #print("Current Player:" + str(currentPlayer))
        #print(".", end="")


        currentState = tree.Node(0, copy.deepcopy(mainBoard.field))
        currentState.nextTurns = brainV2.getPossibleStates(currentPlayer, currentState, turnCounter, 0)

        if setMinimax:
            start = 0
            end = 0
            start=timer()
            minimax.minimax(currentState, 0)
            end = timer()
            print("The amout of time that minimax took:", timedelta(seconds = end - start))

        if not setMinimax:
            AlphaBeta.alphaBeta(currentState, 0, (0-math.inf), (math.inf))
        

        #debugging
        """
        if (turnCounter < 2):
            print("####### Current State Tree for Turn " + str(turnCounter) + ".#######\n") 
            tree.printTree(currentState)
            print("####### End Tree " + str(turnCounter) + "#######\n\n") 
        """

        #find best move
        for i in range(len(currentState.nextTurns)):
            if currentState.heuristic == tree.maxHeuristic(currentState.nextTurns[i]):
                #if(turnCounter % 2 == 1):       #debugging
                #    print("EUREKA!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                mainBoard.field = currentState.nextTurns[i].state
                break

        if printTurns:
            print("Player " + str(currentPlayer.turn) + "'s turn:")
            print("Turn: " + str(turnCounter))
            print("Selected Heuristic: " + str(currentState.heuristic))
            board.printBoard(mainBoard.field)
        

        turnCounter += 1
        currentPlayer = currentPlayer.opponent
        currentState = None

    #end while not endGame

    print("\n\n\n##### GAME OVER #####")
    print("Turns made: " + str(turnCounter) + ".\n")
    print("Winner Player: " + str((turnCounter-1)%2))
    print("Final state of board:\n")
    board.printBoard(mainBoard.field)
    winCounter[(turnCounter-1)%2] += 1

    print("Wins:")
    print(winCounter)

#end for 10 games

