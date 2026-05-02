# sum=lambda a,b,c:a+b-c
# print(sum(12,3,5))
from http.cookiejar import uppercase_escaped_char

# square=lambda n:n*n
# n=int(input('enter a number :'))
# print('square is :',square(n))
# avg=lambda a,b,c:(a+b+c)/3
# print('average is',avg(2,4,5))
# avg=lambda x,y,z:(x+y+z)/3
# a=int(input('enter a number 1:'))
# b=int(input('enter a number 2:'))
# c=int(input('enter a number 3:'))
# print(avg(a,b,c))
# large=lambda x,y: x if x>y  else y
# a = int(input('enter a number 1:'))
# b = int(input('enter a number 2:'))
# print(large(a,b))
str=lambda s: s.upper()
n=input('enter a string :')
print(str(n))


# lst=[i for i in range(5)]
# print(lst)
# lst=[1,2,3,4]
# new=[i+10 for i in lst]
# print(new)
# lst=['apple','orange','kiwi','mango','banana']
# newlst=[  i  for i in lst if i !='apple']
# print(newlst)
lst=[i  for i in range(0,1000)if i%7==0]
print(lst)