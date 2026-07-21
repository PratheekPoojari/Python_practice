def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

def fibonacci(n):
    first = 0
    second = 1
    for i in range(1, n):
        temp = first
        first += second
        second = temp
    return first

def print_factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
        print(fact, end = " ")

def print_fibonacci(n):
    first = 0
    second = 1
    print(first, end = " ")
    for i in range(1, n):
        temp = first
        first += second
        print(first, end = " ")
        second = temp

n = int(input("Enter the number, to get it's factorial and fibonacci value and series:"))
res1 = factorial(n)
print("The factorial of", n, "is:", res1)
res2 = fibonacci(n)
print("The fibonacci value of", n, "is:", res2)
print("The factorial series of", n, "is:")
print_factorial(n)
print()
print("The fibonacci series of", n, "is:")
print_fibonacci(n)
print()
