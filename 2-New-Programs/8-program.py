
#Task: Write remove_duplicates(lst) that returns a new list with duplicates removed,
# keeping the first occurrence of each element. Use only loops and a helper list (no set or dictionary).
#Remove duplicates from a list while preserving order
def remove_duplicates(lst):
    new_list = []
    for i in lst:
        if i not in new_list:
            new_list.append(i)
    return new_list
lst = [1,1,1,2,3,4,4,4,5]
print(remove_duplicates(lst))
