# fruits = ["apple", "banana", "cherry"]
# for i in range(len(fruits)):
#     print(f"index {i}:{fruits[i]}")
#
# fruits = ["apple", "banana"]
# fruits.append("cherry")
# print(fruits)
# fruits.insert(1, "orange")
# print(fruits)
# fruits.extend(["graphs","chikku","pineapple","mango"])
# print(fruits)
# fruits.remove("pineapple")
# print(fruits)
# fruits.pop(3)
# print(fruits)
# fruits.pop()
# print(fruits)
# del fruits[2]
# print(fruits)
#
# numbers = [10,20,30,40,50,60,70]
# print(numbers[::2])
# print(numbers[::-1])
# print(numbers[::-2])
# print(numbers[::3])
# print(numbers.index(40))

# grades = [85,77,80,92,88,90]
# avg = sum(grades)/len(grades)
# print(f"average grade : {avg}")
# highest = max(grades)
# print(f"highest grade : {highest}") #print(highest)
# passing=[]
# for i in grades:
#     if i > 85:
#         passing.append(i)
# print("passing grade",passing)

cart=[]
cart.append("laptop")
cart.append("mouse")
cart.append("desktop")
cart.append("tv")
print(cart)
print(f"your cart : {cart}")
print(f"your items :{len(cart)}")
cart.remove("tv")
print(f"after remove : {cart}")
if "laptop" in cart:
    print("laptop is your cart")











