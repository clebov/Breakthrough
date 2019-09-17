#this file contains methods to create, populate, and print a board

#size of board, number of squares on each side and initialize  the board with [] to represent squares
def createBoard(fBoard):
  row, col = (8,8)
  Board =[['[]' for i in range(col)]for j in range(row)]

  for row in Board:
      print(*row) 



