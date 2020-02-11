from functions import *
from plot_path import *
from collections import deque

# Data structure for the nodes is a list of lists, each list inside the list 
# nodes is a node. The first 3 elements are the first column, the second 3 
# elements are the second column, and the next 3 are the last column. The last 
# element in the list is the parent node of the node and refers to the index in 
# nodes where it can be found. The starting node has a parent node of -1

nodes = [[]]

print("\n*****************************")
print("Welcome to the 8 Puzzle Game")
print("*****************************\n")
print("Please enter the starting configuration of your puzzle")
print("  It should have the form of \n  11,21,31,12,22,32,13,23,33\n")
print("  For a puzzle like this:\n")
print("    11  12  13\n")
print("    21  22  23\n")
print("    31  32  33\n")

start_node_str = input("Starting Configuration: ")

print("Please enter the goal configuration of your puzzle")
goal_node_str = input("Goal Configuration: ")

start_node = [] #[8,4,2,3,1,7,5,6,0]
goal_node = [] #[5,4,3,6,0,2,7,8,1]

for s in start_node_str:
    if s.isdigit():
        start_node.append(int(s))

for s in goal_node_str:
    if s.isdigit():
        goal_node.append(int(s))

if (len(goal_node) != 9) or (len(start_node) != 9):
    raise Exception('Your configurations are not formatted correctly')

# Checked nodes are additionally stored in a set which is much faster for 
# checking if the node has already been visited
node_set = {tuple(start_node)}

start_node.append(-1)
nodes[0] = start_node

# The queue is strucuted as a deque which allows for much faster operation
queue = deque()
queue.append(0)

isgoal = False
neighbors = ['left','up','right','down'] #modify order to change the order of search
while queue:
    # Set the current node as the top of the queue and remove it
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

path_file = open("nodePath.txt","w+")
for node in path:
    for tile in node:
        path_file.write(str(tile)+" ")
    path_file.write("\n")
path_file.close()

plot_path()
