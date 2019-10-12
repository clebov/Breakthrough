import boardV2
import brainV2
import player

b = 6

print("\n################### Start Breakthrough.py ###################\n")

legalMoves = ['L', 'F', 'R']
offensiveStrategy1 = [player.aboutToWin, player.aboutToLose, player.offensiveHeuristic]
defensiveStrategy1 = [player.aboutToWin, player.aboutToLose, player.defensiveHeuristic]
offensiveStrategy2 = [player.aboutToWin, player.aboutToLose, player.runForward, player.offensiveHeuristic]
defensiveStrategy2 = [player.aboutToWin, player.aboutToLose, player.moveWall, player.defensiveHeuristic]


#Game 1:
#   Minimax Offensive Heuristic 1 VS AlphaBeta Offensive Heuristic 1
game1board = boardV2.board(b, b, "[]", legalMoves)
player1 = player.player("White1", "WW", 0, 1, offensiveStrategy1, False, game1board)
player2 = player.player("Black1", "BB", 1, 1, offensiveStrategy1, True, game1board)

boardV2.runGame(player1, player2, game1board)


#Game 2: (all following games use only AlphaBeta, not Minimax)
#   Offensive Heuristic 2 VS Defensive Heuristic 1
game2board = boardV2.board(b, b, "[]", legalMoves)
player3 = player.player("White2", "WW", 0, 1, offensiveStrategy2, True, game2board)
player4 = player.player("Black2", "BB", 1, 1, defensiveStrategy1, True, game2board)

boardV2.runGame(player3, player4, game2board)


#Game 3:
#   Defensive Heuristic 2 VS Offensive Heuristic 1
game3board = boardV2.board(b, b, "[]", legalMoves)
player5 = player.player("White3", "WW", 0, 1, defensiveStrategy2, True, game3board)
player6 = player.player("Black3", "BB", 1, 1, offensiveStrategy1, True, game3board)

boardV2.runGame(player5, player6, game3board)


#Game 4:
#   Offensive Heuristic 2 VS Offensive Heuristic 1
game4board = boardV2.board(b, b, "[]", legalMoves)
player7 = player.player("White4", "WW", 0, 1, offensiveStrategy2, True, game4board)
player8 = player.player("Black4", "BB", 1, 1, offensiveStrategy1, True, game4board)

boardV2.runGame(player7, player8, game4board)


#Game 5:
#   Defensive Heuristic 2 VS Defensive Heuristic 1
game5board = boardV2.board(b, b, "[]", legalMoves)
player9 = player.player("White5", "WW", 0, 1, defensiveStrategy2, True, game5board)
player10 = player.player("Black5", "BB", 1, 1, defensiveStrategy1, True, game5board)

boardV2.runGame(player9, player10, game5board)


#Game 6:
#   Offensive Heuristic 2 VS Defensive Heuristic 2
game6board = boardV2.board(b, b, "[]", legalMoves)
player11 = player.player("White6", "WW", 0, 1, offensiveStrategy2, True, game6board)
player12 = player.player("Black6", "BB", 1, 1, defensiveStrategy2, True, game6board)

boardV2.runGame(player11, player12, game6board)




