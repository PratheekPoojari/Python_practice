import sys

a = float(input("Enter the value of a:",))
b = float(input("Enter the value of b:",))

#a = round(a) # Rounds the float to the nearest integer value

while 1:
    print("\nChoose your Operation Code:")
    op = int(input("1.Addition, 2.Subtraction, 3.Multiplication, 4.Division, 5.Remainder, 6.Sqaure, 7.Exit\n",))

    match op:
        case 1:
            res = a + b
            print(f"Sum of {a} and {b} is: {res}\n")

        case 2:
            diff = a - b
            print(f"Difference of {a} and {b} is: {diff}\n")

        case 3:
            prod = a * b
            print(f"The product of {a} and {b} is: {prod:,}\n") # {prod:,} -> specifies that there needs to be a comma after every '3' digits
                                                                #(3 is by default, can be changed to any value as required).
        
        case 4:
            if(b == 0):
                print("Error!!!, Can't divide by 0!\n")
            else:
                #dvsn = round(a / b, 3)
                dvsn = a / b
                print(f"The division of {a} by {b} gives: {dvsn:.3f}\n") # The .3f functions the same as the round function before, 
                                                                         #displaying only 3 values after the decimal place.
        
        case 5:
            rem = a % b
            print(f"The remainder, when {a} is divided by {b} is: {rem}\n")
        
        case 6:
            sqr = a * a
            sqr1 = b * b
            print(f"The square of {a} is: {sqr} and square of {b} is: {sqr1}\n")
        
        case 7:
            print("Exiting the CLI Calculator.\nThank You for using it.")
            sys.exit(0)
        
        case _: # Default case
            print("Choose a Valid Option!!!\n")
