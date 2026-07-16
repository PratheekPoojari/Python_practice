def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("Enter the value of n:", ))
        if n > 0:
            return n

def meow(n):
    for i in range(n):
        print("meow")

main()
