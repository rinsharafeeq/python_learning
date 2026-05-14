
#Task: Create a function filter_even(numbers) which returns a new list containing only the
# even numbers from the input list.
#Filter even numbers from a list
def filter_even(numbers):

    list_even = []
    for num in numbers:
        if num % 2 == 0:
            list_even.append(num)
    return list_even
print(filter_even([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]))