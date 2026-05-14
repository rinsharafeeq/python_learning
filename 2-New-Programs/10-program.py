<<<<<<< Updated upstream
#Task: Write word_frequency(sentence) that takes a string and returns a dictionary where keys
# are words (lowercased) and values are how many times each word appears.
# Words are separated by spaces. Ignore punctuation – for simplicity assume only spaces and letters.
#Count frequency of words in a sentence
def  word_frequency(sentence):
  dic = {}
  words = sentence.lower().split()
  for word in words:
     if word not in dic:
         dic[word] = 1
     else:
         dic[word] = dic[word]+1
  print(dic)
text = "the cat and the dog and the bird"
word_frequency(text)
=======
#Task: Write word_frequency(sentence) that takes a string and returns a dictionary
# where keys are words (lowercased) and values are how many times each word appears.
# Words are separated by spaces. Ignore punctuation – for simplicity assume only spaces
# and letters.
#Count frequency of words in a sentence

>>>>>>> Stashed changes
