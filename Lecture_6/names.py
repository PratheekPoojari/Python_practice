name = input("What's your name? ",)

# If "w"(write mode) is used instead of "a"(append mode), the file that is to be operated, will have it's
# entire data truncated(deleted/cleared) and only the data written in the write mode will be saved.
# Hence, if the already existing contents need to be preserved and adding new content is the goal, we use
# "a" instead of "w"
with open("names.txt", "a") as file: 
    file.write(f"{name}\n")
