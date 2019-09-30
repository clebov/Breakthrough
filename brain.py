#this file contains methods that control the main AI of the program
#   it will include methods to decide on potential moves and scan game states 
#       multiple turns ahead in order to decide on potential game states. 
#   it will include heuristic methods to determine game states more
#       suitable to given strategies

import copy
import tree
import random

#get row and columns from board.py
import board
row = board.row
col = board.col

#set the layer depth at which search trees will be made
searchDepth = 3



#method to create and return a list of game possible states
#   returns a binary search tree of possible game states
#   accessible from a parameterized list of current game states
#   a "state" is a copy of a board
#   in MAIN a board should not be passed into this function, but should be 
#       appended to an empty list first
def getPossibleStates(fCurrentState, fCurrentTurn, fDepth):

    #debugging:
    #print("DEBUGGING: GETPOSSIBLESTATES: FINDME: DEPTH: " + str(fDepth)) 

    #define tree to be returned at end of function
    newStates = []
    #newStates = tree.insert(newStates, 0, copy.deepcopy(fCurrentState))

    #char list of possible moves, left, forward, right, for looping. 
    moves = {'L', 'F', 'R'}

    #get current player
    playerToken = ''
    if fCurrentTurn % 2 == 0:       #white
        #print("It is now White's turn") #debugging
        playerToken = board.whiteToken
        #print(board.whiteToken)
        #print(playerToken)
    elif fCurrentTurn % 2 == 1:     #black
        #print("It is now Black's turn") #debugging
        playerToken = board.blackToken

    #for each possible move from current states
    #for a in range(len(fCurrentState)):
    for i in range(row):
        for j in range(col):
            #print("Checking moves from:\n")
            #board.printBoard(fCurrentStates[a])
            if fCurrentState.state[i][j] == playerToken: 
                #print("FINDME: GETSTATES: IFPLAYERTOKENFOUND") #debugging
                for move in moves:
                    #tempState.append(copy.deepcopy(pState[a]))
                    #[tempIndexCounter]
                    tempState = copy.deepcopy(fCurrentState.state)
                    if(board.makeMove(tempState, int(i), int(j), move)):
                        print("thinking...")
                        #print("Valid move found: ")
                        #board.printBoard(tempState)
                        #add node to tree
                        #tree.insert(newStates, getHeuristic(tempState), copy.deepcopy(tempState))
                        newStates.append(tree.Node(getHeuristic(tempState), copy.deepcopy(tempState))) 

    #end for i, j
    global searchDepth
    #print("Hello, checking depth 01:" + str(fDepth) + " " + str(searchDepth))
    if fDepth < searchDepth:
        for b in range(len(newStates)):
            newStates[b].nextTurns = getPossibleStates(newStates[b], fCurrentTurn+1, fDepth+1)
        #debugging
    #    print("Hello, checking depth 02")

    #print("\n\n\n\n\n\n\n\n\n\n\n\n\n#############################")
    #Tree.inorder(newStates) 
    return newStates 

#end getPossibleStates


#find the heuristic value of a given node
#   the heuristic is defined as the number of white peices on a board. 
#   the white player if playing defensively will search for a higher heureistic
#   the black player if playing offensivley will search for a lower heuristic
#   a random float >=0 but <1 is added to break ties.
def getHeuristic(fState):
    h = random.random()

    #for a in range(len(fState)):
    for i in range(row):
        for j in range(col):
            if fState[i][j] == board.whiteToken:
                h += 1
    
    #print("getHeuristic: heuristic returned: " + str(h) + ".\n")
    return h 
#end getHeuristic