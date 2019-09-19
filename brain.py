#this file contains methods that control the main AI of the program
#   it will include methods to decide on potential moves and scan game states 
#       multiple turns ahead in order to decide on potential game states. 
#   it will include heuristic methods to determine game states more
#       suitable to given strategies

import copy

#get row and columns from board.py
import board
row = board.row
col = board.col



#method to create and return a list of game possible states
#   accessible from a parameterized list of current game states
#   a "state" is a copy of a board
#   in MAIN a board should not be passed into this function, but should be 
#       appended to an empty list first
def getPossibleStates(fCurrentStates, fCurrentTurn):
    #holds one state to be stored into newStates
    pState = copy.deepcopy(fCurrentStates)
    tempState = []
    tempIndexCounter = 0
    newStates = []
    moves = {'L', 'F', 'R'}
    for a in range(len(fCurrentStates)):
        #make empty binary tree

        for i in range(row):
            for j in range(col):
                #print("Checking moves from:\n")
                #board.printBoard(fCurrentStates[a])
                for move in moves:
                    tempState.append(copy.deepcopy(pState[a]))
                    if(board.makeMove(tempState[tempIndexCounter], int(i), int(j), move)):
                        board.printBoard(tempState[tempIndexCounter])
                        newStates.append(tempState[tempIndexCounter])
                        #create node with heuristic and state

                        #add node to tree

                    tempIndexCounter+=1
        #end for i, j
