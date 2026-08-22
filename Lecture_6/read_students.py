import csv

students = []

# csv.reader(file) — the basic version. Each row comes back as a plain list of strings (not a dict),
# ["Pratheek", "Ittmadu, Banashankari"]. You'd access fields by index (row[0], row[1]), 
# which is more fragile since column order matters. Rarely what you want when the CSV has headers.

# csv.DictReader(file, fieldnames=None) — what you're using. Takes the first row as headers automatically,
# and returns each subsequent row as a dict keyed by those headers. fieldnames is optional — if you don't pass it,
# it grabs the first row as headers; if you do pass a list like fieldnames=["name", "address"], it uses your list instead 
# and treats the first row as actual data (useful if your CSV has no header row at all).

with open("students.csv") as file:
   reader = csv.DictReader(file)
   for row in reader:
       students.append(row)

# sorted() -> needs to know what to sort by. For a list of numbers, that's obvious (sort by the number itself). 
# But for a list of dicts, Python has no idea which key inside each dict you want to sort on,
# a dict doesn't have a natural "size" the way a number does. That's what the 'key' argument solves: it's a function that,
# given one item from the list, returns the value to actually sort by.

# lambda student: student["name"] is a tiny anonymous function — equivalent to writing:

# def get_name(student):
#   return student["name"], The trade-off is that no loops, or multiple statements. Just a inline throw away function.

# But written inline since it's simple enough not to need a full def. So sorted() runs this function on every dict in students,
# pulls out just the "name" value from each one, and sorts the dicts based on those extracted names — alphabetically, since they're strings.

for student in sorted(students, key = lambda student: student["name"]):
    print(f"{student['name']} lives in:{student['address']}")


