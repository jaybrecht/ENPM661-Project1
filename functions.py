def print_matrix(state):
    counter = 0
    for row in range(0, len(state)-1, 3):
        if counter == 0 :
            print("-------------")
        for element in range(counter, len(state)-1, 3):
            if element <= counter:
                print("|", end=" ")
            print(int(state[element]), "|", end=" ")
        counter = counter +1
        print("\n-------------")
