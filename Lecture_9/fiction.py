students = ["Hermione", "Harry", "Ron"]

# enumerate(iterable, start=0), returns the index and the value at that specific index. 
for i,student in enumerate(students):
    print(i+1, student)

#for i in range(len(students)):
#    print(i+1, students[i])

# Dict Comprehension -> similar to List comprehension, syntax: {key: value "statements"}
#gryffindors = {student: "Gryffindor" for student in students}

# List Comprehension
#gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]

#gryffindors = []

#for student in students:
#    gryffindors.append({"name": student, "house": "Gryffindor"})

#print(gryffindors)
