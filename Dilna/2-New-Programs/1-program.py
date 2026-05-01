#Task: Write a function average(numbers) that takes a list of numbers and returns
# their
#average. Use a for loop to sum them.

def average(numbers):
    sum = 0
    for x in numbers:
       sum = sum + x
    avg = sum / len(numbers)
    print(avg)
average([55,55,67,98])