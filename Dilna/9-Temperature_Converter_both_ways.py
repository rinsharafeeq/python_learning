# Write two functions: to_celsius(f) and to_fahrenheit(c).
# Each should return the converted value. Then call them and print the results.
def to_celsius(f):
     celsius =( f-32)*5/9
     print(celsius)
def to_fahrenheit(c):
    fahrenheit = (c*9/5)+32
    print(fahrenheit)
to_celsius(10)
to_fahrenheit(243)