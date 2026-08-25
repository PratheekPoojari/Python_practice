names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip()) # .rstrip() -> removes the whitespaces to the right(cuz, 'r') of the string, doesn't affect anything on the left.

for name in sorted(names):
    print(f"Hello, {name}")
