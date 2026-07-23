import csv

name = input("What's your name? ",)
address = input("Which area do u live in? ",)

with open("students.csv", "a", newline = "") as file:
    writer = csv.DictWriter(file, fieldnames = ["name", "address"])
    writer.writerow({"name": name, "address": address})
