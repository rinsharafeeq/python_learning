
#Task: Write a function find_pairs(nums, target) that returns a list of unique number pairs
#(as tuples) from nums that add up to target. Use only loops and conditionals (no itertools).
#Find all pairs in a list that sum to a target value





def find_pairs(nums, target):
 pairs = []
 n = len(nums)
 for i in range(n):
  for j in range(i + 1, n):  # j starts after i to avoid duplicate pairs and self-pairing
   if nums[i] + nums[j] == target:
    pairs.append((nums[i], nums[j]))
 return pairs
# Example Test Case
nums_list = [1, 2, 3, 4, 3, 2, 5]
target_val = 6
print(find_pairs(nums_list, target_val))
