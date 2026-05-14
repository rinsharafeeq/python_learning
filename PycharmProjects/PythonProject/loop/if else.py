# a = 10
# b = 20
# if a>b:
#     print("a is the biggest number")
# else:
#     print("b is biggest number")
#
# #checks major or minor by age
# age = 20
# if (age >= 18):
#     print("major")
# else:
#     print("minor")
#
# #finding a number is odd or even
# num =int(input("Enter a number"))
# print(num)
# if num%2 == 0:
#     print("even")
# else:
#     print("odd")
#
# num = input("Enter a number: ")
# print(num)
# from importlib import invalidate_caches
#
# num = 30
# if num<=10:
#     print("yellow")
# elif num>10 and num<=20:
#     print("blue")
# else :
#     print("black")


# char = input("Enter a character in VIBGYOR: ").lower() # lower() നൽകിയാൽ ക്യാപിറ്റൽ ലെറ്ററും സ്വീകരിക്കും
#
# if char == 'v':
#     print("Violet")
# elif char == 'i':
#     print("Indigo")
# elif char == 'b':
#     print("Blue")
# elif char == 'g':
#     print("Green")
# elif char == 'y':
#     print("Yellow")
# elif char == 'o':
#     print("Orange")
# elif char == 'r':
#     print("Red")
# else:
# #     print("Invalid Input")
#
# num = 5  # or
# num = int(input("Enter a number: "))
# if num == 1:
#     print("sunday")
# elif num == 2:
#     print("Monday")
# elif num == 3:
#     print("Tuesday")
# elif num == 4:
#     print("Wednesday")
# elif num == 5:
#     print("Thursday")
# elif num == 6:
#     print("Friday")
# elif num == 7:
#     print("Saturday")
# else :
#     print("Invalid Input")

num1 = 10
num2 = 20
num3 = 15
if num1 > num2 and num1 > num3:
    print(f"{num1} is biggest number")  #value venenkil formating function use cheyyuka eg-(f"{num1}....)
elif num2 > num1 and num2 > num3:
    print(f"{num2} is biggest number")
else:
    print(f"{num3} is biggest number")
    #or
if num1 > num2:
    print(f"{num1} is biggest number")
elif num2 > num3:
    print(f"{num2} is biggest number")
else:
    print(f"{num3} is biggest number")
