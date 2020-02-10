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
        print("You cannot move the blank space left")
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
        print("You cannot move the blank space right")
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
        print("You cannot move the blank space up")
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
        print("You cannot move the blank space down")
    else:
        status = True
        zero_ind = (3*i)+j
        down_ind = (3*i)+(j+1)
        down_element = node[down_ind]
        new_node[down_ind] = 0
        new_node[zero_ind] = down_element
    return [status,new_node]

