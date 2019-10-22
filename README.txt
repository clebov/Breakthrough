Authors:
Christopher Lebovitz
Dylan Wheeler

Date: 2019 10 18
Course: CSC 412 - Introduction to Artificial Intelligence 
Instructor: Dr. Bo Li


How to run this program:


Make sure you have python (Version 3) installed and that you have pygame installed:
    Python: https://www.python.org/downloads/
    pygame: https://www.pygame.org/download.shtml

In Windows, simply navigate to the same folder in which you found this readme and,
    double click Breakthrough.py

Alternatively you may open the same folder in which you found this readme in 
    Visual Studio and run Breakthrough.py with or without the debugger.
    Running without the debugger is recommended as the debugger can 
    greatly slow down computational time. 


In order for Breakthrough.py to function, 
    the following files must be included in the same folder:

        WhitePawn.png
        BlackPawn.png
        Null.png
        Breakthrough.py
        player.py
        boardV2.py
        brainV2.py
        treeV2.py
        display.py

    If any of the above files are missing, Breakthrough.py may not function.



Explaination of heuristics:

    The game will run multiple matchups and 
        display a set os statistics about each round.

    Each player in each matchup may use one of the four following strategies:
        Offensive Strategy 1
        Defensive Strategy 1
        Offensive Strategy 2
        Defensive Strategy 2

    Offensive Strategy 1:
        This strategy gives a higher heuristic rating to board states which 
            have fewer of the opponent's pieces on the board.
        Thus the player will be more likely to select those states and
            attack the opponent.

    Deffensive Strategy 1:
        This strategy gives a higher heuristic rating to board states which
            have more of the player's pieces on the board.
        Thus the player will be more likely to select those states in which
            none of its pieces have been taken.

    Offensive Strategy 2:
        This strategy gives a higher heuristic rating to board states in which 
            the player has moved at least one piece forward one row.
        This causes the player to "run forward" so it can 
            attack the other player or take the home faster.
        It also takes the same heuristics from Offensive Strategy 1 into account.

    Defensive Strategy 2:
        This strategy gives a higher heuristic rating to board states in which
            the player moves more pieces into the row with 
            it's most progressed piece.
        This cuases the player to tend to moving it's pieces along row by row
            to make a "wall" like structure for defending. 
        It also takes the same heuristics from Defensive Strategy 1 into account.
