import tree
import brainV2

searchDepth = brainV2.searchDepth

#minimax
def minimax(fNode, fDepth):
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
#end minimax