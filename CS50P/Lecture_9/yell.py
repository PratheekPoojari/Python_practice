def main():
    #yell("Learning Python from CS50P")
    yell("Learning", "Python", "from", "CS50P")

def yell(*words):
    # List Comprehension -> Create a list, and use a python expression inside the list,
    # that generates a new list by executing that expression/statement.
    uppercased = [word.upper() for word in words]
    print(*uppercased)
    

    # map(function, iterable) -> takes a function and a variable with values to iterate over.
    # Then applies the function to each and every value, and returns it after the moification.
    #uppercased = map(str.upper, words)
    #print(*uppercased)


    #uppercased:list = []
    #for word in words:
    #    uppercased.append(word.upper())
    #print(uppercased)
    #print(*uppercased)


#def yell(phrase:str):
#    print(phrase.upper())

if __name__ == "__main__":
    main()
