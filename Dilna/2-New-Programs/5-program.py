
#Task: Given keys list and values list of the same length,
# create a function make_dict(keys, values) that returns a dictionary where
# each key is paired with the corresponding value. Use a for loop and range.
#Combine two lists into a dictionary (key: value pairs)
def  make_dict(keys, values):
    dict = {}
    for i in range(len(keys)):
        dict[keys[i]] = values[i]
    return dict

name = ["rinsha","dilna","rishana"]
age = [10,20,30]
print(make_dict(name,age))