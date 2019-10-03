import board
import player
import brain
import brainV2
import tree
import copy

print("\n################### Start glados.py ###################\n")

winCounter = [0, 0]

for i in range(10):

    mainBoard = board.board(5, 5, '_', {'L', 'F', 'R'})

    player01 = player.player('W', 0, 1, {player.offensiveHeuristic}, mainBoard)
    player02 = player.player('B', 1, 1, {player.offensiveHeuristic}, mainBoard)
    player.setOpponents(player01, player02)
    board.setStartingPieces(player01)
    board.setStartingPieces(player02)
    board.printBoard(mainBoard.field)

    print("\n##### Start glados GAME #####\n")

    currentPlayer = player01
    turnCounter = 0

    while(not(brainV2.endGame(mainBoard, currentPlayer.opponent))):

        #print("Current Player:" + str(currentPlayer))
        #print(".", end="")


        currentState = tree.Node(0, copy.deepcopy(mainBoard.field))
        currentState.nextTurns = brainV2.getPossibleStates(currentPlayer, currentState, turnCounter, 0)
        brain.minimax(currentState, turnCounter, 0)
    
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

        """
        print("Player " + str(currentPlayer.turn) + "'s turn:")
        print("Turn: " + str(turnCounter))
        print("Selected Heuristic: " + str(currentState.heuristic))
        board.printBoard(mainBoard.field)
        """

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
#end for 10 games

print("Wins:")
print(winCounter)
