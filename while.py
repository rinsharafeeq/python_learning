# #print 1 to 50 using while loop
# i = 1
# while i<51:
#     print(i)
#     i = i + 1
#
# i = 1
# while i <= 5:  # or  # i<6:
#     print('ashique')
#     i = i + 1
#
# # revere order
# i = 6
# while i>0:
#     print(i)
#     i = i - 1
#
# i = 0
# while i<6:
#     print(i)
#     if i==4:
#         break
#     i += 1
#
# x = int(input('how many candies you want'))
# i = 1
# while i<=x:  #or # while i<6:
#     print('candy')
# #     i+=1

# avg = 10
# x = int(input("how many candies you want"))
# if x > avg:
#     print("out of stock")
# else:
#     i = 1
#     while i <= x:
#         print("candy")
#         i += 1

# while loop continue statement
i = 0
while i<6:
    i +=1
    if i == 4:
        continue
    if i == 5:
        continue
    print(i)
    #for loop break statement
fruits = ["apple","banana","cherry"]
for x in fruits:
    print(x)
    if x =="banana":
        break

fruits = ["apple","banana","cherry"]
for x in fruits:
    if x =="banana":
        break
    print(x)

#for loop continue statement
frutes = ["apple","banana","cherry"]
for x in frutes:
    if x == "banana":
        continue
    print(x)

#nested loop
adj = ["red","big","tasty"]
fruits = ["apple","banana","cherry"]
for x in adj:
  for y in fruits:
    print(x,y)

for i in range(1,101):
    if i % 2 != 0:  # odd -> if i%2==0:
        pass
    else:
        print(i)




