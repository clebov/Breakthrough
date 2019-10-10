##TODO:
#make the size of the board dynamic
#show a pop-up winner anouncing the winner of the game and how many pieces captured


import math
import board
import pygame
from pygame.display import set_mode
from pygame.draw import rect
from pygame.rect import Rect
import board


def quit():
    #look for an event fromt he user
    ev = pygame.event.poll()
    if ev.type == pygame.QUIT: #check if the user has selected the close button
        pygame.quit()

        

squareCenters = []
BoardWidth = 640
BoardHeight = 640
screen = pygame.display.set_mode((900,700))
light_brown = (251, 196, 117)
gray = (100, 100, 100)
violet = (238, 130, 238)
dark_brown = (139, 69, 0)
colors = [dark_brown, light_brown]

def draw_board(the_board):
    """ Draw a chess board with queens, as determined by the the_board. """

    pygame.init()
    #set the caption for the window to Breakthrough
    pygame.display.set_caption('Breakthrough')
    colors = [light_brown, dark_brown]    # Set up colors [red,]

    n = len(the_board.field)         # This is an NxN chess board.
    surface_sz = 480           # Proposed physical surface size.
    sq_sz = surface_sz // n    # sq_sz is length of a square.
    surface_sz = n * sq_sz     # Adjust to exactly fit n squares.

    # Look for an event from keyboard, mouse, etc.
   
    # Create the surface of (width, height), and its window.
    surface = pygame.display.set_mode((surface_sz, surface_sz))  
        
    # Draw a fresh background (a blank chess board)
    for row in range(the_board.row):           # Draw each row of the board.
        c_indx = row % 2           # Alternate starting color
        for col in range(the_board.col):       # Run through cols drawing squares
            the_square = (col*sq_sz, row*sq_sz, sq_sz, sq_sz)
            surface.fill(colors[c_indx], the_square)
            # Now flip the color index for the next square
            c_indx = (c_indx + 1) % 2

    # Now that squares are drawn, draw the queens.
    for row in range (the_board.row):
        for col in range(the_board.col):
            if the_board.field[row][col] == 'BB':
                Pawn = pygame.image.load("BlackPawn.png")
            if the_board.field[row][col] == 'WW':
                Pawn = pygame.image.load("WhitePawn.png")
            if the_board.field[row][col] == '[]':
                Pawn = pygame.image.load("Null.png")
            Pawn_offset = (sq_sz-Pawn.get_width()) // 2
            surface.blit(Pawn,
                (col*sq_sz+Pawn_offset,row*sq_sz+Pawn_offset))

    pygame.display.update()