import re

name = input("What's Your name? ").strip()
# matches = re.search(r"^(.+), *(.+)$", name) # () -> everything in the paranthesis is returned to the user.
# if matches:                                # In this case, used to return the values of first and last name.
    # last = matches.group(1)                # last, first = matches.groups(); .groups() is a method that helps return the value back to the user.
    # first = matches.group(2)               # similarly, .group(n) can be used to get the value of the specific group
    # name = f"{first} {last}"
    # name = matches.group(2) + " " + matches.group(1) # Skipping the use of variables, since we are using them immediately.

if matches := re.search(r"^(.+), *(.+)$", name): # Walrus Operator(:=) -> assigns value and simultaneously asks a boolean question
    name = matches.group(2) + " " + matches.group(1) 
print(f"Hello, {name}")
