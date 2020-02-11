def print_matrix(node):
    counter = 0
    for row in range(0, len(node)-1, 3):
        if counter == 0 :
            print("-------------")
        for element in range(counter, len(node)-1, 3):
            if element <= counter:
                print("|", end=" ")
            if(node[element] == 0):
                print(" ", "|", end=" ")
            else:
                print(int(node[element]), "|", end=" ")
        counter = counter +1
        print("\n-------------")


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
    path = [nodes[-1]]
    for ind in path_nodes:
        if ind == -1:
            break
        else:
            path.insert(0,nodes[ind])
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



    

    
   

