balance:int = 0 # Global Variable -> can be read anywhere in the program, but to write to it is not possible directly.
# 'global' -> the keyword that makes it so that global variables can be edited by any function in the file.


def deposit(n:int) -> None:
    global balance
    balance += n

def withdraw(n:int) -> None:
    global balance
    balance -= n

def main():
    print(f"Balance: {balance}")
    deposit(100)
    withdraw(50)
    print(f"Balance: {balance}")





if __name__ == "__main__":
    main()
