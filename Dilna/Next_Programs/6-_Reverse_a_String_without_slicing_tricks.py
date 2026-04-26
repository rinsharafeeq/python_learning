# Write a function reverse_string(s) that returns the reversed version of s using a loop.
# Test: "hello" → "olleh", "Python" → "nohtyP".
# 
# Hint: Build a new string by iterating from the last character to the first.
#


def reverse_string(s):
    reversed_s = ""
    for char in s:
        reversed_s = char + reversed_s  # h +"" ->"h" ,"e"+"h"->"eh","l"+"eh"->"leh"
    return reversed_s


print(reverse_string("hello"))
print(reverse_string("Python"))
