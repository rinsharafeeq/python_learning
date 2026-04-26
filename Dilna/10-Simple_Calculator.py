# Write a function calculate(a, b, op) where op is a string ("+", "-", "*", "/").
# It should print the result of the operation. If op is unrecognized, print "Unknown operation".

#Test with:

#(10, 5, "+") → 15

#(10, 5, "-") → 5

#(10, 5, "*") → 50

#(10, 5, "/") → 2.0

#(8, 2, "%") → "Unknown operation"

#========================
def calculate(a, b, op):
    if op == "+":
        return a+b
    elif op == "-":
        return a-b
    elif op == "*":
        return a*b
    elif op == "/":
        return a/b
    else:
        return "unknown operation"
print(calculate(10, 5, "+"))
print(calculate(10, 5, "-"))
print(calculate(10, 5, "*"))
print(calculate(10, 5, "/"))
print(calculate(8,  2, "%"))
