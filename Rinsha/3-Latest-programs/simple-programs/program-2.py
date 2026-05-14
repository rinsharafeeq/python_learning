# Read a file and handle missing file error
# What it does:
# Tries to read data.txt. If it doesn't exist, prints a friendly message instead of crashing.
try:
  with open("data.txt","r") as file:
    print(file.read())
except FileNotFoundError:
    print("File 'data.txt' not found. Please create it and try again.")