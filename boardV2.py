import tree
import brainV2
import player
import display
import copy
import math
from timeit import default_timer as timer
nodeCounter = 0

#create a board object
class board(object):
    def __init__(self, row, col, blank, moves):
        self.row = row
        self.col = col
        self.blank = blank
        self.moves = moves
        self.field = [[blank for i in range(col)]for j in range(row)]

    def print(self):
        printBoard(self.field)
#end board class


#print the board
def printBoard(fBoard):
    for row in fBoard:
        print(*row) 
    print("\n")
#end printBoard


#place the starting pieces on the board
#   BB is a black piece and WW is a white piece
def setStartingPieces(fPlayer):
    #if first player
    if fPlayer.turn == 0:
        for i in range(fPlayer.board.col):
            fPlayer.board.field[fPlayer.board.row - 1][i] = fPlayer.token
            fPlayer.board.field[fPlayer.board.row - 2][i] = fPlayer.token
    #if first player
    elif fPlayer.turn == 1:
        for i in range(fPlayer.board.col):
            fPlayer.board.field[0][i] = fPlayer.token
            fPlayer.board.field[1][i] = fPlayer.token
    else:
        print("Error: boardV2.py: setStartingPieces: " + "player has invalid turn order: " + str(fPlayer))
#end setStartingPieces


#check if a location is on the board
def isOnBoard(fBoard, fRow, fCol):
    if (fRow >= 0 and fRow < fBoard.row and fCol >= 0 and fCol < fBoard.col):
        return True
    else:
        return False
#end isValid


#make a valid move, follows game rules for Breakthrough
#   returns true if a move was made or false if an error was found
#   player will be 0 for White, or 1 for Black
#   move refers to a character, L, F, or R, to reference a left, forward, or
#   right move
#   left and right flip orientation depending on the player
#       (black is at the top facing down, white is at the bottom facing up)
def makeMove(fBoard, fPlayer, oldRow, oldCol, move):
    #TODO: CHRIS: Copy this function and rename the copy as
    #makeMoveGUI([params])
    
    #check that valid space is being targeted
    if (not(isOnBoard(fPlayer.board, oldRow, oldCol))):
        #print("Error, makeMove: targeted space is not on the board.")
        return False

    #determine if a piece is being targeted and which player
    if fBoard[oldRow][oldCol] == fPlayer.board.blank:
        #print("Error, makeMove: please target a piece, not an empty space.\n")
        return False
    

    #determine vertical direction, up or down
    #   remember the list indeces for the vertical movement are reversed
    #       0 at top and 8 or row at bottom
    vert = 0
    if fPlayer.turn == 0:    #white
        vert = -1
    elif fPlayer.turn == 1:  #black
        vert = 1
    else:
        #print("Error, makeMove: please enter valid player (0 or 1).\n")
        return False

    #determine horizontal direction if any, left or right
    horiz = 0
    if move == 'F':     #forward
        None
    elif move == 'L':   #left
        horiz = vert
    elif move == 'R':   #right
        horiz = 0 - vert
    else:
        #print("Error, makeMove: please enter a valid move (L, F, or R)\n")
        return False

    #candidate coordinates for new move
    newRow = oldRow + vert
    newCol = oldCol + horiz

    #determine if potential move is on board
    if(not(isOnBoard(fPlayer.board, newRow, newCol))):
        #print("Error, makeMove: candidate move goes off the board.\n")
        return False
    

    #determine if potential move is blocked
    #blocked by a friendly piece
    if(fBoard[newRow][newCol] == fPlayer.token):
        #print("Error, makeMove: cannot move into friendly piece " +
        #playerToken +
        #      " at (" + str(newRow) + ", " + str(newCol) + "): " +
        #      fBoard[newRow][newCol] + ".\n")
        return False

    #blocked by enemy piece in front of player
    if(move == 'F' and (fBoard[newRow][newCol] != fPlayer.board.blank)):
        #print("Error, makeMove: cannot move directly forward into enemy piece
        #" +
        #      enemyToken + " at (" + str(newRow) + ", " + str(newCol) +
        #      ").\n")
        return False

    #at this point, the new move is:
    #   on the board
    #   is not blocked by a friendly piece at all
    #   is not block by an enemy piece if it is a forward move
    #therefore move piece
    #print("makeMove: moving piece " + fBoard[oldRow][oldCol] + " from (" +
    #      str(oldRow) + ", " + str(oldCol) + ") to (" +
    #      str(newRow) + ", " + str(newCol) + ").")
    fBoard[newRow][newCol] = fPlayer.token
    fBoard[oldRow][oldCol] = fPlayer.board.blank
    return True

#end makeMove


#detect captured piece
#compared two board states and determines whether a piece was captured
def findCapturedPieces(fPlayer, fOldState, fNewState):
    oldNumPieces = 0
    newNumPieces = 0
    
    for i in range(fPlayer.board.row):
        for j in range(fPlayer.board.col):
            if fOldState[i][j] == fPlayer.opponent.token:
                oldNumPieces += 1
            if fNewState[i][j] == fPlayer.opponent.token:
                newNumPieces += 1
    #end for i and j

    if newNumPieces < oldNumPieces:
        return True
    else:
        return False
#end find captured pieces


#bestMoveIndex
#   finds and returns the index of the best move in an array such that
#       it has the highest heuristic but does not lead to a losing move when
#       the opponent takes the next turn.
#   This should ensure if the player is about to lose due to his openent 
#       moving to the his home row, that he does not take a turn which allows that to happen.
def bestMoveIndex(fPlayer, fCurrentState):

    #if player can win, make move
    for j in range(len(fCurrentState.nextTurns)):
        if (brainV2.endGame(fCurrentState.nextTurns[j].state, fPlayer)):
            return j

    #find best non-losing move
    best = 0
    for i in range(len(fCurrentState.nextTurns)):
        if(fCurrentState.nextTurns[best].heuristic < fCurrentState.nextTurns[i].heuristic):
            fail = False
            for each in fCurrentState.nextTurns[i].nextTurns:
                if brainV2.endGame(each.state, fPlayer.opponent):
                    fail = True
            
            if not fail:
                best = i
    #end for i in nextTurns
    return best
#end bestMoveIndex


#run game
#   takes two player objects and a board object as parameters
#   returns a list of game statistics, gameStats, including:
#   0: the winner of the game 
#   1: the turn counter
#   2: final state of the board
#   3: player 1 total nodes 
#   4: player 2 total nodes
#   5: player 1 workers captured 
#   6: player 2 workers captured
#   7: average runtime for AlphaBeta
#   8: average runtime for MiniMax
def runGame(fPlayer1, fPlayer2, fBoard, match):

    #initialize game stats
    gameStats = ['', 0, None, 0, 0, 0,0,0,0] 

    #list to keep track of the time it takes to run AlphaBeta
    timerAB = []
    #list to keep track of teh time it take to run MiniMax
    timerMM = []

    #set counters for game stats
    global nodeCounter
    turnCounter = 0
    p1nodes = 0
    p2nodes = 0
    p1captures = 0
    p2captures = 0
    abCounter = 0
    mmCounter = 0
    totalAB = 0
    totalMM = 0

    start = 0
    end = 0
    
    display.printMatch(match)

    #get players ready
    player.setOpponents(fPlayer1, fPlayer2)
    setStartingPieces(fPlayer1)
    setStartingPieces(fPlayer2)
    
    #find first player
    if(fPlayer1.turn == 0):
        currentPlayer = fPlayer1
    else:
        currentPlayer = fPlayer2
    #end if else currentPlayer

    display.draw_board(fBoard)

    #start game
    while(not(brainV2.endGame(fBoard.field, currentPlayer.opponent))):

        #establish current state of board
        currentState = tree.Node(0, copy.deepcopy(fBoard.field))

        #find next available moves
        currentState.nextTurns = brainV2.getPossibleStates(currentPlayer, currentState, turnCounter, 0)

        #output node tree
        """
        outfile = "outputFiles/treeForTurn_" + str(turnCounter) + ".txt"
        tree.writeTree(currentState, outfile)
        """

        #increment node counters for current player
        if(turnCounter % 2 == 0):
            p1nodes += nodeCounter
        else:
            p2nodes += nodeCounter
        nodeCounter = 0

        #apply alphabeta or minimax based off player's strategy
        if(currentPlayer.algorithm):

            start=timer()
            brainV2.alphaBeta(currentState, 0, (0 - math.inf), (math.inf))
            end = timer()

            totalAB += (end-start)
            abCounter+=1
        else:
            start=timer()
            brainV2.minimax(currentState, 0) 
            end = timer()

            totalMM += (end-start)
            mmCounter+=1
            gameStats[8] = totalMM / mmCounter

        start = 0
        end = 0

        #find best non-losing move
        best = bestMoveIndex(currentPlayer, currentState)
        """
        for i in range(len(currentState.nextTurns)):
            if((currentState.nextTurns[best].heuristic < currentState.nextTurns[i].heuristic) and not(brainV2.endGame(currentState.nextTurns[i].state, currentPlayer.opponent))):
                best = i
        #end for i in nextTurns
        """

		#increment captured pieces counter for current player
        if(findCapturedPieces(currentPlayer, currentState.state, currentState.nextTurns[best].state)):
            if(turnCounter % 2 == 0):
                p2captures += 1
            else:
                p1captures += 1

        #make best move
        fBoard.field = currentState.nextTurns[best].state


        display.draw_board(fBoard)


        #print turn
        """
        print("Player " + str(currentPlayer.turn) + "'s turn:")
        print("Turn: " + str(turnCounter))
        print("Selected Heuristic: " + str(currentState.heuristic))
        printBoard(fBoard.field)
        """
       
        #get ready for next turn
        turnCounter += 1
        currentPlayer = currentPlayer.opponent
        currentState = None

    #end while not endGame

    gameStats[0] = currentPlayer.opponent.name
    gameStats[1] = turnCounter 
    gameStats[2] = fBoard.field
    gameStats[3] = p1nodes
    gameStats[4] = p2nodes
    gameStats[5] = p1captures
    gameStats[6] = p2captures
    gameStats[7] = totalAB / abCounter
    

    
    display.message_display(gameStats)
    
    
    print("\n\n\n##### GAME OVER #####")
    print("Turns made: " + str(turnCounter) + ".\n")
    print("Winner: " + currentPlayer.opponent.name + "!")
    print("Final state of board:\n")
    printBoard(fBoard.field)
    #winCounter[(turnCounter-1)%2] += 1
    display.draw_board(fBoard)
   
    
    nodeCounter = 0

    return gameStats

#end run game