def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

two_digit_primes = [num for num in range(10, 100) if is_prime(num)]

print("Two-digit prime numbers:")
print(two_digit_primes)