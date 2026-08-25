#MEOWS = 3 # Demonstartation of a Constant, purely convention here. MEOWS = 4, would easily overwrite it.

#for _ in range(MEOWS):
#    print("meow")

#class Cat:
#    MEOWS = 3

#    def meow(self):
#        for _ in range(Cat.MEOWS):
#            print("meow")

#cat = Cat()
#cat.meow()

def meow(n:int) -> str:
    """
    Meow n times.
        
    :param n: Number of times to meow
    :type n: int
    :raise TypeError: If n is not an int
    :return: A string of meows n times
    :rtype: str

    """ 
    # Official way to document anything in python, rather than using '#' for comments.
    # """Documentation""" -> it makes it so that we can use specific python tools, to analyze, extract and read these
    # 'docstrings' for documentation in python. 
    return "meow\n" * n

number:int = int(input("number: "))
meows:str = meow(number)
print(meows, end = "")
