a = -67
if a > 0:
    print("the number is positive")
elif a < 0:
    print("the number is negative")
else:
    print("the number is zero")

a=15
if  (a%2)==0:
    print("even")
a=int(input("enter a number :"))
if a>0:
    print("the number is positive")
else:
    print("the number is negative or zero")

if a%2==0: # a=20 -> 20%2==2
    print("the number is even")
else:
    print("the number is odd")

a=6
if a%5==0:
    print("the number is multiple of 5")
else:
   print("the number is not multiple of 5")

n= int(input("enter  a number"))
if (n%5==0 and n%7==0):
   print(n,"is divisible by 5 and 7")
elif n%5==0:
    print(n,"is divisible by 5 only")
elif n%7==0:
    print(n," is divisible by 7 only")
else:
    print(n,"is not divisible by 5 and 7 ")
print(n,"is negative")


n=-67
if n > 0:
    print(n, "is positive")
elif n == 0:
    print(n, "is 0")
else:
    print(n, "is negative")


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for n in a:
    if n % 2 == 0:
        print(n, "is an even number")
    else:
        print(n, "is an odd number")