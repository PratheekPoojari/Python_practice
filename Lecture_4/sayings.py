def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"Hello, {name}")

def goodbye(name):
    print(f"Goodbye, {name}")

if __name__ == "__main__":   # This is a guard clause that python checks for every time a file is run.
    main()                   # If the file is run directly then this __name__ is set to __main__, 
                             # else if it was imported then, the __name__ is set to the file name, 
                             # in this case 'sayings'.
                             # Without this gaurd clause, when imported the file would excute top to bottom,
                             # and also excute all the unwanted function/statements in the file as well.
