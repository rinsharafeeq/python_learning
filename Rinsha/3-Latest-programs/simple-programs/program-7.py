# Add two numbers (with error handling)
# What it does:
# Asks for two numbers, prints the sum. If the user types text instead of a number, it catches
# the error and asks again.
while True:
   try:
      num1 = int(input("enter a number :"))
      num2 = int(input("enter a number :"))
      print(f"Sum = {num1 + num2}")
      break
   except ValueError :
        print("enter a valid integer ")
