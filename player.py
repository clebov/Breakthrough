#this file defines a player class,
#   players have tokens to represent their piece on the board, 
#   an order in which they take turns
#   a choice of searching for high or low heuristics
#   and a set of strategies that affect their heuristics
#
#this file also contains the methods for a variety of player strategies

import board
import random
import brainV2


#break ties between equivalent high heuristics using random number generation
randomTiebreakers = True


class player(object):
    def __init__(self, name, token, turn, heuristic, strategies, board):
        #name of player
        #   usually "White" or "Black"
        self.name = name
        
        #token should be a two character string 
        #   meant to represent a player's piece on a  board
        self.token = token

        #turn should be 0 or 1,
        #   0 means the player goes first
        #   1 means the player goes second
        self.turn = turn

        #a player may search for a high hueristic or a low heuristic,
        #   heuristic should be 1 or -1
        #   1 means the player is searching for a high heuristic
        #   -1 means the player is searching for a low heuristic
        self.heuristic = heuristic

        #strategies is a list of low level heuristic functions
        #   high level heuristics should return the sum of heuristics in 
        #   strategies for a given player
        self.strategies = strategies

        #board is the board that the player is placed on
        self.board = board

        #player has an opponent, set in setOpponents
        self.opponent = None
    #end init
#end player


#print player
def printPlayer(fPlayer):
    print("Token: " + fPlayer.token)
    print("Turn order: " + str(fPlayer.turn))
    print("Heuristic: " + str(fPlayer.heuristic))
    print("Strategies: " + str(fPlayer.strategies))
    print("Board: " + str(fPlayer.board))
#end print player


#set opponents
def setOpponents(fPlayer01, fPlayer02):
    fPlayer01.opponent = fPlayer02
    fPlayer02.opponent = fPlayer01 
#end set opponents


#high level heuristic
def highHeuristic(fPlayer, fState):
    high = 0
    global randomTiebreakers
    if randomTiebreakers:
        high += (random.random()/100)
    for strategy in fPlayer.strategies:
        high += strategy(fPlayer, fState)
    #end for strategies
    return high
#end high level heuristic


#weighted highHeuristic
def weightedHighHeuristic(fPlayer, fState):
    high = 0

    global randomTiebreakers
    if randomTiebreakers:
        high += (random.random()/100)

    i = 0.0
    for strategy in fPlayer.strategies:
        high += strategy(fPlayer, fState)*(i*.9)
        i += 1.0
    #end for strategies

    #print("\n"+str(high)+"\n\n")
    return high
#end wighted high heuristic


#offensive heuristic
#   gives higher score to a board state that has 
#   fewer of the opponent's pieces
def offensiveHeuristic(fPlayer, fState):
    #set to number of starting pieces on board for a player
    h = (fPlayer.board.col * 2)
    #print(h)
    #subtract for every opponent's piece on the board
    for i in range(fPlayer.board.row):
        for j in range(fPlayer.board.col):
            if (fState[i][j] == fPlayer.opponent.token):
                h -= fPlayer.heuristic

    #end for i, j
    return (h/(fPlayer.board.col * 2))
#end offensive heuristic


#defensive heuristic
#   gives higher score to a board state that has
#   more of the player's pieces
def defensiveHeuristic(fPlayer, fState):
    h = 0
    #count the number of player's pieces on board
    for i in range(fPlayer.board.row):
        for j in range(fPlayer.board.col):
            if (fState[i][j] == fPlayer.token):
                h += fPlayer.heuristic
    
    #end for i, j
    return (h/(fPlayer.board.col * 2))
#end defensive heuristic


#aboutToWin heuristic
#   gives higher score to board states where
#   the player is one move away from winning
def aboutToWin(fPlayer, fState):
    h = 0
    if brainV2.endGame(fState, fPlayer):
        h += 1*fPlayer.heuristic
    return h
#end about to win


#about to loose heuristic
#   gives a lower score to board states where
#   the player is about to lose
def aboutToLose(fPlayer, fState):
    h = 0
    if brainV2.endGame(fState, fPlayer.opponent):
        h -= 1*fPlayer.heuristic
    return h
#end about to lose


#offensive heuristic 2
#   gives a higher score when the player has pieces closer to the end
def runForward(fPlayer, fState):
    h = fPlayer.board.row

    direction = (2*fPlayer.turn)-1

    endRow = ((fPlayer.board.row-1)*fPlayer.turn)
    if(endRow == 0):
        startRow = fPlayer.board.row-1
    else:
        startRow = 0

    foundPiece = False

    while endRow != startRow:
        for i in range(fPlayer.board.col):
            if fState[endRow][i] == fPlayer.token:
                foundPiece = True
                break
        if foundPiece:
            break
        else:
            h -= 1
        endRow -= direction
    #end while

    return (h/fPlayer.board.row)

#end run forward


#defensive heuristic 2
#   gives higher score to board states in which the player 
#   moves its pieces forward in unison, like a wall
def moveWall(fPlayer, fState):
    return .5
#end moveWall