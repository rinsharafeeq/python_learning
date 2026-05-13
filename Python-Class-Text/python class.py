#
# a = 33
# b = 200
# if b > a:
#   print("b is greater than a")
# elif b<a:
#     print("b is less than a")
# else:
#     print("b is not  equal to a")
#
#
# a = 25
# b = 20
#
# if a > b or a < b:
#    print("I am right")
#    print("next Line")


# import camelcase
# c = camelcase.CamelCase()
# txt = "hello world"
# print(c.hump(txt))


# import re
# str = "The rain in Spain"
# x = re.search(r"\bS\w+", str)
# print(x.span())


# import re
# str = "The rain in Spain"
# x = re.search(r"\bS\w+", str)
# print(x.string)


# import re
# str = "The rain in Spain"
# x = re.search(r"\bS\w+", str)
# print(x.group())
#
# import re
# str = "The rain in Spain"
# x = re.sub(r"\s", "9", str)
# print(x)

#
# class mysample :
#     def hello(self,n) :
#         self.name=n
#     def print_name(self):
#         print(self.name)
# x=mysample()
# y=mysample()
# name="dilna"
# x.hello(name)
# y.hello('ashique')
# x.print_name()
# y.print_name()
#

# import json
# # some JSON:
# x =  '{ "name":"John", "age":30, "city":"New York"}'
# # parse x:
# y = json.loads(x)
# # the result is a Python dictionary:
# print(y["name"])
# print(y["age"])
# print(y["city"])
# print(y)


# import json
# x = {"name": "John",
#      "age": None,
#      "city": "New York"
# }
# y = json.dumps(x)
# print(y)


# import json
# print(json.dumps({"name": "John", "age": 30}))
# print(json.dumps(["apple", "bananas"]))
# print(json.dumps(("apple", "bananas")))
# print(json.dumps("hello"))
# print(json.dumps(42))
# print(json.dumps(31.76))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None))
#
#
# import json
# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }
# print(json.dumps(x))


# print(json.dumps(x, indent=4, separators=(". ", " = ")))
# separators(item_separator,key_value_separator)
#
#
# print(json.dumps(x, indent=4, sort_keys=True))  # alphapat order values aavaan



# class ashique:
# 	print("this is my class")
# 	a = 10
# print (ashique.a)


# class human :
#     eyes = 2
#     legs = 2
# print(human.eyes)
# print(human.legs)


# class Car:
# 	wheel = 4
# 	door = 10
# 	print("This is my class")
#
#
# Benz = Car()
# print(Benz.wheel)
#
# Toyota = Car()
# print(Toyota.door)

#
# class human:
#     eyes = 2
#     legs = 2
#     address = 'earth'
#     def breath(self):
#         print('breathing')
#     def walk(self):
#         print('walking')
# dilna = human()
# print(dilna.eyes)
# print(dilna.legs)
# print(dilna.address)
# dilna.breath()
# dilna.walk()
#
#
# class Teacher(human):
#       def teach(self):
#           print ("Teaching")
#
# class Artist(human):
#       def teach(self):
#           print ("painting")
#
# ali = Teacher()
# ali.teach()

#
# class Teacher:
#     def teach(self):
#         print("Teaching")
#
#
# class Bioteacher(Teacher):
#     pass
#
#
# class EngTeacher(Teacher):
#     pass
#
#
# anil = Teacher()
# anil.teach()
# sunil = Bioteacher()
# sunil.teach()
#
#
#
# class Teacher:
#       def teach(self):
#           print ("Teaching")
#
# class Bioteacher(Teacher):
#       def teach(self):
#           print ("Teaching Biology")
#
# class EngTeacher(Teacher):
#       def teach(self):
#           print ("Teaching English")
#
#
# anil = Bioteacher()
# anil.teach()
# SUNIL =('teaching english')
# sunil.teach()

#
# class animal():
#     legs = 0
#
#     def walk(self):
#         print("walking")
#
#
# puppy = animal()
# # puppy.legs = 4
# print(puppy.legs)


class Animal():
    legs = 0

    def walk(self):
        print("walking")

    def count_legs(self):
        print("number of legs %d" % legs)


puppy = Animal()
puppy.legs = 4

Kangaroo = Animal()
Kangaroo.legs = 2

fish = Animal()


      def slate(self):
          print("slate from class one")

class Two:
      def slate(self):
          print("slate from class Two")

      def notebook(self):
          print("Notebook from class Two")

class Three:
      def notebook(self):
          print("Notebook from class Three")
      def textbook(self):
          print("Textbook from Class Three")

class Student(One, Two, Three):
akhil = Student()

akhil.slate()

akil.notebook()

akil.textbook()













