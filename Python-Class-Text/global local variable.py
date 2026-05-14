a = 10
def greet():
    a = 20
    print(a) #local variable

greet()
print(a)# global variable

a = 10
def greet():
    a = 20
    b = 20
    print(a)

greet()
print(a)
#print(b) #b is not defined

a = 10


def greet():
    a = 9
    print("Local variable", a)

    x = globals()['a']
    print("Global Varible", x)


greet()
print(a)


def greeting():
    print("Hello")
    greeting()

greeting()











