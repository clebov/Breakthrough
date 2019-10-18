#Authors:
#Christopher Lebovitz 
#Dylan Wheeler

#Date: 2019 10 18
#Course: CSC 412 - Introduction to Artificial Intelligence 
#Instructor: Dr. Bo Li


import pygame
from pygame.display import set_mode
from pygame.draw import rect
from pygame.rect import Rect
import pygame.font
import time

BoardWidth = 700
BoardHeight = 450
# color definitions to be used for the board and Winner dispay
light_brown = (251, 196, 117)
black = (0,0,0)
white = (255,255,255)
dark_brown = (139, 69, 0)
colors = [dark_brown, light_brown]

#Output a start screen and display the intent of the program to the user including the matchups for each game
def startScreen():

    pygame.init()

    pygame.display.set_caption('Breakthrough')

    #def screen size
    screen = pygame.display.set_mode((BoardWidth,BoardHeight))
    
    #def font and size
    largeText = pygame.font.Font('freesansbold.ttf',20)

    #create the Rectangle that contains the text to be displayed to the user
    textSurf, textRect = text_objects("Breakthrough!", largeText)
    text2Surf, text2Rect = text_objects("This program will run through several matches in succession:", largeText)
    text3Surf, text3Rect = text_objects("Minimax Offensive Heuristic 1 VS AlphaBeta Offensive Heuristic 1", largeText)
    text4Surf, text4Rect = text_objects("Offensive Heuristic 2 VS Defensive Heuristic 1", largeText)
    text5Surf, text5Rect = text_objects("Defensive Heuristic 2 VS Offensive Heuristic 1", largeText)
    text6Surf, text6Rect = text_objects("Offensive Heuristic 2 VS Offensive Heuristic 1", largeText)
    text7Surf, text7Rect = text_objects("Defensive Heuristic 2 VS Defensive Heuristic 1", largeText)
    text8Surf, text8Rect = text_objects("Offensive Heuristic 2 VS Defensive Heuristic 2", largeText)
    ContinueSurf,ContinueRect=text_objects('Close the Window to continue', largeText)

    #set the location where the Rectangle will be placed on the screen
    textRect.center = ((BoardWidth/2),(BoardHeight/10))
    text2Rect.center = ((BoardWidth/2),(BoardHeight/6))
    text3Rect.center = ((BoardWidth/2),(BoardHeight/3.50))
    text4Rect.center = ((BoardWidth/2),(BoardHeight/2.80))
    text5Rect.center = ((BoardWidth/2),(BoardHeight/2.35))
    text6Rect.center = ((BoardWidth/2),(BoardHeight/2))
    text7Rect.center = ((BoardWidth/2),(BoardHeight/1.75))
    text8Rect.center = ((BoardWidth/2),(BoardHeight/1.55))
    ContinueRect.center = ((BoardWidth/2),(BoardHeight/1.2))
    
    #place the Rectangles with the text
    screen.fill(white)
    screen.blit(textSurf, textRect)
    screen.blit(text2Surf, text2Rect)
    screen.blit(text3Surf, text3Rect)
    screen.blit(text4Surf, text4Rect)
    screen.blit(text5Surf, text5Rect)
    screen.blit(text6Surf, text6Rect)
    screen.blit(text7Surf, text7Rect)
    screen.blit(text8Surf, text8Rect)
    screen.blit(ContinueSurf,ContinueRect)
    
    #update the display 
    pygame.display.update()
    Pause()


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

#output the results of the match to the screen for the user to see with the statistics of the game
def message_display(stats):

    pygame.display.set_caption('Breakthrough')

    #pause the loop to display the final board to the user before showing the result screen 
    time.sleep(4.4)

    # set the size of the result screen
    screen = pygame.display.set_mode((BoardWidth,BoardHeight))

    #fill it with white for the result text to show up
    screen.fill(white)

    #update the display
    pygame.display.update()
    
    
    #def text font and size
    largeText = pygame.font.Font('freesansbold.ttf',20)
   
    #calculate the average amout of nodes expanded and the average time it takes AlphaBeta to run
    avgNodes = round(((stats[3]+ stats[4]) / stats[1]),2)
    avgSeconds = str(round((stats[7]),5))
    
     #create the Rectangle that contains the text to be displayed to the user
    winnerSurf, winnerRect = text_objects('Winner is: ' + stats[0], largeText)
    player1Surf,player1Rect = text_objects('Total number of game tree nodes expanded for White: '+str(stats[3]), largeText)
    player2Surf,player2Rect = text_objects('Total number of games tree nodes expanded for Black:' + str(stats[4]), largeText)
    nodeSurf, nodeRect = text_objects('Average nodes expanded per move: '+ str(avgNodes), largeText)
    timerABSurf, timerABRect = text_objects(('Average run time of AlphaBeta: '+ avgSeconds), largeText)
    p1CaptureSurf,p1CaptureRect =  text_objects('Total number of White pawns captured: '+ str(stats[5]), largeText)
    p2CaptureSurf,p2CaptureRect =  text_objects('Total number of Black pawns captured: '+ str(stats[6]), largeText)
    turnCounterSurf, turnCounterRect = text_objects('Total number of moves made: '+ str(stats[1]), largeText)
    ContinueSurf,ContinueRect=text_objects('Close the Window to continue to the next match', largeText)

    #set the location where the Rectangle will be placed on the screen
    winnerRect.center = ((BoardWidth/2),(BoardHeight/3.90))
    nodeRect.center = ((BoardWidth/2),(BoardHeight/3.30))
    player1Rect.center = ((BoardWidth/2),(BoardHeight/2.80))
    player2Rect.center = ((BoardWidth/2),(BoardHeight/2.40))
    timerABRect.center = ((BoardWidth/2),(BoardHeight/2.10))
    p1CaptureRect.center = ((BoardWidth/2),(BoardHeight/1.85))
    p2CaptureRect.center = ((BoardWidth/2),(BoardHeight/1.65))
    turnCounterRect.center = ((BoardWidth/2),(BoardHeight/1.40))
    ContinueRect.center = ((BoardWidth/2),(BoardHeight/1.2))

    #fill the screen with white so its easy to read the winner and the statistics 
    screen.fill(white)

    #place the Rectangles with the text
    screen.blit(winnerSurf, winnerRect)
    screen.blit(nodeSurf, nodeRect)
    screen.blit(player1Surf,player1Rect)
    screen.blit(player2Surf,player2Rect)
    screen.blit(timerABSurf,timerABRect)
    screen.blit(p1CaptureSurf,p1CaptureRect)
    screen.blit(p2CaptureSurf,p2CaptureRect)
    screen.blit(turnCounterSurf,turnCounterRect)
    screen.blit(ContinueSurf,ContinueRect)

    #update the display to print the winner
    pygame.display.update()
    #wait for user to close the screen before proceeding
    Pause()
    
#wait for user to close the screen before proceeding
def Pause():
    pause = True
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pause = False

#function to show the user what match is being played before the start of the game
def printMatch(text):
    pygame.init()

    pygame.display.set_caption('Breakthrough')

    screen = pygame.display.set_mode((BoardWidth,BoardHeight))
    largeText = pygame.font.Font('freesansbold.ttf',20)
    textSurf, textRect = text_objects(text, largeText)
    textRect.center = ((BoardWidth/2),(BoardHeight/5))
    ContinueSurf,ContinueRect=text_objects('Close the Window to continue', largeText)
    ContinueRect.center = ((BoardWidth/2),(BoardHeight/2))
    screen.fill(white)
    screen.blit(textSurf, textRect)
    screen.blit(ContinueSurf,ContinueRect)
    pygame.display.update()
    Pause()

def quit():
    #look for an event fromt he user
    ev = pygame.event.poll()
    if ev.type == pygame.QUIT: #check if the user has selected the close button
        pygame.quit()

def draw_board(the_board):
    """ Draw a chess board with pawns, as determined by the the_board. """
   
    pygame.init()

    #set the caption for the window to Breakthrough
    pygame.display.set_caption('Breakthrough')
    colors = [light_brown, dark_brown]    # Set up colors [light_brown, dark_brown]

    """
    n = len(the_board.field)         # This is an NxN chess board.
    surface_sz = 480           # Proposed physical surface size.
    sq_sz = surface_sz // n    # sq_sz is length of a square.
    surface_sz = n * sq_sz     # Adjust to exactly fit n squares.
    """
    # Look for an event from keyboard, mouse, etc.
   
    n = the_board.col         # This is an NxM chess board.
    surface_sz = 100*the_board.col           # Proposed physical surface size.
    sq_sz = surface_sz // n    # sq_sz is length of a square.
    surface_sz = n * sq_sz     # Adjust to exactly fit n squares.

    m = the_board.row         # This is an NxM chess board.
    surface_sy = 100*the_board.row           # Proposed physical surface size.
    sq_sy = surface_sy // m    # sq_sz is length of a square.
    surface_sy = m * sq_sy     # Adjust to exactly fit n squares.


    # Create the surface of (width, height), and its window.
    surface = pygame.display.set_mode((surface_sz, surface_sy))  
        
    # Draw a fresh background (a blank chess board)
    for row in range(the_board.row):           # Draw each row of the board.
        c_indx = row % 2           # Alternate starting color
        for col in range(the_board.col):       # Run through cols drawing squares
            the_square = (col*sq_sz, row*sq_sy, sq_sz, sq_sy)
            surface.fill(colors[c_indx], the_square)
            # Now flip the color index for the next square
            c_indx = (c_indx + 1) % 2

    # Now that squares are drawn, draw the pawns.
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
                (col*sq_sz+Pawn_offset,row*sq_sy+Pawn_offset))
    
    pygame.display.update()