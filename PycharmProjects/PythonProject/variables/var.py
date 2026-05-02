print("hello world")
a=37
b=45
print(a,b)
name=" rinsha"
print(name)

x = 10
y = x

print(x)
print(y)

x = 20

print(x)
print(y)

# Creating multiple variables
item1_price = 25
item2_price = 30
item3_price = 15

# Using them in calculations
total = item1_price + item2_price + item3_price
average = total / 3

print(f"Total: ${total}")
print(f"Average price: ${average}")

# Swapping values between variables
a = 5
b = 10
print(f"Before swap: a={a}, b={b}")

# Python's elegant way to swap
a, b = b, a
print(f"After swap: a={a}, b={b}")

a = 5
b = 10

# Swapping
temp = a
a = b
b = temp

print("a =", a)  # Output: a = 10
print("b =", b)  # Output: b = 5

# Getting input from user and storing in variables
# user_name = input("What is your name? ")
# user_age =int(input("How old are you? ")) # Convert text to number
#
# # Calculate future age
# years_to_add = 10
# future_age = user_age + years_to_add
#
# print(f"Hello {user_name}!")
# print(f"In {years_to_add} years, you will be {future_age} years old")

# is_active = (input("Enter True/False: "))
# print(is_active)

# String (text)
message = "Hello, World!"
first_char = message[1]  # Gets 'H'
print(first_char)

# Integer (whole numbers)
count = 42
negative = -10
large = 1_000_000  # Underscores for readability

# Float (decimal numbers)
pi = 3.14159
price = 19.99

# Boolean (True/False)
is_raining = True
is_sunny = False

# Checking variable types
print(type(message))  # <class 'str'>
print(type(count))    # <class 'int'>
print(type(pi))       # <class 'float'>
print(type(is_raining))  # <class 'bool'>
age = "25"  # This is a string, not a number!
next_age = int(age) + 1
print(next_age)

# Temperature converter example
celsius = 25
fahrenheit = (celsius * 9/5) + 32

print(f"{celsius}C is equal to {fahrenheit}°F")

# Now change celsius to 100 and run again
celsius = 100
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is equal to {fahrenheit}°F")

month = "jan\nfeb\nmar\napr"
print (month)
A = """India is my country
All indias are bro and sis"""
print(A)

num = 5
print(id(num))
print(id)
my_name = 'rinsha'
my_age = 18

print("My name is : %s" % my_name)
print("My name is %s and My Age is %s " % (my_name, my_age))
