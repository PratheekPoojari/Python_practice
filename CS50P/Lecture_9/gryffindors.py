students = [
    {"name": "Hermione", "house":"Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]

def is_gryffindor(s:dict) -> bool:
    return s["house"] == "Gryffindor"

# filter(function, iterable) -> similar to 'map', but expects the function to return a boolean value, which is 
# later applied to each value in the iterable, and returns only the values that have 'True' as their boolean value.
gryffindors = filter(is_gryffindor, students)

for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
    print(gryffindor["name"])

#gryffindors = [
#    student["name"] for student in students if student["house"] == "Gryffindor"
#]

#for gryffindor in sorted(gryffindors):
#    print(gryffindor)
