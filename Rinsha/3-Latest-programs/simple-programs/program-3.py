# Append user input to a file with a timestamp
# What it does:
# Asks you to type something, then adds it to notes.txt with the current date and time.
import datetime
from time import strftime

user_note = input("enter a note :")
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
try:
    with open("notes.txt","a") as file:
        file.write(f"{now} - {user_note}\n")
    print("Note saved!")
except Exception as e:
    print("could not save note :",e)