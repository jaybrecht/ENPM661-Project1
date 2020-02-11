from functions import *
from collections import deque

# Data structure for the nodes is a list of lists, each list inside the list 
# nodes is a node. The first 3 elements are the first column, the second 3 
# elements are the second column, and the next 3 are the last column. The last 
# element in the list is the parent node of the node and refers to the index in 
# nodes where it can be found. The starting node has a parent node of -1

nodes = [[]]

start_node = [8,4,2,3,1,7,5,6,0]
goal_node = [5,4,3,6,0,2,7,8,1]

node_set = {tuple(start_node)}

start_node.append(-1)
nodes[0] = start_node

queue = deque()
queue.append(0)

isgoal = False
neighbors = ['right','left','up','down'] #modify order to change the order of search
while queue:
    cur_node = nodes[queue.popleft()]
    parent = nodes.index(cur_node)
    for direction in neighbors:
        [status,new_node] = check_neighbors(cur_node,direction)
        if status == True:
            new_node[9] = parent
            [nodes,node_set,exists] = AddNode(new_node,nodes,node_set)
            if not exists:            
                queue.append(len(nodes))
        if new_node[0:9] == goal_node:
            isgoal = True
            break
    if isgoal:
        break

path = generate_path(nodes)
for node in path:
    print_matrix(node)

print("The goal state can be achieved with ",len(path)-1, " steps.")

