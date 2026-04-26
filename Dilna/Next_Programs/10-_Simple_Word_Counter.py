# Write a function word_count(text) that receives a string of multiple words
# (separated by spaces) and returns a dictionary (or just prints)
# how many times each word appears.
# Example: "hello world hello" → hello: 2, world: 1
# 
# Hint: Use text.split() to get a list of words, then a dictionary to count.
# 
def word_counter(text):
    words = text.split()
    dictionary = {}
    for word in words:
        if word in dictionary:
            dictionary[word] = dictionary[word] + 1
        if word not in dictionary:
            dictionary[word] = 1

    print(dictionary)
word_counter( "hello world hello how are you you")