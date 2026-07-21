def main():
    print_square(30)

def print_square(size):

    #For each row in square
    for i in range(size):

        #For each brick in row
        for j in range(size):

            #Print Brick
            print("#", end = "")

        #Prints a new line
        print()

main()
