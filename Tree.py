#testing how to make a binary tree

#create class that represents an individual node in
#a binary tree

row = 8
col = 8

#character token to represent an empty space on the board
blankSpace = '[]'
#character token to represent spaces occupied by player pieces
blackToken = 'BB'
whiteToken = 'WW'



#initialize the board with [] to represent squares
fBoard = [[blankSpace for i in range(col)]for j in range(row)]
#end createBoard

class Node:
    def __init__(self, key, fBoard):
        self.left = None
        self.right = None

        self.val = key
        self.state = fBoard

##### recursive function to add new node to the tree
def insert(root, key, fBoard): 
    if root is None : 
        return Node(key, fBoard) 
    else: 
        if key <= root.val: 
           root.left = insert(root.left, key, fBoard) 
        else: 
            root.right = insert(root.right, key, fBoard) 
        return root
        

root = None
root = insert(root, 6 , fBoard)
insert(root, 2 , fBoard)
insert(root, 3 , fBoard)
insert(root, 20 , fBoard)


#prints the binary tree in order form when tehe data was entered
def printInorder(root, fBoard): 
  
    if root: 
  
        # First recur on left child 
        printInorder(root.left, fBoard)
  
  
        # then print the data of node 
        print(root.val)
        for row in fBoard:
            print(*row) 
           
        
        # now recur on right child 
        printInorder(root.right, fBoard) 
       

printInorder(root,fBoard)

#put an "Heuristic" after min and max to reduce the confusion of using the functions we defined vs the ones built into python
#find the Heuristic with the highest value 
def maxHeuristic(root): 
      
    if root.right == None:
        return root.key
    else:
        return minHeuristic(root.right)

#find the Heuristic with the lowest value
def minHeuristic(root):
    if root.left == None:
        return root.val
    else:
        return minHeuristic(root.left)

print(maxHeuristic(root))
print(minHeuristic(root))
