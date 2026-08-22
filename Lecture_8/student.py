class Student:
    def __init__(self, name, house):           # '__init__' -> 'dunder': 'double underscore' method, that initializes the object. 
        if not name:                           # 'self' -> "The FIRST parameter" in the dunder method that is a mandatory reference 
            raise ValueError("Missing Name")   # to the specific instance of the class being creted. It allows the method to access 
                                               # and modify attributes of that object. needn't be 'self', can be named anything.
        self.name = name   # Instance Variable called 'name'
        self.house = house # Instance Variable called 'house'

    def __str__(self): # Takes only one parameter, 'self' -> reference to the specific instance of the class.
        return f"{self.name} from {self.house}"
    
    @property # Treat this method as a 'Getter', used/runs when the 'house' attribute is read.
    def house(self): 
        return self._house

    @house.setter # Treat this method as 'Setter', used/runs when the 'house' attribute is written to.
    def house(self, house):
        if house not in ["Gryffindor", "Huffelpuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        self._house = house

        
def main():
    student = get_student()
    #print(f"{student.name} from {student.house}")
    print(student) # prints the memory location of the object, as '__str__' isn't defined.
                   # else prints the return value of '__str__'

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)

    #student = Student(name, house) # Constructor Call -> used to 'instantiate' an object from a class's
    #return student                 # blueprint. Ex: 'student' obj from 'Student' Class in this case.
    
    #student = Student() # Creates an object called student of class Student.
    #student.name = input("Name: ") # Attribute called 'name'
    #student.house = input("House: ") # Attribute called 'house'
    #return student


#def get_student(): # Before using classes and objects.
    #name = input("name: ")
    #house = input("house: ")
    #return (name, house) # Returns a 'tuple'
    #name = input("name: ")
    #house = input("house: ")
    #return {"name" : name, "house": house} # Returns a {[key] : [value]} pair.

if __name__ == "__main__":
    main()
