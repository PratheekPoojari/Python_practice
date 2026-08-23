class Wizard:
    def __init__(self, name:str) -> None:
        if not name:
            raise ValueError("Missing Name!")
        self.name = name

    ...


# class ChildClass(ParentClass) -> this means that the 'ChildClass' inherits (or) is a subclass of the 'ParentClass'.
# In this case Student is a sub-class of Wizard, hence it inherits from it. This also make Wizard the super-class of Student.
class Student(Wizard):
    def __init__(self, name:str, house:str) -> None:
        # 'super()' -> makes a reference to the super class of the current class,from Student to Wizard in our case. 
        # '.__init__(attribute)' -> accesses the init dunder method of the super-class and passes to it, the value assigned
        # to the attribute of the sub-class. So, here the value assigned to the 'name' attribute of Student is passed to the
        # 'name' attribute of the Wizard class.
        super().__init__(name)
        self.house = house

    ...


class Professor(Wizard):
    def __init__(self, name:str, subject:str) -> None:
        super().__init__(name)
        self.subject = subject

    ...



wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defense against the Dark Arts")

print(f"Wizard's name: {wizard.name}")
print(f"{student.name} is from {student.house}")
print(f"{professor.name} teaches {professor.subject}")
