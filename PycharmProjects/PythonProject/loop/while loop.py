# i = 1  # initialization
# while i <= 10:   # condition:
#     print('hai')  # body of the loop
#     i = i+1  # updation statement
#

# i = 1
# while i <= 100:
#     print(i)
#     i = i + 1
#

# a = 1
# while a <= 50:
#     print(a)
#     a = a + 2


# i = 1
# while i <= 10:
#     print(i,'hello')
#     i = i + 1
#     if i == 5:
#         break


# i = 0  # 'i' എന്ന വേരിയബിൾ പൂജ്യത്തിൽ തുടങ്ങുന്നു
# while i < 10:
#     i = i + 1
#     if i == 5:
#         continue
#     print(i, 'hello')


count = 1
while count <= 3:
    print(f"Counting: {count}")
    count += 1
else:
    print("Loop finished naturally without a break.")


numbers = [1, 3, 5, 7, 9]
target = 4
i = 0

while i < len(numbers):
    if numbers[i] == target:
        print(f"Found {target}!")
        break
    i += 1
else:
    print(f"Target {target} was not in the list.")