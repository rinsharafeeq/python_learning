# tm=int(input("enter total mark out of 500 :"))
# p=tm/500*100
# if p>=80:
#     print("A Grade")
# elif p>=60:
#     print("B grade")
# elif p>=50:
#     print("C grade")
# elif p>=40:
#     print("D grade")
# else:
#     print("FAILED")
a = 25
b = 20

if a > b or a < b:
   print("I am right")
   print("next Line")
a = 33
b = 200
if b > a:
  print("b is greater than a")
a =100
b =500
if a > b: print("a is greater than b")

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

a = 5
b = 10
print("A") if a > b else print("B")

age = 12

if age >= 18:  # 12 >= 18
    print("You can vote!")

score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is: {grade}")

age = 25
has_license = True

# Both conditions must be True
if age >= 18 and has_license:
    print("You can drive!")

# At least one condition must be True
if age >= 65 or age <= 12:
    print("You get a discount!")

# Reverse a condition
if not has_license:
    print("You need a license to drive!")

    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == "admin" and password == "secret123":
        print("Login successful! Welcome admin!")
    elif username == "guest" and password == "guest":
        print("Login successful! Welcome guest!")
    else:
        print("Invalid username or password!")