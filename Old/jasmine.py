import player
import boardV2
import brainV2
import display

b = 8

print("\n################### Start Jasmine.py ###################\n")

legalMoves = ['L', 'F', 'R']
offensiveStrategy1 = [player.aboutToWin, player.aboutToLose, player.offensiveHeuristic]
defensiveStrategy1 = [player.aboutToWin, player.aboutToLose, player.defensiveHeuristic]
offensiveStrategy2 = [player.aboutToWin, player.aboutToLose, player.runForward, player.offensiveHeuristic]
defensiveStrategy2 = [player.aboutToWin, player.aboutToLose, player.moveWall, player.defensiveHeuristic]

display.startScreen()


#Game 1
match ="Minimax Offensive Heuristic 1 VS AlphaBeta Offensive Heuristic 1"
game1board = boardV2.board(8, 3, "[]", legalMoves)
player1 = player.player("White", "WW", 0, 1, offensiveStrategy1, False, game1board)
player2 = player.player("Black", "BB", 1, 1, offensiveStrategy1, True, game1board)
print(boardV2.runGame(player1, player2, game1board,match))