
#Task: Write rotate_right(lst, k) that returns a new list with elements shifted
# to the right by k positions (elements that fall off the end wrap around to the front).
# Do not use slicing tricks (e.g., lst[-k:] + lst[:-k]) — use loops.
#Rotate a list to the right by k steps


def rotate_right(lst, k):
    if not lst:
        return []
    n = len(lst)
    k = k % n               # handle k larger than list length
    rotated = [0] * n
    for i in range(n):
        rotated[(i + k) % n] = lst[i]
    return rotated

lst = [1,2,3,4,5]
print(rotate_right(lst,3))