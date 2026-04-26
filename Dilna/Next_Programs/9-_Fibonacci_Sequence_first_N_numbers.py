# Write a function fibonacci(n) that prints the first n numbers of the
# Fibonacci sequence (starting with 0, 1).
# Example for n=6: 0 1 1 2 3 5
# 
# Hint: Use two variables to keep track of the last two numbers, update in a loop.
# 
def fibonacci(n):
    a ,b=0,1
    for i in range(n):
        print(a,end = " ")
        a ,b= b,a+b
fibonacci(6)