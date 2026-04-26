# Write a function swap(a, b) that prints the values of a and b before swapping, then swaps them (using a temporary variable), and prints the values after swapping. Call it with (10, 20) and ("cat", "dog")
def swap(a,b):
    print("before swapping ",a,b)
    temp=a
    a=b
    b=temp
    print("after swapping ",a,b)
swap(10,20)
swap("cat","dog")
