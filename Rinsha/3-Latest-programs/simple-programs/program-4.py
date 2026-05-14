# Calculate days until your birthday
# What it does:
# Asks for your birthday (month and day), then tells you how many days until your next birthday.
import datetime

today = datetime.date.today()
birthday_str = input("Enter your birthday (MM-DD): ")

try:
    # Parse with a full date using a known leap year (2000) to safely handle Feb 29
    birthday_full = datetime.datetime.strptime(f"2000-{birthday_str}", "%Y-%m-%d")
    birthday = birthday_full.date().replace(year=today.year)

    if birthday < today:
        birthday = birthday.replace(year=today.year + 1)

    days_left = (birthday - today).days
    print(f"Your next birthday is in {days_left} days.")
except ValueError:
    print("Invalid format. Please use MM-DD (e.g., 05-15 for May 15).")
