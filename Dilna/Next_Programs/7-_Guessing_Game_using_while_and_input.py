# Write a program that:
# 
# Stores a secret number (e.g., secret = 42).
# 
# Asks the user to guess the number.
# 
# If the guess is too low, prints "Too low"; if too high, "Too high".
# 
# Continues until the user guesses correctly, then prints "Correct!" and exits.
# Bonus: Count how many guesses it took.
#


def guessing_game():
    secret = 42
    attempts = 0

    while True:
        # Get user input and convert to an integer
        guess = int(input("Guess the secret number: "))
        attempts += 1

        if guess < secret:
            print("Too low")
        elif guess > secret:
            print("Too high")
        else:
            print(f"Correct! It took you {attempts} guesses.")
            break
guessing_game()


secret =42
attempts = 0
while True:
    number = int(input("Guess the secret number: "))
    attempts += 1
    if number<secret:
        print("Too low")
    elif number>secret:
        print("Too high")
    elif number==secret:
        print(f"Correct! It took you {attempts} guesses.")
        break
