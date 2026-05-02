# DEFINE a function
def say_hello():
    print("Hello there!")

# USE (call) the function
say_hello()  # P
# rints: Hello there!
def add(a, b):
    return a + b

result=add(3, 5)
print(result)
def my_function(name,place):
    print("my name is %s and i am coming from %s" % (name,place))
    print("my name is ",name)
my_function("rinsha","ullanam")
my_function("pyhon","karnataka")

def printme(test):
    print(test)
    return;
printme("hey")
def def_string_example(country = "Us"):
    print("I am from" , country )

def_string_example("India")
def_string_example(100)
def_string_example(1.5)
def_string_example()

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")


def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))


def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Get input from user
c_temp = float(input("Enter temperature in Celsius: "))
f_temp = celsius_to_fahrenheit(c_temp)
print(f"{c_temp}°C is equal to {f_temp:.1f}°F")




# def sum():
#     a=int(input('enter a number :'))
#     b=int(input('enter a number :'))
#     c=a+b
#     print(c)
# sum()
# sum()
# sum()
# def sum(a,b,c):
#     d=a+b+c
#     print(d)
# sum(2,3,4)
# sum(4,6,7)
# def sub():
#     a=int(input('enter a number :'))
#     b=int(input('enter a number :'))
#     c=a-b
#     print(c)
# sub()
# sub()
# def mul():
#     a=int(input('enter a number :'))
#     b=int(input('enter a number :'))
#     c=a*b
#     print(c)
# mul()
# mul()
# mul()
# def div(a,b):
#     c=a/b
#     print(c)
#
# div(4,8)
# def fact(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     print("factorial of",n,":",fact)
# fact(5)
# fact(7)
# fact(87)
# fact(6)
# fact(3)
# fact(77)
# def sum(a,b):
#     s=a+b
#     return s
#
# hy=sum(2,3)
# print(hy)
# def avg(a,b):
#     average=a+b/2
#     return average
# s=avg(2,4)
# print(s)
# def student_details(n,r,d='BCOM',c='IIT'):
#     print('roll no : ',r)
#     print('name :',n)
#     print('department :',d)
#     print('college :',c)
# student_details('anu','gh',56,5)


# def var_len(*n):
#     for i in n:
#      print(i)
# var_len(10,20,30,40,50,60,70,80,90)


# n=int(input('enter a number :'))
# def factorial(n):
#     if n<=1:
#         return n
#     else:
#        return n*factorial(n-1)
# s=factorial(n)
# print(s)


# n=int(input('enter a number :'))
# def fibonacci(n):
#     if n<=1:
#         return n
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
# n=10
# for i in range(n):
#     print(fibonacci(i),end=' ')
# s=fibonacci(10)
# print(s)

# n=int(input("enter a number :"))
# def  factorial(n):
#     if n<=1:
#         return n
#     else:
#         return n*factorial(n-1) #5 24  4 6  3 2  2 1
# s=factorial(n)
# print(s)