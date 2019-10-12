#testing file to run as main to check external funtions
import board
import player
import brain
import brainV2
import tree

print("\n################### Start testing.py ###################\n")

test05 = board.board(8, 8, '_', {'L', 'F', 'R'})

player01 = player.player('W', 0, 1, {player.aboutToWin, player.offensiveHeuristic, player.runForward}, test05)
player02 = player.player('B', 1, 1, {player.defensiveHeuristic, player.aboutToLose}, test05)
player.setOpponents(player01, player02)
board.setStartingPieces(player01)
board.setStartingPieces(player02)

board.placePiece(test05.field, 1, 4, player01.token)
#board.placePiece(test05.field, 2, 3, board.whiteToken)
#board.placePiece(test05.field, 2, 3, board.whiteToken)

board.printBoard(test05.field)

print(player.runForward(player01, test05.field))
print()
print(player.runForward(player02, test05.field))



#ignore this comment
#   ignore this comment too
























print("\n################### End testing.py ###################\n")


"""







test03 = board.board(4, 2, '_', {'L', 'F', 'R'})

player01 = player.player('W', 1, 1, {player.offensiveHeuristic}, test03)
player02 = player.player('B', 0, 1, {player.offensiveHeuristic}, test03)
player.setOpponents(player01, player02)
board.setStartingPieces(player01)
board.setStartingPieces(player02)


board.printBoard(test03.field)
print(player01)
player.printPlayer(player01)
print("\n\n" + str(player.highHeuristic(player01)))


currentState = tree.Node(0, player01.board.field)
currentState.nextTurns = brainV2.getPossibleStates(player02, currentState, 0, 0)
brain.minimax(currentState, 0, 0)
tree.printTree(currentState)
test1 = board.createBoard()
board.setStartingPieces(test1)
board.printBoard(test1)

currentState = tree.Node(0, test1)
currentState.nextTurns = brain.getPossibleStates(currentState, 0, 0)

print("\n################### Printing Next States Tree ###################\n")
brain.minimax(currentState, 0, 0)
tree.writeTree(currentState)







##### testing 10/02/2019
class player(object):
  def __init__(self, token, turn, strategy):
    self.token=token
    self.turn= turn
    self.strategy= strategy


print("__________")
progressedBoard = board.createBoard()
board.placePiece(progressedBoard, 2, 3, board.whiteToken)
board.placePiece(progressedBoard, 5, 4, board.whiteToken)
board.placePiece(progressedBoard, 2, 7, board.whiteToken)
board.placePiece(progressedBoard, 3, 3, board.whiteToken)
board.placePiece(progressedBoard, 7, 1, board.whiteToken)
board.placePiece(progressedBoard, 1, 0, board.whiteToken)
board.placePiece(progressedBoard, 6, 6, board.blackToken)
board.placePiece(progressedBoard, 4, 4, board.blackToken)
board.placePiece(progressedBoard, 2, 0, board.blackToken)

#brain.getHeuristic(progressedBoard)
board.printBoard(progressedBoard)

next02 = tree.Node(0, progressedBoard)
next02.nextTurns = brain.getPossibleStates(next02, 0, 1)
tree.printTree(next02)

#print(test1)
"""
