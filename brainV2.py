
import copy
import board
import player
import tree
searchDepth = 3


def getPossibleStates(fPlayer, fState, fCurrentTurn, fDepth):
    #define tree to be returned at end of function
    newStates = []
    

    #get current player
    #if fCurrentTurn % 2 == fPlayer.turn:
    #for each possible move from current states
    for i in range(fPlayer.board.row):
        #debugging, this loop takes a long time to complete so this is to know it's in progress
        #print("thinking...")
        for j in range(fPlayer.board.col):
            
            #if a space contains a piece of the current player
            if fState.state[i][j] == fPlayer.token: 
                #check all valid moves that player can make from the current state
                for move in fPlayer.board.moves:
                    tempState = copy.deepcopy(fState.state)
                    if(board.makeMove(tempState, fPlayer, int(i), int(j), move)):
                        #if a valid move can be made, add that move to the list of possible next turns
                        newStates.append(tree.Node(player.highHeuristic(fPlayer, copy.deepcopy(tempState)), copy.deepcopy(tempState))) 
                        #board.printBoard(tempState)
    #end for i, j

    #recurse to the appropriate depth
    global searchDepth
    if fDepth < searchDepth-1:
        for b in range(len(newStates)):
            #print("HEllo World")
            newStates[b].nextTurns = getPossibleStates(fPlayer.opponent, newStates[b], fCurrentTurn+1, fDepth+1)
    
    #return the list of possible states to the appropriate depth back to 
    #   the nextTurns value of the fCurrentState node.
    return newStates 

#end getPossibleStates


#minimax
def minimax(fNode, fDepth):
    #all trees should be built to global searchDepth variable
    #   so we know at that depth is the terminal nodes
    global searchDepth

    if fDepth < searchDepth-1:
        d = 1
        while (d <= searchDepth-1):
            for i in range(len(fNode.nextTurns)):
                minimax(fNode.nextTurns[i], fDepth+d)
            d+=1
    else:
        #if white player (even turns), use max heuristic
        if fDepth % 2 == 0:
            fNode.heuristic = tree.maxHeuristic(fNode)
        #if black player (odd turns), use min heuristic
        elif fDepth % 2 == 1:
            fNode.heuristic = tree.minHeuristic(fNode)

    #if white player (even turns), use max heuristic
    if fDepth % 2 == 0:
        fNode.heuristic = tree.maxHeuristic(fNode)
    #if black player (odd turns), use min heuristic
    elif fDepth % 2 == 1:
        fNode.heuristic = tree.minHeuristic(fNode)
#end minimax


#check for win condition and return
def endGame(fBoard, fPlayer):
    win = False
    for i in range(fPlayer.board.col):
        if (fBoard[((fPlayer.board.row-1)*fPlayer.turn)][i] == fPlayer.token):
            win = True
    return win
#end endGame

