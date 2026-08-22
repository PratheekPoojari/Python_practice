import csv

name = input("What's your name? ",)
address = input("Which area do u live in? ",)

# csv.writer(file) — pairs with csv.reader. You write rows as lists: writer.writerow(["Pratheek", "Bengaluru"]).

# csv.DictWriter(file, fieldnames=[...]) — pairs with DictReader. Unlike DictReader, fieldnames is required here, not optional.
# Because when writing, Python needs to know which dict keys to pull values from and in what column order to write them. 
# Two methods you'll use constantly:
# 'writer.writeheader()' — writes just the header row (name,address) — you call this once, typically right after creating the writer,
# and only if the file doesn't already have a header.
# 'writer.writerow({"header1": value, "header2": value})' — writes one data row, pulling values by matching the dict's keys against fieldnames.
# 'writer.writerow({"name" : name, "address": address})' in this scenario.

with open("students.csv", "a", newline = "") as file:
    writer = csv.DictWriter(file, fieldnames = ["name", "address"])
    writer.writerow({"name": name, "address": address})

# newline="" is required whenever you use the csv module for writing.
# Without it, on some systems you get unwanted blank lines inserted between every row, because both
# Python's text-mode newline translation and the csv module's own newline handling can double up. 
# It's a known quirk, hence always include newline="" when opening a file for csv.writer/DictWriter
