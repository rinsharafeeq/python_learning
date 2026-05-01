# Write a function sum_list(numbers) that takes a list of numbers and returns their sum. Do not use the built-in sum() function.
# Test with: [1, 2, 3, 4, 5] → 15, [10, -2, 3] → 11.
# 
# Hint: Use a loop to accumulate the total.
# 
def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Testing the function
print(sum_list([1, 2, 3, 4, 5]))
print(sum_list([10, -2, 3]))
