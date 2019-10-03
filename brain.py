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
#   default to 3, more layers are possible but dramatically increase processing time
searchDepth = 3



#method to create and return a list of game possible states
#   accessible from a parameterized node of the current game state
#   in Main a node must be constructed with heuristic (key) of 0 and 
#       the current game state to be passed into fCurrentState
#   in Main fDepth should always be passed in as 1, since 
#       the current state is layer 0 and the possible states start at layer 1
def getPossibleStates(fCurrentState, fCurrentTurn, fDepth):

    #define tree to be returned at end of function
    newStates = []

    #get current player
    playerToken = ''
    if fCurrentTurn % 2 == 0:       #white
        playerToken = board.whiteToken
    elif fCurrentTurn % 2 == 1:     #black
        playerToken = board.blackToken

    #for each possible move from current states
    for i in range(row):
        #debugging, this loop takes a long time to complete so this is to know it's in progress
        #print("thinking...")
        for j in range(col):
            #if a space contains a piece of the current player
            if fCurrentState.state[i][j] == playerToken: 
                #check all valid moves that player can make from the current state
                for move in board.moves:
                    tempState = copy.deepcopy(fCurrentState.state)
                    if(board.makeMove(tempState, int(i), int(j), move)):
                        #if a valid move can be made, add that move to the list of possible next turns
                        newStates.append(tree.Node(getHeuristic(tempState), copy.deepcopy(tempState))) 

    #end for i, j

    #recurse to the appropriate depth
    global searchDepth
    if fDepth < searchDepth-1:
        for b in range(len(newStates)):
            newStates[b].nextTurns = getPossibleStates(newStates[b], fCurrentTurn+1, fDepth+1)
    
    #return the list of possible states to the appropriate depth back to 
    #   the nextTurns value of the fCurrentState node.
    return newStates 

#end getPossibleStates


#find the heuristic value of a given node
#   the heuristic is defined as the number of white peices on a board. 
#   the white player if playing defensively will search for a higher heureistic
#   the black player if playing offensivley will search for a lower heuristic
#   a random float >=0 but <1 is added to break ties.
def getHeuristic(fState):
    #add randomnes to break ties
    h = random.random()

    #add the number of white tokens 
    for i in range(row):
        for j in range(col):
            if fState[i][j] == board.whiteToken:
                h += 1
    
    #print("getHeuristic: heuristic returned: " + str(h) + ".\n")
    return h 
#end getHeuristic


#minimax
def minimax(fNode, fTurn, fDepth):
    #all trees should be built to global searchDepth variable
    #   so we know at that depth is the terminal nodes
    global searchDepth

    if fDepth < searchDepth-1:
        d = 1
        while (d <= searchDepth-1):
            for i in range(len(fNode.nextTurns)):
                minimax(fNode.nextTurns[i], fTurn+d, fDepth+d)
            d+=1
    else:
        #if white player (even turns), use max heuristic
        if fTurn % 2 == 0:
            fNode.heuristic = tree.maxHeuristic(fNode)
        #if black player (odd turns), use min heuristic
        elif fTurn % 2 == 1:
            fNode.heuristic = tree.maxHeuristic(fNode)

    #if white player (even turns), use max heuristic
    if fTurn % 2 == 0:
        fNode.heuristic = tree.maxHeuristic(fNode)
    #if black player (odd turns), use min heuristic
    elif fTurn % 2 == 1:
        fNode.heuristic = tree.maxHeuristic(fNode)
#end minimax

            