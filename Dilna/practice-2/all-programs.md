1. Multiplication Table (using a loop)
Write a function print_table(n) that prints the multiplication table for n from 1 to 10.
Hint: Use a for loop and range(1, 11).

Example output for print_table(5):

text
5 x 1 = 5
5 x 2 = 10
...
5 x 10 = 50
<details> <summary>Solution</summary>
python
def print_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

print_table(5)
</details>
2. Sum of a List of Numbers
Write a function sum_list(numbers) that takes a list of numbers and returns their sum. Do not use the built-in sum() function.
Test with: [1, 2, 3, 4, 5] → 15, [10, -2, 3] → 11.

Hint: Use a loop to accumulate the total.

<details> <summary>Solution</summary>
python
def sum_list(numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total

print(sum_list([1, 2, 3, 4, 5]))   # 15
print(sum_list([10, -2, 3]))        # 11
</details>
3. Count Vowels in a String
Write a function count_vowels(s) that returns the number of vowels (a, e, i, o, u, case‑insensitive) in the string s.
Test: "Hello World" → 3 (e, o, o); "Python" → 1 (o).

Hint: Convert string to lowercase with s.lower(), then loop through each character and check if it's in "aeiou".

<details> <summary>Solution</summary>
python
def count_vowels(s):
    s = s.lower()
    count = 0
    for ch in s:
        if ch in "aeiou":
            count += 1
    return count

print(count_vowels("Hello World"))  # 3
print(count_vowels("Python"))       # 1
</details>
4. Find the Largest Number in a List
Write a function find_max(numbers) that returns the largest number in a list. Do not use max().
Test: [3, 7, 2, 9, 1] → 9.

Hint: Start by assuming the first element is the largest, then loop through the rest and update if you find a bigger one.

<details> <summary>Solution</summary>
python
def find_max(numbers):
    if not numbers:   # handle empty list
        return None
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val

print(find_max([3, 7, 2, 9, 1]))  # 9
</details>
5. Is Prime? (using a loop and conditionals)
Write a function is_prime(n) that returns True if the number n is prime, else False.
Recall: a prime number is greater than 1 and has no positive divisors other than 1 and itself.
Test: is_prime(7) → True, is_prime(10) → False, is_prime(1) → False.

Hint: Check divisibility from 2 up to sqrt(n) (or simply up to n//2). Use break early when a divisor is found.

<details> <summary>Solution</summary>
python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):  # efficient: check up to sqrt(n)
        if n % i == 0:
            return False
    return True

print(is_prime(7))   # True
print(is_prime(10))  # False
print(is_prime(1))   # False
</details>
6. Reverse a String (without slicing tricks)
Write a function reverse_string(s) that returns the reversed version of s using a loop.
Test: "hello" → "olleh", "Python" → "nohtyP".

Hint: Build a new string by iterating from the last character to the first.

<details> <summary>Solution</summary>
python
def reverse_string(s):
    reversed_str = ""
    for i in range(len(s) - 1, -1, -1):
        reversed_str += s[i]
    return reversed_str

print(reverse_string("hello"))   # olleh
print(reverse_string("Python"))  # nohtyP
</details>
7. Guessing Game (using while and input)
Write a program that:

Stores a secret number (e.g., secret = 42).

Asks the user to guess the number.

If the guess is too low, prints "Too low"; if too high, "Too high".

Continues until the user guesses correctly, then prints "Correct!" and exits.
Bonus: Count how many guesses it took.

<details> <summary>Solution</summary>
python
secret = 42
guess = None
attempts = 0

while guess != secret:
    guess = int(input("Guess the number: "))
    attempts += 1
    if guess < secret:
        print("Too low")
    elif guess > secret:
        print("Too high")
    else:
        print(f"Correct! You took {attempts} attempts.")
</details>
8. Remove Duplicates from a List
Write a function unique_elements(lst) that returns a new list containing only the unique elements of lst (preserve order of first appearance).
Example: [1, 2, 2, 3, 1, 4] → [1, 2, 3, 4]

Hint: Loop through the list and add to a new list only if it's not already there.

<details> <summary>Solution</summary>
python
def unique_elements(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

print(unique_elements([1, 2, 2, 3, 1, 4]))  # [1, 2, 3, 4]
</details>
9. Fibonacci Sequence (first N numbers)
Write a function fibonacci(n) that prints the first n numbers of the Fibonacci sequence (starting with 0, 1).
Example for n=6: 0 1 1 2 3 5

Hint: Use two variables to keep track of the last two numbers, update in a loop.

<details> <summary>Solution</summary>
python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()  # newline

fibonacci(6)  # 0 1 1 2 3 5
</details>
10. Simple Word Counter
Write a function word_count(text) that receives a string of multiple words (separated by spaces) and returns a dictionary (or just prints) how many times each word appears.
Example: "hello world hello" → hello: 2, world: 1

Hint: Use text.split() to get a list of words, then a dictionary to count.

<details> <summary>Solution</summary>
python
def word_count(text):
    words = text.split()
    counts = {}
    for w in words:
        if w in counts:
            counts[w] += 1
        else:
            counts[w] = 1
    return counts

result = word_count("hello world hello")
print(result)  # {'hello': 2, 'world': 1}
</details>
