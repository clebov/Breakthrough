Breakthrough is an abstract strategy board game invented by Dan Troyka in 2000 and made available as a Zillions of Games file (ZRF). It won the 2001 8x8 Game Design Competition, 
even though the game was originally played on a 7x7 board, as it is trivially extensible to larger board sizes.

The 8x8 board is initially set up as shown below. Each player has 16 workers in their team.]

Choose a player to go first; then play alternates, with each player moving one piece per turn.

In each turn, a worker can only move one square in the forward or diagonally-forward directions, Moreover, 
a worker can 'capture' workers of the enemy team if they are placed diagonally forward from it.
if enemy workers are directly in front of the player, then a capture isn't possible.

A piece may move into a square containing an opponent's piece if and only if that square is one step diagonally forward. The opponent's piece is removed and the player's piece replaces it. 
Note that capturing is not compulsory, nor is it "chained" as in checkers.

The first player to reach the opponent's home row — the one farthest from the player — is the winner.
[1] If all the pieces of a player are captured, that player loses. A draw is impossible
[2] because pieces can only move ahead (or be captured), and the piece closest to the opponent's home row always has at least one forward diagonal move available.

Minimax and Alpha-Beta agents:

Our task is to implement agents to play the above game, one using minimax search and one using alpha-beta search as well as two evaluation functions - one which is more offensive 
(i.e., more focused on moving forward and capturing enemy pieces), 
while the other which is more defensive (i.e., more focused on preventing the enemy from moving into your territory or capturing your pieces). 
The evaluation functions are used to return a value for a position when the depth limit of the search is reached. Try to determine the maximum depth to which it is feasible for you to do the search (for alpha-beta pruning, this depth should be larger than for minimax). 
The worst-case number of leaf nodes for a tree with a depth of three in this game is roughly 110,592, but in practice is usually between 25,000 - 35,000. Thus, you should at least be able to do minimax search to a depth of three

We provide the following two dummy heuristics: 
    • Defensive Heuristic 1: The more pieces you have remaining, the higher your value is. The value will be computed according to the formula 2*(number_of_own_pieces_remaining) + random(). 
    • Offensive Heuristic 1: The more pieces your opponent has remaining, the lower your value is. The value will be computed according to the formula 2*(30 - number_of_opponent_pieces_remaining) + random(). 
            NOTE: random() generates a random float uniformly in the semi-open range [0.0, 1.0) as per Python's random(). This noise is added to provide an easy way to break ties. 

Our task for this part is: 
    • Implement minimax search for a search tree depth of 3. 
    • Implement alpha-beta search for a search tree of depth more than that of minimax. 
    • Implement Defensive Heuristic 1 and Offensive Heuristic 1. 
    • Design and implement an Offensive Heuristic 2 with the idea of beating Defensive Heuristic 1.
    • Design and implement a Defensive Heuristic 2 with the idea of beating Offensive Heuristic 1. 

Then play the following matchups: 
    1. Minimax (Offensive Heuristic 1) vs Alpha-beta (Offensive Heuristic 1) 
    2. Alpha-beta (Offensive Heuristic 2) vs Alpha-beta (Defensive Heuristic 1) 
    3. Alpha-beta (Defensive Heuristic 2) vs Alpha-beta (Offensive Heuristic 1) 
    4. Alpha-beta (Offensive Heuristic 2) vs Alpha-beta (Offensive Heuristic 1) 
    5. Alpha-beta (Defensive Heuristic 2) vs Alpha-beta (Defensive Heuristic 1) 
    6. Alpha-beta (Offensive Heuristic 2) vs Alpha-beta (Defensive Heuristic 2)

For each of the above matchups, report the following: 
    A. The final state of the board (who owns each square) and the winning player. 
    B. The total number of game tree nodes expanded by each player in the course of the game. 
    C. The average number of nodes expanded per move and the average amount of time to make a move. 
    D. The number of opponent workers captured by each player, as well as the total number of moves required till the win. 

If we have time, try to run each matchup multiple times to determine whether the noise in the evaluation function has any effect on the final outcome. 
Finally, you should summarize any general trends or conclusions that you have observed.
    How does the type of evaluation function (offensive vs. defensive) affect the outcome? 
    How do different combinations of evaluation functions do against each other?




