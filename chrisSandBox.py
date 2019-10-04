import brain
import tree
import copy
class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key 

currentState = tree.Node(0, copy.deepcopy(mainBoard))
currentState.nextTurns = [4,3,5,123,125,1,5,8,1]
turn = 0
# create root 


brain.alphaBeta(currentState, turn, 0)
tree.printTree