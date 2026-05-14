# Calculate days until your birthday
# What it does:
# Asks for your birthday (month and day), then tells you how many days until your next birthday.

import datetime
today = datetime.date.today()
birthday_str =input(" enter  birthday month and day (MM-DD) :")
try:
    birthday_full = datetime.datetime.strptime(f"2000-{birthday_str}","%Y-%m-%d")
    birthday = birthday_full.date().replace(year = today.year)

    if birthday < today:
        birthday = birthday.replace(year = today.year+1)

    days_left = (birthday-today).days
    print(f"your next birthday is in {days_left} days")
except ValueError:
    print("invalid format.please use MM-DD(eg. 05-15 for may 15)")




