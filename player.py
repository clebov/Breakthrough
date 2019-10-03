#this file defines a player class,
#   players have tokens to represent their piece on the board, 
#   an order in which they take turns
#   a choice of searching for high or low heuristics
#   and a set of strategies that affect their heuristics
#
#this file also contains the methods for a variety of player strategies

import board
import random

class player(object):
    def __init__(self, token, turn, heuristic, strategies, board):
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
def highHeuristic(fPlayer):
    high = random.random()
    for strategy in fPlayer.strategies:
        high += strategy(fPlayer)
    #end for i
    return high






def offensiveHeuristic(fPlayer):
    #set to number of starting pieces on board for a player
    h = (fPlayer.board.col * 2)
    #print(h)
    #subtract for every opponent's piece on the board
    for i in range(fPlayer.board.row):
        for j in range(fPlayer.board.col):
            if (fPlayer.board.field[i][j] == fPlayer.opponent.token):
                h -= fPlayer.heuristic
                #print(fPlayer.board.field[i][j] + " " + str(h))
                #print(h)
    #end for i, j
    #print(str(h)+"\n")
    return h
#end offensive heuristic
