#Authors:
#Christopher Lebovitz 
#Dylan Wheeler

#Date: 2019 10 18
#Course: CSC 412 - Introduction to Artificial Intelligence 
#Instructor: Dr. Bo Li


import math

class Node(object):
    def __init__(self, fKey, fState):
        self.heuristic = fKey
        self.state = fState
        self.nextTurns = []     #list of nodes

def maxHeuristic(fNode): 
    max = (0-math.inf)
    for i in range(len(fNode.nextTurns)):
        if fNode.nextTurns[i].heuristic > max:
            max = fNode.nextTurns[i].heuristic
    return max