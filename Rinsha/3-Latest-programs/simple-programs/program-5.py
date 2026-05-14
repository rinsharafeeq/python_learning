# Simple log writer (with try/except)
# What it does:
# Writes a log message to mylog.txt. If it fails, prints the error.

import datetime

def write_log(message):
    try:
        timestamp = datetime.datetime.now()
        with open("mylog.txt", "a") as log_file:
            log_file.write(f"{timestamp} - {message}\n")
        print("Logged successfully.")
    except Exception as err:
        print("Logging failed:", err)

write_log("hello")
write_log('i am logged')
write_log("Program started")
write_log("User clicked a button")
write_log("Program ended")