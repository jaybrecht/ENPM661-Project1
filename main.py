from functions import *
from plot_path import *

game_mode = True

if game_mode:
    [start_node,goal_node] = startGame()
else:
    # Possible Case
    # start_node = [8,4,2,3,1,7,5,6,0]
    # goal_node = [5,4,3,6,0,2,7,8,1]

    # Impossible Case
    start_node = [8,0,7,1,4,6,2,3,5]
    goal_node = [1,4,7,2,5,8,3,6,0]

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

