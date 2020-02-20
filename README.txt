# ENPM661-Project1

## 8-Puzzle Solver:

The included code has a solver for the 8-puzzle game. The game is setup as a 3x3 grid
like the one below:

-------------
| 1 | 2 | 3 | 
-------------
| 8 |   | 4 | 
-------------
| 7 | 6 | 5 | 
-------------

Tiles can be moved into the blank space.

The code uses a BFS (Breadth First Search) Algorithm to solve for the necessary path to
reach the goal state from the desired starting state. 


## How to Use the Code

### Game Mode

Clone or download the repository. In terminal navigate to the directory and run:

python3 main.py

The default mode is game mode. This will allow the user to input a start configuration 
and goal configuration. If a path exists the code will output the steps to reach the goal. 

**Please input both the start and goal in column notation**

For the board above the notation would be: 1,8,7,2,0,6,3,4,5

### Random Mode

You can also run the game in random mode. To do this open main.py in a text editor and change
lines 5 and 6 to:

game_mode = False
random_mode = True

Running main.py in this mode will generate a random starting board and find a solution if possible.

### Code-Input Mode

This is the last possible mode. For this mode change lines 5,6 and 7 to:

game_mode = False
random_mode = False
input_from_code = True

This will allow you to input the start node and goal node on lines 16 and 17. Running main.py will print the path to solve your inputed configuration if possible.

## Dependencies 

The code requires the following modules:
numpy
deque from collections
random



