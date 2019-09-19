
#testing how to make a binary tree

#create class that represents an individual node in
#a binary tree

import brain
import Breakthrough

class Node:
    def __init__(self, key, fboard):
        self.left = None
        self.right = None
        self.val = key
        self.state = fboard

##### recursive function to add new node to the tree
def addNode(root, newNode):
    if root == None:
        root = newNode
    elif newNode.val <= root.val:
        addNode(root.left, newNode)
    elif newNode.val > root.val:
        addNode(root.right, newNode)
    else:
        # CHANGE THIS BEFORE DUE DATE!!!!!!!!
        print("sHiT HaPpEnD")

def Max(root):
    if root.right != None:
        return False





# Function to  print level order traversal of tree 
def printLevelOrder(root): 
    h = height(root) 
    for i in range(1, h+1): 
        printGivenLevel(root, i) 


""" Compute the height of a tree--the number of nodes 
    along the longest path from the root node down to 
    the farthest leaf node 
"""
def height(node): 
    if node is None: 
        return 0 
    else : 
        # Compute the height of each subtree  
        lheight = height(node.left) 
        rheight = height(node.right) 
  
        #Use the larger one 
        if lheight > rheight : 
            return lheight+1
        else: 
            return rheight+1
  
        #print the board
def inorder(tree):
  if tree != None:
      inorder(tree.getLeftChild())
      print(tree.getRootVal())
      inorder(tree.getRightChild())