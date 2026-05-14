# import datetime
# x = datetime.datetime.now()
# print(x)
#
# import datetime as dt  # short aayi eyuthaan
# x = dt.datetime.now()
# print(x)
#
# import datetime
# x = datetime.datetime.now()
# print(x.year)
# print(x.strftime('%j')) # srtftime == string format time
#
# import datetime
# x = datetime.datetime(2020, 5, 17, 10,30)
# print(x)
#
# import datetime
# x = datetime.datetime(2018, 6, 1)
# print(x.strftime("%x"))
#
# import mymodule
# mymodule.greeting("dilna")

# import mymodule
# a = mymodule.person1["country"]
# print(a)
#
# import mymodule as mx
# a = mx.person1["age"]
# print(a)
#
# import platform
# x = platform.system()
# print(x)
#
# import platform
# x = dir(platform)
# print(x)
#
# import mymodule
# x = dir(mymodule)
# print(x)

from mymodule import person1
print (person1["age"])


print("File1 __name__ = %s" %__name__ )
if __name__ == "__main__":
    print("File1 is being run directly")
else:
    print("File1 is being imported")







