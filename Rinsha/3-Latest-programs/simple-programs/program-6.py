# Read all lines from a file and print them
# What it does:
# Reads todo.txt and shows each line with a number. If the file is missing, creates an empty one.
try:
    with open("todo.txt", "r") as file:
        lines = file.readlines()
        if lines:
            for i, line in enumerate(lines, start=1):
                print(f"{i}. {line.strip()}")
        else:
            print("Your todo list is empty.")
except FileNotFoundError:
    print("No todo list found. Creating an empty one...")
    with open("todo.txt", "w") as file:
        file.write("")
    print("Created todo.txt – you can add tasks later.")

