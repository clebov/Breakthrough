#testing how to make a binary tree
#create class that represents an individual node in
#a binary tree

#TODO
#1. make binary tree
#2. creat the maxHeuristic and minHeuristic
#3. find a way to pass the state and Heuristic to the binary tree (Dylan currently working on in brain.py)
#4.

import board
import copy

row = board.row
col = board.col

#character token to represent an empty space on the board
blankSpace = board.blankSpace
#character token to represent spaces occupied by player pieces
blackToken = board.blackToken
whiteToken = board.whiteToken

#initialize the board with [] to represent squares
treeBoard = [[blankSpace for i in range(col)]for j in range(row)]

#end createBoard
#put an "Heuristic" after min and max to reduce the confusion of using the functions we defined vs the ones built into python
#find the Heuristic with the highest value 
#rewrite min max and inorder to search next turns to find the specific value

class Node(object):
    def __init__(self, key, fState):
        self.nextTurns = []
        self.heuristic = key
        self.state = fState


#def createNode(key,fState):
#    return Node(key, fState) 

def getNodeKey(thisNode):
    return thisNode.heuristic

def maxHeuristic(root): 
      
    if root.right == None:
        return root
    else:
        return minHeuristic(root.right)

#find the Heuristic with the lowest value
def minHeuristic(root):
    if root.left == None:
        return root
    else:
        return minHeuristic(root.left)

##### recursive function to add new node to the tree
def insert(root, key, fState): 
    if root == None: 
        return Node(key,fState)
    else: 
        root.nextTurns.append((Node(key, fState)))
        #sorted(root.nextTurns, key = getNodeKey)    
        
#prints the binary tree in order form when tehe data was entered
def printTree(root): 
    if root:
        counter = 0
        #then print the data of node 
        print(counter)
        print(root.heuristic)
        board.printBoard(root.state)
        counter += 1
        for i in range(len(root.nextTurns)):
            print(counter)
            print(root.nextTurns[i].heuristic)
            board.printBoard(root.nextTurns[i].state)
            counter += 1
#end print

#testing
"""
root = None
root = insert(root, 9 , copy.deepcopy(treeBoard))
insert(root, 6 , copy.deepcopy(treeBoard))
insert(root, 2 , copy.deepcopy(treeBoard))
board.setStartingPieces(treeBoard) 
insert(root, 3 , copy.deepcopy(treeBoard))
insert(root, 20 , copy.deepcopy(treeBoard))
printTree(root)

print()
print()
"""
#print(maxHeuristic(root).heuristic)
#board.printBoard(maxHeuristic(root).state)
#print(minHeuristic(root).heuristic)