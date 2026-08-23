import random

class Hat:
    # def __init__(self):
        # self.houses = ["Gryffindor", "Hufflepuf", "Ravenclaw", "Slytherin"]
    
    # def sort(self, name:str) -> None:
        # print(f"{name} is in {random.choice(self.houses)}")
    
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"] # Class Variable, shared by the entire 'Class'
    
    # Class method -> makes it so that the class doesn't create instances, and acts as a contianer. similar to a function.
    # 'cls' -> the keyword to access the Class variables('houses', in this case) rather than using self. 
    @classmethod
    def sort(cls, name:str) -> None:
        print(f"{name} is in {random.choice(cls.houses)}")


# hat = Hat()
Hat.sort("Harry")
