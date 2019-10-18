#Authors:
#Christopher Lebovitz 
#Dylan Wheeler

#Date: 2019 10 18
#Course: CSC 412 - Introduction to Artificial Intelligence 
#Instructor: Dr. Bo Li


import player
import boardV2
import brainV2
import display

#size of board to make a nxn board.
b = 8

print("\n################### Start Breakthrough.py ###################\n")

#per the rules of breakthrough, a player may move left, forward, or right
legalMoves = ['L', 'F', 'R']

#define strategies based off which heuristic scores they consider
offensiveStrategy1 = [player.aboutToWin, player.aboutToLose, player.offensiveHeuristic]
defensiveStrategy1 = [player.aboutToWin, player.aboutToLose, player.defensiveHeuristic]
offensiveStrategy2 = [player.aboutToWin, player.aboutToLose, player.runForward, player.offensiveHeuristic]
defensiveStrategy2 = [player.aboutToWin, player.aboutToLose, player.moveWall, player.defensiveHeuristic]


display.startScreen()


#Game 1
match ="Minimax Offensive Heuristic 1 VS AlphaBeta Offensive Heuristic 1"
game1board = boardV2.board(b, b, "[]", legalMoves)
player1 = player.player("White", "WW", 0, 1, offensiveStrategy1, False, game1board)
player2 = player.player("Black", "BB", 1, 1, offensiveStrategy1, True, game1board)
boardV2.runGame(player1, player2, game1board,match)


#Game 2: (all following games use only AlphaBeta, not Minimax)
match="Offensive Heuristic 2 VS Defensive Heuristic 1"
game2board = boardV2.board(b, b, "[]", legalMoves)
player3 = player.player("White", "WW", 0, 1, offensiveStrategy2, True, game2board)
player4 = player.player("Black", "BB", 1, 1, defensiveStrategy1, True, game2board)

boardV2.runGame(player3, player4, game2board,match)


#Game 3:
match="Defensive Heuristic 2 VS Offensive Heuristic 1"
game3board = boardV2.board(b, b, "[]", legalMoves)
player5 = player.player("White", "WW", 0, 1, defensiveStrategy2, True, game3board)
player6 = player.player("Black", "BB", 1, 1, offensiveStrategy1, True, game3board)

boardV2.runGame(player5, player6, game3board,match)


#Game 4:
match="Offensive Heuristic 2 VS Offensive Heuristic 1"
game4board = boardV2.board(b, b, "[]", legalMoves)
player7 = player.player("White", "WW", 0, 1, offensiveStrategy2, True, game4board)
player8 = player.player("Black", "BB", 1, 1, offensiveStrategy1, True, game4board)

boardV2.runGame(player7, player8, game4board,match)


#Game 5:
match = "Defensive Heuristic 2 VS Defensive Heuristic 1"
game5board = boardV2.board(b, b, "[]", legalMoves)
player9 = player.player("White", "WW", 0, 1, defensiveStrategy2, True, game5board)
player10 = player.player("Black", "BB", 1, 1, defensiveStrategy1, True, game5board)

boardV2.runGame(player9, player10, game5board,match)


#Game 6:
match = "Offensive Heuristic 2 VS Defensive Heuristic 2"
game6board = boardV2.board(b, b, "[]", legalMoves)
player11 = player.player("White", "WW", 0, 1, offensiveStrategy2, True, game6board)
player12 = player.player("Black", "BB", 1, 1, defensiveStrategy2, True, game6board)

boardV2.runGame(player11, player12, game6board,match)


#Game 7:
match = "Offensive Heuristic 2 VS Defensive Heuristic 2, oblong board"
game7board = boardV2.board(5, 10, "[]", legalMoves)
player13 = player.player("White", "WW", 0, 1, offensiveStrategy2, True, game7board)
player14 = player.player("Black", "BB", 1, 1, defensiveStrategy2, True, game7board)

boardV2.runGame(player13, player14, game7board,match)

