#Task: Implement a function reverse_list(lst) that returns a new list with elements in reverse order,
# using a for loop.
# Reverse a list without using reverse() or slicing [::-1]
def reverse_list(lst):
    reversed_lst = []
    for x in lst:
        reversed_lst.insert(0,x)
    print(reversed_lst)
reverse_list([1,2,3,4,5])