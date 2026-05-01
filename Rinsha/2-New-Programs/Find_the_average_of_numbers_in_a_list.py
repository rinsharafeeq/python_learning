#Task: Write a function average(numbers) that takes a list of numbers and returns their average.
# Use a for loop to sum them.
def average(numbers):
    if not numbers:
        return 0

    total = 0
    for num in numbers:
        total += num
    return total /len(numbers)

num_list = [5,5,22,44,5,67,90]
result = average(num_list)
print(f"average is {result}")


