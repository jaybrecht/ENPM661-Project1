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
    print("\nThe goal configuration: ")
    print_matrix(goal_node)
    print("can not be reached for the starting board:")
    print_matrix(start_node[0:9])
    print("The program searched",str(len(nodes)), "nodes")
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

