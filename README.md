# ENPM661-Project1

## 8-Puzzle Solver:

The included code has a solver for the 8-puzzle game. The game is setup as a 3x3 grid
like the one below:

<pre><code>-------------
| 1 | 2 | 3 | 
-------------
| 8 |   | 4 | 
-------------
| 7 | 6 | 5 | 
-------------</code></pre>

Tiles can be moved into the blank space.

The code uses a BFS (Breadth First Search) Algorithm to solve for the necessary path to
reach the goal state from the desired starting state. 


## How to Use the Code

Clone or download the repository. In terminal navigate to the directory and run:
<pre><code>python3 main.py</code></pre>

The default mode is game mode. This will allow the user to input a start configuration 
and goal configuration. If a path exists the code will output the steps to reach the goal.

You can also run the game in random mode. To do this open main.py in a text editor and change
lines 5 and 6 to:
<pre><code>game_mode = False</code></pre>
<pre><code>random_mode = True</code></pre>
Running main.py in this mode will generate a random starting board and find a solution if possible.

## Dependencies 

The code requires the following modules:
<pre><code>numpy</code></pre>
<pre><code>deque from collections</code></pre>
<pre><code>random</code></pre>



