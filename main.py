from functions import *
from plot_path import *

# User Inputs
game_mode = False  
random_mode = True
input_from_code = False

if game_mode:
    [start_node,goal_node] = startGame()
elif random_mode:
    goal_node = [1,4,7,2,5,8,3,6,0]
    start_node = generate_random()
elif input_from_code:
    # Input the start node and goal node for Code-Input Mode
    start_node = [2,0,7,8,4,6,1,3,5]
    goal_node = [1,8,7,2,0,6,3,4,5]

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
    node_file = open("Nodes.txt","w+")
    info_file = open("NodesInfo.txt","w+")
    for node in path:
        for tile in node:
            path_file.write(str(tile)+" ")
        path_file.write("\n")
    path_file.close()

    for i,node in enumerate(nodes):
        for j,tile in enumerate(node):
            if j != 9:
                node_file.write(str(tile)+" ")
        node_file.write("\n")

        info_file.write(str(i)+" ")
        info_file.write(str(node[9])+" ")
        info_file.write(str(0)+" ")
        info_file.write("\n")
    path_file.close()
    node_file.close()
    info_file.close()

    plot_path()

