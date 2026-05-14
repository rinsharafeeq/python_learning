# try:
#   print(x)
# except:
#   print("Something went wrong")
# finally:
#   print("The 'try except' is finished")
#
# try:
#   f = open("demofile.txt")
#   f.write("Lorum Ipsum")
# except:
#   print("Something went wrong when writing to the file")
# finally:
# #   f.close()
#
#
# try:
#     number = int(input("Enter a number : "))
#     result = 10 / number
# except ZeroDivisionError:
#     print("Error: You cannot divide by zero!")
# except ValueError:
#     print("Error: That wasn't a valid number.")
try:
   a = open("numbers.txt")
   print(a.read())
except FileNotFoundError:
  print("File not found")



