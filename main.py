from functions import *

# Data structure for the nodes is a list of lists, each list inside the list 
# nodes is a node. The first 3 elements are the first column, the second 3 
# elements are the second column, and the next 3 are the last column. The last 
# element in the list is the parent node of the node and refers to the index in 
# nodes where it can be found. The starting node has a parent node of -1

nodes = [[]]

start_node = [8,2,3,6,5,0,7,4,1]
goal_node = [1,4,7,2,5,8,3,6,0]

node_set = {tuple(start_node)}

start_node.append(-1)
nodes[0] = start_node

queue = [nodes[0]]

isgoal = False

while not isgoal:
    cur_node = queue[0].copy()
    parent = nodes.index(cur_node)
    neighbors = ['L','R','U','D']
    for ind,direction in enumerate(neighbors):
        if direction == 'L':
            [status,new_node] = ActionMoveLeft(cur_node)
        if direction == 'R':
            [status,new_node] = ActionMoveRight(cur_node)
        if direction == 'U':
            [status,new_node] = ActionMoveUp(cur_node)
        if direction == 'D':
            [status,new_node] = ActionMoveDown(cur_node)
        if status == True:
            new_node[9] = parent
            [nodes,node_set,exists] = AddNode(new_node,nodes,node_set)
            print(len(nodes))
            if not exists:            
                queue.insert(ind+1,new_node)
        if new_node[0:9] == goal_node:
            isgoal = True
            break
        else:
            isgoal = False
    queue.remove(cur_node)

path = generate_path(nodes)
for node in path:
    print_matrix(node)

