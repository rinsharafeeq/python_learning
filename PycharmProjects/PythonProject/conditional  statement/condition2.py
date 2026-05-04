n1=int(input("enter a numbers 1:"))
n2=int(input("enter a number 2 :"))
n3=int(input("enter a number 3 :"))
if n1>=n2 and n1>=n3:
    print(n1,"is large")
elif n2>=n1 and n2>=n3:
    print(n2,"is large")
else:
    print(n3,"is large")
