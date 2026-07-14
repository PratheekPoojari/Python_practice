# Strings(str)

# Ask the user for his name.
#name = input("Enter your name:",)

# Ask the user for his name, and then strip the whitespaces off and capitalize the first letter of each word.
#name1 = input("Enter your name:",).strip().title()

# Split users fisrt, middle and last name.

#first, middle, last = name1.split(" ")

# Remove the whitespaces from the left and right of a string.
#name = name.strip()

# Remove the whitespaces from the left and right of a string and Capitalize the fist letter of each word.
#name = name.strip().title()

# All the letters are turned into uppercase
#name1.upper()

# All the letters are turned into lowercase
#name.lower()

# Capitalize user input(only the first letter of the first word).
#name = name.capitalize()

# Capitalize user input(first letter of each word).
#name = name.title()

# Say hello to the user
#print(f"Hello, {name}") # 'f' is the format string, that helps output the variable value inside a string.
#print(f"Hello, {first}")
#print(f"Your initial is: {middle}")
#print(f"Your Surname is: {last}")

#==========================================================================================================================================================================================================================

# Functions

name = input("Enter your name:",).strip().title()

def segregate(a):
    first, middle, last = a.split(" ")
    print(f"Your first name is: {first}")
    print(f"Your middle name is: {middle}")
    print(f"Your last name is: {last}")

def greet(a):
    print(f"Hello, {a}")

segregate(name)
greet(name)
