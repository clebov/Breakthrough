import brainV2
import math
import tree

from timeit import default_timer as timer
from datetime import timedelta


def alphaBeta(fNode,fTurn,alpha,beta):
    MAX = math.inf
    MIN = (0-math.inf)


    start = 0
    end = 0

    start=timer()
    #all trees should be built to global searchDepth variable
    #   so we know at that depth is the terminal nodes
    global searchDepth
    # find the layer of the tree that contains the terminal nondes and returns the minimax avalues of those nodes  before starting the layer above it
    
    if (True):
    #if fTurn % 2 == 0:
        best = MIN     
        for i in range(len(fNode.nextTurns)):
            for j in range(len(fNode.nextTurns[i].nextTurns)):                     
                val = tree.maxHeuristic(fNode.nextTurns[i].nextTurns[j])
                best = max(best,val)
                alpha = max(alpha,best)
                if beta<=alpha:
                    break
                fNode.nextTurns[i].nextTurns[j].heuristic = best
            #end for j
        #end for i

        best = MIN
        for k in range(len(fNode.nextTurns)):
            val = tree.maxHeuristic(fNode.nextTurns[k])
            best = max(best,val)
            alpha = max(alpha,best)
            if beta<=alpha:
                break
            fNode.nextTurns[k].heuristic = best

        fNode.heuristic = tree.maxHeuristic(fNode) 
    else:
        best = MAX
        for i in range(len(fNode.nextTurns)): 
            
            for j in range(len(fNode.nextTurns[i].nextTurns)):
                val = tree.minHeuristic(fNode.nextTurns[i].nextTurns[j])
                best = min(best, val)
                beta = min(beta, best)
            if beta <= alpha:                
                break
        fNode.heuristic = best
    end = timer()
    print("The amout of time that AlphaBeta took:", timedelta(seconds = end - start))