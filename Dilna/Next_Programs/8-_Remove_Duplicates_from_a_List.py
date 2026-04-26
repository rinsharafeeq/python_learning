# Write a function unique_elements(lst) that returns a new list containing only
# the unique elements of lst (preserve order of first appearance).
# Example: [1, 2, 2, 3, 1, 4] → [1, 2, 3, 4]
# 
# Hint: Loop through the list and add to a new list only if it's not already there.
# 
def unique_elements(lst):
    new_lst = []
    for i in lst:
        if i not in new_lst:
            new_lst.append(i)

    print(new_lst)
unique_elements( [1, 2,2,2,3, 3, 4,4,2])