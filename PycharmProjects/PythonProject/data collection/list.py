# lst=input('enter the list elements :').split()
# print(lst)
# for i in lst:
#     if len(i)%2==0:
#       print(i,'is the even length ')
#
# lst=[1,2,3,4,[2,3,4,],3,54,7]
# print(lst[4],[2])
# lst=[1,2,3,[4,5,[6,7],8],9]
# print(lst[3])
# print(lst[3],[2])
# print(lst[3],[2],[0])

lst=input('enter the list elements :').split()
print(lst)
sum=5
for i in lst:
    sum=sum+int(i)
print(sum)


lst=[1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,3,4,4,4,4,4,4,5,5,5,5,5,5]
newlst=[]
for i in lst:
   if i not in  newlst :
       newlst.append(i)
print(newlst)

lst=[1,2,3,4,5,6]
sum=4
for i in lst:
    sum=sum+i
print(sum)

s=input('enter a string :')
dcount=0  # ethra numbers und enn nookkunnu
acount=0  # ethra letters und enn nookkunnu
for i in s:
    if i.isdigit():
        dcount=dcount+1
    elif i.isalpha():
        acount=acount+1
print(dcount)
print(acount)

lst=[3,1,7,9,0,4]
print(lst)
lst.sort()  # numbers kramathil eyuthaan use cheyyunnu
print(lst)
print(lst[-2])