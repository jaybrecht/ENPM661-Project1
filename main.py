from functions import *
from plot_path import *

# User Inputs
game_mode = True
random_mode = False

if game_mode:
    [start_node,goal_node] = startGame()
elif random_mode:
    goal_node = [1,8,7,2,0,6,3,4,5]
    start_node = generate_random()


[nodes,success] = BFS(start_node,goal_node)

if not success:
    print("\nThe goal configuration cannot be reached.")
    print("Please try a different configuration\n")

else:
    path = generate_path(nodes)

    path_file = open("nodePath.txt","w+")
    for node in path:
        for tile in node:
            path_file.write(str(tile)+" ")
        path_file.write("\n")
    path_file.close()

    plot_path()

