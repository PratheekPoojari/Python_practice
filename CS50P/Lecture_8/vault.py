class Vault:
    def __init__(self, galleons:int = 0, sickels:int = 0, knuts:int = 0) -> None:
        self.galleons = galleons
        self.sickels = sickels
        self.knuts = knuts

    def __str__(self) -> str:
        return f"{self.galleons} Galleons, {self.sickels} Sickles, {self.knuts} knuts"
    
    # Operator overloading -> This is a property of python through which we can customize the functionality of certain operators.
    # In this case we use the dunder method '__add__' to customize the functionality of the '+' operator, to add the values of 2
    # different classes. Normally, this gives a 'TypeError', but after the overloading it through the use of the '__add__' dunder
    # method, we can add the contents of 2 class as if it were normal addition. 

    # '__add__' -> takes self and one other value, which can be named anything. 'other' in this case, where self refers to the object
    # on the left of the operator(+), the one in which it has been defined and other refers to the class on the right of the operator,
    # which is being added to this class. This also returns values, in this case it is a class containing the sum of both the classes.

    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickels = self.sickels + other.sickels
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickels, knuts)


potters = Vault(100, 50, 25)
print(f"potters have: {potters}")

weasley = Vault(25, 50, 100)
print(f"weasleys have: {weasley}")

total = potters + weasley
print(total)

# galleons = potters.galleons + weasley.galleons
# sickels = potters.sickels + weasley.sickels
# knuts = potters.knuts + weasley.knuts

# total = Vault(galleons, sickels, knuts)
# print(f"total of potters and weasleys is: {total}")
