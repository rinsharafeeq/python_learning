#Write a timestamp to a file What it does: Saves the current date and time into a file called
# timestamp.txt.

import datetime
x = datetime.datetime.now()
result =x.strftime("%Y-%m-%d %H:%M:%S")

with open("timestamp.txt","w") as f:
  f.write(f"current date and time :{result}")
print("Timestamp saved to timestamp.txt")