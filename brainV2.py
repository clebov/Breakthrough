import player
import treeV2
import boardV2

import math
import copy

searchDepth = 3


def getPossibleStates(fPlayer, fState, fCurrentTurn, fDepth):
    global searchDepth

    #define tree to be returned at end of function
    newStates = []

    #get current player
    #if fCurrentTurn % 2 == fPlayer.turn:
    #for each possible move from current states
    for i in range(fPlayer.board.row):
        #debugging, this loop takes a long time to complete so this is to know it's in progress
        #print("thinking...")
        for j in range(fPlayer.board.col):
            
            #if a space contains a piece of the current player
            if fState.state[i][j] == fPlayer.token: 
                #check all valid moves that player can make from the current state
                for move in fPlayer.board.moves:
                    tempState = copy.deepcopy(fState.state)
                    if(boardV2.makeMove(tempState, fPlayer, int(i), int(j), move)):
                        #if producing a terminal node, calculate heuristic
                        h = 0
                        if(fDepth == searchDepth-1):
                            h = player.highHeuristic(fPlayer, copy.deepcopy(tempState))
                        #if a valid move can be made, add that move to the list of possible next turns
                        newStates.append(treeV2.Node(h, copy.deepcopy(tempState))) 
                        boardV2.nodeCounter += 1
                        #board.printBoard(tempState)
    #end for i, j

    #recurse to the appropriate depth
    if fDepth < searchDepth-1:
        for b in range(len(newStates)):
            #print("HEllo World")
            newStates[b].nextTurns = getPossibleStates(fPlayer.opponent, newStates[b], fCurrentTurn+1, fDepth+1)
    
    #return the list of possible states to the appropriate depth back to 
    #   the nextTurns value of the fCurrentState node.
    return newStates 

#end getPossibleStates


#minimax
def minimax(fNode, fDepth):

    """
    start = 0
    end = 0
    start=timer()
    """

    #all trees should be built to global searchDepth variable
    #   so we know at that depth is the terminal nodes
    global searchDepth

    if fDepth < searchDepth-1:
        d = 1
        while (d <= searchDepth-1):
            for i in range(len(fNode.nextTurns)):
                minimax(fNode.nextTurns[i], fDepth+d)
            d+=1
    else:
        #if white player (even turns), use max heuristic
        if fDepth % 2 == 0:
            fNode.heuristic = treeV2.maxHeuristic(fNode)
        #if black player (odd turns), use min heuristic
        elif fDepth % 2 == 1:
            fNode.heuristic = treeV2.maxHeuristic(fNode)

    #if white player (even turns), use max heuristic
    if fDepth % 2 == 0:
        fNode.heuristic = treeV2.maxHeuristic(fNode)
    #if black player (odd turns), use min heuristic
    elif fDepth % 2 == 1:
        fNode.heuristic = treeV2.maxHeuristic(fNode)

    #print("The amout of time that minimax took:", timedelta(seconds = end - start))
#end minimax


def alphaBeta(fNode,fTurn,alpha,beta):
    MAX = math.inf
    MIN = (0-math.inf)


    start = 0
    end = 0

    #start=timer()
    #all trees should be built to global searchDepth variable
    #   so we know at that depth is the terminal nodes
    global searchDepth
    # find the layer of the tree that contains the terminal nondes and returns the minimax avalues of those nodes  before starting the layer above it
    
    if (True):
    #if fTurn % 2 == 0:
        best = MIN     
        for i in range(len(fNode.nextTurns)):
            for j in range(len(fNode.nextTurns[i].nextTurns)):                     
                val = treeV2.maxHeuristic(fNode.nextTurns[i].nextTurns[j])
                best = max(best,val)
                alpha = max(alpha,best)
                if beta<=alpha:
                    break
                fNode.nextTurns[i].nextTurns[j].heuristic = best
            #end for j
        #end for i

        best = MIN
        for k in range(len(fNode.nextTurns)):
            val = treeV2.maxHeuristic(fNode.nextTurns[k])
            best = max(best,val)
            alpha = max(alpha,best)
            if beta<=alpha:
                break
            fNode.nextTurns[k].heuristic = best

        fNode.heuristic = treeV2.maxHeuristic(fNode) 
    """
    else:
        best = MAX
        for i in range(len(fNode.nextTurns)): 
            
            for j in range(len(fNode.nextTurns[i].nextTurns)):
                val = treeV2.minHeuristic(fNode.nextTurns[i].nextTurns[j])
                best = min(best, val)
                beta = min(beta, best)
            if beta <= alpha:                
                break
        fNode.heuristic = best
    """
    #end = timer()
    #print("The amout of time that AlphaBeta took:", timedelta(seconds = end - start))


#check for win condition and return
def endGame(fBoard, fPlayer):
    win = False
    for i in range(fPlayer.board.col):
        if (fBoard[((fPlayer.board.row-1)*fPlayer.turn)][i] == fPlayer.token):
            win = True
    return win
#end endGame

