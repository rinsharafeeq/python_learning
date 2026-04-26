1. Greeting Function
Write a function greet(name) that takes a name as a parameter and prints "Hello, <name>!". Then call it with three different names.

Example output:

text
Hello, Alice!
Hello, Bob!
Hello, Charlie!

<details> <summary>Solution</summary>
python
def greet(name):
    print("Hello, " + name + "!")

greet("Alice")
greet("Bob")
greet("Charlie")
</details>

2. Add Two Numbers
Write a function add(a, b) that prints the sum of a and b. Call it with numbers like (3, 5), (10, -2), (0, 0).

Expected output:

text
8
8
0
<details> <summary>Solution</summary>
python
def add(a, b):
    print(a + b)

add(3, 5)
add(10, -2)
add(0, 0)
</details>
3. Rectangle Area
Write a function rectangle_area(length, width) that calculates and prints the area. Then call it with (5, 3) and (2.5, 4).

Output:

text
15
10.0
<details> <summary>Solution</summary>
python
def rectangle_area(length, width):
    area = length * width
    print(area)

rectangle_area(5, 3)
rectangle_area(2.5, 4)
</details>
4. Celsius to Fahrenheit
Write a function c_to_f(celsius) that converts Celsius to Fahrenheit using the formula (celsius * 9/5) + 32 and prints the result. Test with 0, 100, -40.

Output:

text
32.0
212.0
-40.0
<details> <summary>Solution</summary>
python
def c_to_f(celsius):
    fahrenheit = (celsius * 9/5) + 32
    print(fahrenheit)

c_to_f(0)
c_to_f(100)
c_to_f(-40)
</details>
5. Even or Odd?
Write a function even_or_odd(number) that prints "Even" if the number is even, and "Odd" if it is odd. Test with 4, 7, 0, -3.

Hint: Use the modulo operator %. A number is even if number % 2 == 0.

<details> <summary>Solution</summary>
python
def even_or_odd(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

even_or_odd(4)
even_or_odd(7)
even_or_odd(0)
even_or_odd(-3)
</details>
6. Swap Two Variables
Write a function swap(a, b) that prints the values of a and b before swapping, then swaps them (using a temporary variable), and prints the values after swapping. Call it with (10, 20) and ("cat", "dog").

Example output:

text
Before: a=10, b=20
After:  a=20, b=10
Before: a=cat, b=dog
After:  a=dog, b=cat
<details> <summary>Solution</summary>
python
def swap(a, b):
    print("Before: a=" + str(a) + ", b=" + str(b))
    temp = a
    a = b
    b = temp
    print("After:  a=" + str(a) + ", b=" + str(b))

swap(10, 20)
swap("cat", "dog")
</details>
7. String Repeater
Write a function repeat_string(s, times) that prints the string s repeated times times (use the * operator). Test with ("Hi", 3), ("Ha", 5).

Output:

text
HiHiHi
HaHaHaHaHa
<details> <summary>Solution</summary>
python
def repeat_string(s, times):
    print(s * times)

repeat_string("Hi", 3)
repeat_string("Ha", 5)
</details>
8. Return the Larger Number
Write a function max_of_two(a, b) that returns the larger number (use return instead of print). Then call it and print the returned value. Test with (8, 12) and (42, 42).

Expected output:

text
12
42
<details> <summary>Solution</summary>
python
def max_of_two(a, b):
    if a > b:
        return a
    else:
        return b

result1 = max_of_two(8, 12)
print(result1)

result2 = max_of_two(42, 42)
print(result2)
</details>
9. Temperature Converter (both ways)
Write two functions: to_celsius(f) and to_fahrenheit(c). Each should return the converted value. Then call them and print the results.

to_celsius(f): formula (f - 32) * 5/9

to_fahrenheit(c): formula c * 9/5 + 32

Test: convert 32°F to Celsius, and 100°C to Fahrenheit.

Output:

text
0.0
212.0
<details> <summary>Solution</summary>
python
def to_celsius(f):
    return (f - 32) * 5/9

def to_fahrenheit(c):
    return c * 9/5 + 32

print(to_celsius(32))
print(to_fahrenheit(100))
</details>
10. Simple Calculator
Write a function calculate(a, b, op) where op is a string ("+", "-", "*", "/"). It should print the result of the operation. If op is unrecognized, print "Unknown operation".
Test with:

(10, 5, "+") → 15

(10, 5, "-") → 5

(10, 5, "*") → 50

(10, 5, "/") → 2.0

(8, 2, "%") → "Unknown operation"

<details> <summary>Solution</summary>
python
def calculate(a, b, op):
    if op == "+":
        print(a + b)
    elif op == "-":
        print(a - b)
    elif op == "*":
        print(a * b)
    elif op == "/":
        print(a / b)
    else:
        print("Unknown operation")

calculate(10, 5, "+")
calculate(10, 5, "-")
calculate(10, 5, "*")
calculate(10, 5, "/")
calculate(8, 2, "%")
</details>

