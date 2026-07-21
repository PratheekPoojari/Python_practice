def main():
    x = int(input("Enter the number to check even or odd:",))
    if is_even(x):
        print(f"{x} is Even")
    else:
        print(f"{x} is Odd")

def is_even(n):
    return n % 2 == 0

main()
