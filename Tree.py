#testing how to make a binary tree
#create class that represents an individual node in
#a binary tree

#TODO
#1. make binary tree
#2. creat the maxHeuristic and minHeuristic
#3. find a way to pass the state and Heuristic to the binary tree (Dylan currently working on in brain.py)
#4.

import board

row = 8
col = 8

#character token to represent an empty space on the board
blankSpace = '[]'
#character token to represent spaces occupied by player pieces
blackToken = 'BB'
whiteToken = 'WW'

#initialize the board with [] to represent squares
fState = [[blankSpace for i in range(col)]for j in range(row)]

#end createBoard
#put an "Heuristic" after min and max to reduce the confusion of using the functions we defined vs the ones built into python
#find the Heuristic with the highest value 
#rewrite min max and inorder to search next turns to find the specific value

class Node(object):
    def __init__(self, key, fState):
        self.nextTurns = []
        self.heuristic = key
        self.state = fState

    def __cmp__(self, other):
        if hasattr(other, 'heuristic'):
            return self.heuristic.__cmp__(other.heuristic)


def maxHeuristic(root): 
      
    if root.right == None:
        return root
    else:
        return minHeuristic(root.right)

def createNode(key,fState):
    return Node(key,fState)



#find the Heuristic with the lowest value
def minHeuristic(root):
    if root.left == None:
        return root
    else:
        return minHeuristic(root.left)

##### recursive function to add new node to the tree
def insert(root, key, fState): 
    if root == None: 
        return createNode(key,fState)
    else: 
        root.nextTurns.append((Node(key, fState)))
        sorted(root.nextTurns)    
        
#prints the binary tree in order form when tehe data was entered
def printInorder(root): 
  
    if root:
        # then print the data of node 
        for i in int (range(root.nextTurns)):
            print(root.heuristic)
        for i in int(range(root.nextTurns)):
            print(printInorder(root.nextTurns[i]))
   
        
root = None
root = insert(root, 9 , fState)
insert(root, 6 , fState)
insert(root, 2 , fState)
insert(root, 3 , fState)
insert(root, 20 , fState)
printInorder(root)

print()
print()
#print(maxHeuristic(root).heuristic)
#board.printBoard(maxHeuristic(root).state)
#print(minHeuristic(root).heuristic)
