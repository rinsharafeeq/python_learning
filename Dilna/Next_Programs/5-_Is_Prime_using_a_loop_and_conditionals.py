# Write a function is_prime(n) that returns True if the number n is prime, else False.
# Recall: a prime number is greater than 1 and has no positive divisors other than 1 and itself.
# Test: is_prime(7) → True, is_prime(10) → False, is_prime(1) → False.
# 
# Hint: Check divisibility from 2 up to sqrt(n) (or simply up to n//2). Use break early when a divisor is found.
# 
def is_prime(n):
    if n<= 1:
      return False
    divisor = 2
    while divisor * divisor <=n:# 4 <=3
        if n % 2 == 0: # 10 % 2 == 0
            return False
        divisor += 1
    return True
print(is_prime(4))
print(is_prime(10))
print(is_prime(-71))
