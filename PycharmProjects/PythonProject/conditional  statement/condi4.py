print("#################MENU###################\n 1.ADDITION \n 2.SUBSTRACTION \n 3.MULTIPLICATION \n 4.DIVISION")
n1=int(input("enter the number 1:"))
n2=int(input("enter the number 2:"))
ch=int(input("enter your choice :"))
if ch==1:
    print("result is",n1+n2)
elif ch==2:
    print("result is",n1-n2)
elif ch==3:
    print("result is" ,n1*n2)
elif ch==4:
    if n2==0:
        print("division is not possible")
    else:
        print("result is",n1/n2)
else:
    print("invalid choice please select 1 to 4.")
