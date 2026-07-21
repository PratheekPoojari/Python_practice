#try:
 #   a = int(input("What's a?\n",))  # checks for int type input from the user.
                                    # try ur best to do only the necessary(the exact line(s) of code, inside 'try'.
    
#except ValueError:
#    print("Please input an integer.") # prints this to the console incase there is a ValueError.
                                      # ValueError -> other data type rather than the before mentioned one. strings/floats in this case.
#else:
#    print(f"a is: {a}") # The above code can be read as: try to take an integer as input from the user. if it is anyother data type(float/string/etc...),
                        # then do as it says in except block, else if the try is successful, execute the else block.
                        # Without this else block, a plain print() would have given NameError, if the try block had failed to get the intended value,
                        # as 'a' would have never been initialized(or even declared in this case).

def main():
    x = get_int("What's 'x'?")
    print(f"x is: {x}")

def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))
            return x
        except ValueError:
            #print("Please input an integer only.")
            pass #does nothing and moves on ahead.

main()
