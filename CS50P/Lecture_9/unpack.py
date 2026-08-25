# *args -> 'n' number of positional(left to right) arguments. This acts as a place holder for these arguments.
# **kwargs -> 'n' number of 'key word' positional arguments that can becalled by their name

def f(*args, **kwargs): 
    #print(f"Positional: {args}")
    print(f"Named: {kwargs}")

#f(100, 50, 25)
f(galleons=100, sickels=50, knuts=25)





#def total(galleons:int, sickels:int, knuts:int) -> int:
#    return (galleons * 17 + sickels) * 29 + knuts

#coins = {
#        "galleons": 100,
#        "sickels": 50,
#        "knuts": 25
#}

#print(f"{total(**coins)} Knuts")
# The above statement is the same as -> print(f"{total(galleons=100, sickels=50, knuts=25)} Knuts")

# Unpacking -> Use a '*' before a List variable name, '**' before a Dict variable name,and python will handle extracting 
# data from that variable, and assigning it the way it is intended.
# '*' -> List just passes a single value per argument, '**' -> Dict passes the "key" : value pair for each argument.

#coins = [100, 50, 25]
#print(f"{total(*coins)} Knuts")
# The above statement is the same as -> print(f"{total(100, 50, 25)} Knuts")




#first, last =input("What's your name: ").split(" ")
#print(f"Hello, {first}")
