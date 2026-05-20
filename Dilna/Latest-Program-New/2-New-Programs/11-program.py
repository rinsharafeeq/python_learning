#Task: Write longest_consecutive(nums) that returns the length of the longest sequence of
# consecutive integers (e.g., [100,4,200,1,3,2] → longest is [1,2,3,4] length 4).
# You can assume no duplicates. Use only loops and lists (no set to speed up – it’s fine to use
# a list for checking).
#Longest consecutive sequence in a list of integers
def longest_consecutive(nums):
    if not nums:
        return 0
    nums_sorted = sorted(nums)  # we'll use sorted – that's allowed
    longest = 1
    current = 1
    for i in range(1, len(nums_sorted)):
        if nums_sorted[i] == nums_sorted[i-1] + 1:  #[1, 2, 3, 4, 100, 200]
            current += 1
        else:
            longest = max(longest, current)
            current = 1
    return max(longest, current)
print(longest_consecutive([100, 4, 200, 1, 3, 2]))