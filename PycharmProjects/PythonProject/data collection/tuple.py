tup=tuple(input('enter the number :').split())
print(tup)
even_lst=[]
odd_lst=[]
for i in tup:
    if int(i)%2==0:
        even_lst.append(i)
    else:
        odd_lst.append(i)
print(tuple(even_lst),"even number")
print(tuple(odd_lst),"odd number")

# tup=(1,2,3,4,'apple')
# print(type(tup))
# print(tup[0:5])
# tup=(1,2,3,4,5,4,5)
# print(tup)
# tup=tuple(input("enter the elements :").split())
# print(tup)
# print(type(tup))
# seet={1,2,3,4,5,7,7,7,8,9,7}
# print(type(seet))
# print(seet)
# print(len(seet))
# seet.pop()
# print(seet)