from functions import *

# Data structure for the nodes is a list of lists, each list inside the list 
# nodes is a node. The first 3 elements are the first column, the second 3 
# elements are the second column, and the next 3 are the last column. The last 
# element in the list is the parent node of the node and refers to the index in 
# nodes where it can be found. The starting node has a parent node of -1
nodes = [[]]

start_node = [1,2,3,4,0,5,6,7,8,-1]

nodes[0] = start_node

# [status,new_node] = ActionMoveLeft(nodes[0])
# [status,new_node] = ActionMoveRight(nodes[0])
# [status,new_node] = ActionMoveUp(nodes[0])
# [status,new_node] = ActionMoveDown(nodes[0])

print_matrix(nodes[0])

new_node = [1,2,3,4,0,5,6,7,8,-1]

[nodes,exists] = AddNode(nodes,new_node)

if(exists==False):
    print_matrix(nodes[1])



