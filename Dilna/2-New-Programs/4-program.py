
#Task: Write a function count_occurrences(lst, target) that returns the number of
# times target appears in lst. Use a for loop.
#Count how many times a value appears in a list
def count_occurrences(lst,target):
    count = 0
    for item in lst:
        if item == target:
            count += 1
    return f"{target} appears {count} times"
print(count_occurrences(["hello","hello","how","are","you","hello"],"hello"))


