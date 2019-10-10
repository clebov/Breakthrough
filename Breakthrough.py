import boardV2
import brainV2
import player


print("\n################### Start Breakthrough.py ###################\n")

legalMoves = ['L', 'F', 'R']
offensiveStrategy1 = [player.aboutToWin, player.aboutToLose, player.offensiveHeuristic]
defensiveStrategy1 = [player.aboutToWin, player.aboutToLose, player.defensiveHeuristic]


#Game 1:
#   Minimax Offensive Heuristic 1 VS AlphaBeta Offensive Heuristic 1
game1board = boardV2.board(5, 5, "[]", legalMoves)
player1 = player.player("White", "WW", 0, 1, offensiveStrategy1, False, game1board)
player2 = player.player("Black", "BB", 1, 1, offensiveStrategy1, True, game1board)

boardV2.runGame(player1, player2, game1board)



#Game 2: (all following games use only AlphaBeta, not Minimax)
#   Offensive Heuristic 2 VS Defensive Heuristic 1




#Game 3:
#   Defensive Heuristic 2 VS Offensive Heuristic 1




#Game 4:
#   Offensive Heuristic 2 VS Offensive Heuristic 1




#Game 5:
#   Defensive Heuristic 2 VS Defensive Heuristic 1




#Game 6:
#   Offensive Heuristic 2 VS Defensive Heuristic 2





