def main():
    n:int = int(input("What's n? "))

    for s in sheep(n):
        print(s)
    #for i in range(n):
    #    print(sheep(i))

def sheep(n:int):
    for i in range(n):
        # yield -> generate value on demand, rather than storing all of them in memory all at once, which can consume 
        # alot of time and space. Useful whilst handling large datasets.
        # 'yeild' returns a 'iterator' that a loop statement can iterate over. This is what is aso known as 'Generators.'
        yield "sheep" * i


    #flock = []
    #for i in range(n):
    #    flock.append("sheep" * i)
    #return flock


    #return "sheep" * n

if __name__ == "__main__":
    main()
