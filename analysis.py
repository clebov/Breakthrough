#Authors:
#Christopher Lebovitz 
#Dylan Wheeler

#Date: 2019 10 18
#Course: CSC 412 - Introduction to Artificial Intelligence 
#Instructor: Dr. Bo Li


import player
import boardV2
import brainV2

import copy

#size of board to make a bxb board.
b = 8

#number of games for each loop
numGames = 99

#initialize list to record cumulative game statistics to report averages
#   0: the turn counter
#   1: offensive player total nodes 
#   2: defensive player total nodes
#   3: offensive player workers captured 
#   4: defensive player workers captured
#   5: average runtime for AlphaBeta
gameStats = [0, 0, 0, 0, 0, 0.0] 
offWins = 0
defWins = 0
fileName = "Analysis.txt"

def writeGameStats(fGameStats, fOffWins, fDefWins, fMatch, fFileName):
    #open file
    file = open(fFileName, "a")

    file.write("Reporting data for " + fMatch + "\n") 
    global numGames
    file.write("Games analyzed: " + str(numGames) + "\n") 
    file.write("Average Number of Turns: " + str(fGameStats[0]) + "\n")
    file.write("Average Offensive Player Nodes Expanded: " + str(fGameStats[1]) + "\n")
    file.write("Average Defensive Player Nodes Expanded: " + str(fGameStats[2]) + "\n")
    file.write("Average Offensive Player Workers Captured: " + str(fGameStats[3]) + "\n")
    file.write("Average Defensive Player Workers Captured: " + str(fGameStats[4]) + "\n")
    file.write("Average Runtime of Alphabeta: " + str(fGameStats[5]) + "\n")
    file.write("Times Offensive Player Won: " + str(fOffWins) + "\n")
    file.write("Times Defensive Player Won: " + str(fDefWins) + "\n")
    file.write("\n\n")

def printGameStats(fGameStats, fOffWins, fDefWins, fMatch):

    print("Reporting data for " + fMatch) 
    global numGames
    print("Games analyzed: " + str(numGames)) 
    print("Average Number of Turns: " + str(fGameStats[0]))
    print("Average Offensive Player Nodes Expanded: " + str(fGameStats[1]))
    print("Average Defensive Player Nodes Expanded: " + str(fGameStats[2]))
    print("Average Offensive Player Workers Captured: " + str(fGameStats[3]))
    print("Average Defensive Player Workers Captured: " + str(fGameStats[4]))
    print("Average Runtime of Alphabeta: " + str(fGameStats[5]))
    print("Times Offensive Player Won: " + str(fOffWins))
    print("Times Defensive Player Won: " + str(fDefWins))
    print("\n")



print("\n################### Start analysis.py ###################\n")

#per the rules of breakthrough, a player may move left, forward, or right
legalMoves = ['L', 'F', 'R']

#define strategies based off which heuristic scores they consider
offensiveStrategy1 = [player.aboutToWin, player.aboutToLose, player.offensiveHeuristic]
defensiveStrategy1 = [player.aboutToWin, player.aboutToLose, player.defensiveHeuristic]
offensiveStrategy2 = [player.aboutToWin, player.aboutToLose, player.runForward, player.offensiveHeuristic]
defensiveStrategy2 = [player.aboutToWin, player.aboutToLose, player.moveWall, player.defensiveHeuristic]
comprehensiveStrategy = [player.aboutToWin, player.aboutToLose, player.runForward, player.offensiveHeuristic, player.moveWall, player.defensiveHeuristic]




#match 1
match = "Offensive 1 vs Defensive 1"

for i in range(numGames):
    print("Game: " + str(i)) 
    gameBoard = boardV2.board(b, b, "[]", legalMoves)
    player1 = player.player("White", "WW", 0, 1, offensiveStrategy1, True, gameBoard)
    player2 = player.player("Black", "BB", 1, 1, defensiveStrategy1, True, gameBoard)

    thisGame = boardV2.runGame(player1, player2, gameBoard, match, False)

    if(thisGame[0] == 'White'):
        offWins += 1
    else:
        defWins += 1

    gameStats[0] += int(thisGame[1])
    gameStats[1] += int(thisGame[3])
    gameStats[2] += int(thisGame[4])
    gameStats[3] += int(thisGame[5])
    gameStats[4] += int(thisGame[6])
    gameStats[5] += int(thisGame[7])

#end for i numGames

#find averages
for i in range(len(gameStats)):
    gameStats[i] /= numGames

printGameStats(gameStats, offWins, defWins, match)
writeGameStats(gameStats, offWins, defWins, match, fileName)

#reset trackers
gameStats = [0, 0, 0, 0, 0, 0.0] 
offWins = 0
defWins = 0

#end match 1




#match 2 
match = "Offensive 2 vs Defensive 1"

for i in range(numGames):
    print("Game: " + str(i)) 
    gameBoard = boardV2.board(b, b, "[]", legalMoves)
    player1 = player.player("White", "WW", 0, 1, offensiveStrategy2, True, gameBoard)
    player2 = player.player("Black", "BB", 1, 1, defensiveStrategy1, True, gameBoard)

    thisGame = boardV2.runGame(player1, player2, gameBoard, match, False)

    if(thisGame[0] == 'White'):
        offWins += 1
    else:
        defWins += 1

    gameStats[0] += int(thisGame[1])
    gameStats[1] += int(thisGame[3])
    gameStats[2] += int(thisGame[4])
    gameStats[3] += int(thisGame[5])
    gameStats[4] += int(thisGame[6])
    gameStats[5] += int(thisGame[7])

#end for i numGames

#find averages
for i in range(len(gameStats)):
    gameStats[i] /= numGames

printGameStats(gameStats, offWins, defWins, match)
writeGameStats(gameStats, offWins, defWins, match, fileName)

#reset trackers
gameStats = [0, 0, 0, 0, 0, 0.0] 
offWins = 0
defWins = 0

#end match 2




#match 3
match = "Offensive 1 vs Defensive 2"

for i in range(numGames):
    print("Game: " + str(i)) 
    gameBoard = boardV2.board(b, b, "[]", legalMoves)
    player1 = player.player("White", "WW", 0, 1, offensiveStrategy1, True, gameBoard)
    player2 = player.player("Black", "BB", 1, 1, defensiveStrategy2, True, gameBoard)

    thisGame = boardV2.runGame(player1, player2, gameBoard, match, False)

    if(thisGame[0] == 'White'):
        offWins += 1
    else:
        defWins += 1

    gameStats[0] += int(thisGame[1])
    gameStats[1] += int(thisGame[3])
    gameStats[2] += int(thisGame[4])
    gameStats[3] += int(thisGame[5])
    gameStats[4] += int(thisGame[6])
    gameStats[5] += int(thisGame[7])

#end for i numGames

#find averages
for i in range(len(gameStats)):
    gameStats[i] /= numGames

printGameStats(gameStats, offWins, defWins, match)
writeGameStats(gameStats, offWins, defWins, match, fileName)

#reset trackers
gameStats = [0, 0, 0, 0, 0, 0.0] 
offWins = 0
defWins = 0

#end match 3




#match 4
match = "Offensive 2 vs Defensive 2"

for i in range(numGames):
    print("Game: " + str(i)) 
    gameBoard = boardV2.board(b, b, "[]", legalMoves)
    player1 = player.player("White", "WW", 0, 1, offensiveStrategy2, True, gameBoard)
    player2 = player.player("Black", "BB", 1, 1, defensiveStrategy2, True, gameBoard)

    thisGame = boardV2.runGame(player1, player2, gameBoard, match, False)

    if(thisGame[0] == 'White'):
        offWins += 1
    else:
        defWins += 1

    gameStats[0] += int(thisGame[1])
    gameStats[1] += int(thisGame[3])
    gameStats[2] += int(thisGame[4])
    gameStats[3] += int(thisGame[5])
    gameStats[4] += int(thisGame[6])
    gameStats[5] += int(thisGame[7])

#end for i numGames

#find averages
for i in range(len(gameStats)):
    gameStats[i] /= numGames

printGameStats(gameStats, offWins, defWins, match)
writeGameStats(gameStats, offWins, defWins, match, fileName)

#reset trackers
gameStats = [0, 0, 0, 0, 0, 0.0] 
offWins = 0
defWins = 0

#end match 4




#match 5
match = "All Heuristics for both players"

for i in range(numGames):
    print("Game: " + str(i)) 
    gameBoard = boardV2.board(b, b, "[]", legalMoves)
    player1 = player.player("White", "WW", 0, 1, comprehensiveStrategy, True, gameBoard)
    player2 = player.player("Black", "BB", 1, 1, comprehensiveStrategy, True, gameBoard)

    thisGame = boardV2.runGame(player1, player2, gameBoard, match, False)

    if(thisGame[0] == 'White'):
        offWins += 1
    else:
        defWins += 1

    gameStats[0] += int(thisGame[1])
    gameStats[1] += int(thisGame[3])
    gameStats[2] += int(thisGame[4])
    gameStats[3] += int(thisGame[5])
    gameStats[4] += int(thisGame[6])
    gameStats[5] += int(thisGame[7])

#end for i numGames

#find averages
for i in range(len(gameStats)):
    gameStats[i] /= numGames

printGameStats(gameStats, offWins, defWins, match)
writeGameStats(gameStats, offWins, defWins, match, fileName)

#reset trackers
gameStats = [0, 0, 0, 0, 0, 0.0] 
offWins = 0
defWins = 0

#end match 5




print("\n################### End analysis.py ###################\n")
