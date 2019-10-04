import tree
import brainV2

from timeit import default_timer as timer
from datetime import timedelta
searchDepth = brainV2.searchDepth

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
            fNode.heuristic = tree.maxHeuristic(fNode)
        #if black player (odd turns), use min heuristic
        elif fDepth % 2 == 1:
            fNode.heuristic = tree.minHeuristic(fNode)

    #if white player (even turns), use max heuristic
    if fDepth % 2 == 0:
        fNode.heuristic = tree.maxHeuristic(fNode)
    #if black player (odd turns), use min heuristic
    elif fDepth % 2 == 1:
        fNode.heuristic = tree.minHeuristic(fNode)

    #print("The amout of time that minimax took:", timedelta(seconds = end - start))
#end minimax

