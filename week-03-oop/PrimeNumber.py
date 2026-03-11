#Ver 1.
"""
def get_prime_numbers(numbers):
    # Define a helper function to check if a number is prime
    # A number n is prime if n >= 2 and it has no divisors between 2 and int(n**0.5) + 1
    def is_prime(n):
        # TODO: Return False if n is less than 2
        if n < 2:
            return False
        # TODO: Loop from 2 to int(n**0.5) + 1 and return False if any divisor divides n evenly
        for i in range (2, int(n**0.5)+1 ):
            if n%i == 0:
                return False
        # TODO: Return True if no divisors were found
        return True
    
    # Use filter() with the helper function to select prime numbers
    prime_numbers = filter(is_prime, numbers)
    
    # Return the list of selected prime numbers
    return list(prime_numbers)
"""
# Ver 2
"""
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
"""

# Prime number search

def is_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, n))

print (
    is_prime(61234)
)
N = 100
f = filter(is_prime, range(N))

print (f)
print(list(f))
print(list(f))
print (f)
