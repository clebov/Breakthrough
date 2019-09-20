#this file contains methods that control the main AI of the program
#   it will include methods to decide on potential moves and scan game states 
#       multiple turns ahead in order to decide on potential game states. 
#   it will include heuristic methods to determine game states more
#       suitable to given strategies

import copy
import Tree
import random

#get row and columns from board.py
import board
row = board.row
col = board.col



#method to create and return a list of game possible states
#   returns a binary search tree of possible game states
#   accessible from a parameterized list of current game states
#   a "state" is a copy of a board
#   in MAIN a board should not be passed into this function, but should be 
#       appended to an empty list first
def getPossibleStates(fCurrentStates, fCurrentTurn):

    #define tree to be returned at end of function
    newStates = None

    #char list of possible moves, left, forward, right, for looping. 
    moves = {'L', 'F', 'R'}

    #get current player
    playerToken = None
    if fCurrentTurn % 2 == 0:       #white
        playerToken == board.whiteToken
    elif fCurrentTurn % 2 == 1:     #black
        playerToken == board.blackToken

    #for each possible move from current states
    for a in range(len(fCurrentStates)):
        for i in range(row):
            for j in range(col):
                #print("Checking moves from:\n")
                #board.printBoard(fCurrentStates[a])
                for move in moves:
                    #tempState.append(copy.deepcopy(pState[a]))
                    #[tempIndexCounter]
                    tempState = copy.deepcopy(fCurrentStates[a])
                    if(board.makeMove(tempState, int(i), int(j), move)):
                        board.printBoard(tempState)
                        #newStates.append(tempState)
                        #create node with heuristic and state

                        #add node to tree

    #end for a, i, j

    #print("\n\n\n\n\n\n\n\n\n\n\n\n\n#############################")
    #Tree.inorder(newStates) 
    return newStates 

#end getPossibleStates

def getHeuristic():
    h = random.random()
    print("getHeuristic: heuristic returned: " + str(h) + ".\n")
    return h 
