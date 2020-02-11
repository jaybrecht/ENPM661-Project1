from collections import deque

def BlankTileLocation(node):
    # finds the index of the blank element in the list
    ind = node.index(0)
    # Converts index in list to column (i) and row (j). 0 is first row/column
    i = (ind//3) 
    j = (ind%3)
    return [i,j]


def ActionMoveLeft(node):
    # moves the blank tile left if possible, if not set status to false and 
    # return original node.
    [i,j] = BlankTileLocation(node)
    new_node = node.copy()
    if i == 0:
        status = False
    else:
        status = True
        zero_ind = (3*i)+j
        left_ind = (3*(i-1))+j
        left_element = node[left_ind]
        new_node[left_ind] = 0
        new_node[zero_ind] = left_element
    return [status,new_node]


def ActionMoveRight(node):
    # moves the blank tile right if possible, if not set status to false and 
    # return original node.
    [i,j] = BlankTileLocation(node)
    new_node = node.copy()
    if i == 2:
        status = False
    else:
        status = True
        zero_ind = (3*i)+j
        right_ind = (3*(i+1))+j
        right_element = node[right_ind]
        new_node[right_ind] = 0
        new_node[zero_ind] = right_element
    return [status,new_node]


def ActionMoveUp(node):
    # moves the blank tile up if possible, if not set status to false and 
    # return original node.
    [i,j] = BlankTileLocation(node)
    new_node = node.copy()
    if j == 0:
        status = False
    else:
        status = True
        zero_ind = (3*i)+j
        up_ind = (3*i)+(j-1)
        up_element = node[up_ind]
        new_node[up_ind] = 0
        new_node[zero_ind] = up_element
    return [status,new_node]


def ActionMoveDown(node):
    # moves the blank tile down if possible, if not set status to false and 
    # return original node.
    [i,j] = BlankTileLocation(node)
    new_node = node.copy()
    if j == 2:
        status = False
    else:
        status = True
        zero_ind = (3*i)+j
        down_ind = (3*i)+(j+1)
        down_element = node[down_ind]
        new_node[down_ind] = 0
        new_node[zero_ind] = down_element
    return [status,new_node]


def AddNode(new_node,nodes,node_set):
    exists = False
    if tuple(new_node[0:9]) in node_set:
        exists = True
    else:
        nodes.append(new_node)
        node_set.add(tuple(new_node[0:9]))
    return [nodes,node_set,exists]


def generate_path(nodes):
    #Assume the last item in nodes is the goal node
    parent = nodes[-1][9]
    path_nodes = [parent]
    while parent != -1:
        parent_node = nodes[path_nodes[-1]]
        parent = parent_node[9]
        path_nodes.append(parent)
    path = [nodes[-1][0:9]]
    for ind in path_nodes:
        if ind == -1:
            break
        else:
            path.insert(0,nodes[ind][0:9])
    return path


def check_neighbors(cur_node,direction):
    if direction == 'right':
        [status,new_node] = ActionMoveLeft(cur_node)
    if direction == 'left':
        [status,new_node] = ActionMoveRight(cur_node)
    if direction == 'up':
        [status,new_node] = ActionMoveUp(cur_node)
    if direction == 'down':
        [status,new_node] = ActionMoveDown(cur_node)
    return [status,new_node]


def BFS(start_node,goal_node):
    # Data structure for the nodes is a list of lists, each list inside the list 
    # nodes is a node. The first 3 elements are the first column, the second 3 
    # elements are the second column, and the next 3 are the last column. The last 
    # element in the list is the parent node of the node and refers to the index in 
    # nodes where it can be found. The starting node has a parent of -1
    nodes = [[]]

    # Checked nodes are additionally stored in a set which is much faster for 
    # checking if the node has already been visited
    node_set = {tuple(start_node)}

    start_node.append(-1) #set start node to have parent of -1
    nodes[0] = start_node

    # The queue is strucuted as a deque which allows for much faster operation
    # when accessing the first item in the list
    queue = deque()
    queue.append(0) #set the start_node as the first node in the queue

    isgoal = False
    success = False

    neighbors = ['left','up','right','down'] #modify order to change the order of search
    while queue:
        # Set the current node as the top of the queue and remove it
        parent = queue.popleft();
        cur_node = nodes[parent]
        for direction in neighbors:
            [status,new_node] = check_neighbors(cur_node,direction)
            if status == True:
                new_node[9] = parent
                [nodes,node_set,exists] = AddNode(new_node,nodes,node_set)
                if not exists:            
                    queue.append(len(nodes)-1)
            if new_node[0:9] == goal_node:
                isgoal = True
                break
        if isgoal:
            success = True
            break

    return [nodes,success]

    
def startGame():
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

    print("\nPlease enter the goal configuration of your puzzle")
    goal_node_str = input("\nGoal Configuration: ")

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

    return [start_node,goal_node]
