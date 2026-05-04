# tm=int(input("enter total markout of 500 :"))
# p=tm/500*100
# if p>=80:
#     print("A")
# elif p>=60:
#     print("B")
# elif p>=50:
#     print("C")
# elif p>=40:
#     print("D")
# else:
#     print("FAILED")
# c=input("enter a character :")
# if c in 'aeiouAEIOUA' :
#     print("vowel")
# else:
#     print("not vowel")


print(" 1.additon \n 2.substraction \n 3.multiplication \n 4.division")
ch=int(input("select one :"))
a=int(input("enter a number :"))
b=int(input("enter a number :"))
if ch==1:
     print("the sum is :",a+b)
elif ch==2:
    print("the substraction is :", a-b)
elif ch==3:
     print("the multiplay value is :", a*b)
else:
     print("the divisible value is :", a/b)




