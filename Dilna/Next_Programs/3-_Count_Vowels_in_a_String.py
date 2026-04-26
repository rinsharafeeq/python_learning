# Write a function count_vowels(s) that returns the number of vowels
# (a, e, i, o, u, case‑insensitive) in the string s.
# Test: "Hello World" → 3 (e, o, o); "Python" → 1 (o).
# 
# Hint: Convert string to lowercase with s.lower(),
# then loop through each character and check if it's in "aeiou".
# 
def count_vowels(s):
    i = s.lower()
    count = 0
    for c in i:
      if c in "aeiou":
        count += 1
    return "no.of vowels",count
print(count_vowels( "Hello World"))
print(count_vowels('python'))

