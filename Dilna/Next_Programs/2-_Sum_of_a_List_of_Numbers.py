# Write a function sum_list(numbers) that takes a list of numbers and returns their sum.
# Do not use the built-in sum() function.
# Test with: [1, 2, 3, 4, 5] → 15, [10, -2, 3] → 11.
# 
# Hint: Use a loop to accumulate the total.
#
from unittest import result


def sum_list(numbers):
    sum = 0
    for i in numbers:
        sum = sum +i
    print("sum is ",sum)
sum_list([1, 2, 3, 4, 5])
sum_list([10, -2, 3])