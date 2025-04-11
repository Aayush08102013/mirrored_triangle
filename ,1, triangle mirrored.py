totalrows = int(input("Enter your amount of rows : "))

for row in range(1, totalrows +1):
    # Display space
    for space in range(1, (totalrows - row) +1 ):
        print(" ", end=" ")

    # Display *
    for symbol in range(1, row+1):
        print("*", end=" ")
    
    print()


