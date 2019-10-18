import math

class Node(object):
    def __init__(self, fKey, fState):
        self.heuristic = fKey
        self.state = fState
        self.nextTurns = []     #list of nodes

def maxHeuristic(fNode): 
    max = (0-math.inf)
    for i in range(len(fNode.nextTurns)):
        if fNode.nextTurns[i].heuristic > max:
            max = fNode.nextTurns[i].heuristic
    return max