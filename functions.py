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
    # Converts index in list to column (i) and row (j)
    i = (ind//3) + 1
    j = (ind%3) + 1
    return [i,j]