import os

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_primes(max_value):
    primes = []
    for num in range(2, max_value + 1):
        if is_prime(num):
            primes.append(num)
    return primes

primes = generate_primes(79)

output_dir = './'
output_file = os.path.join(output_dir, 'primos.txt')

os.makedirs(output_dir, exist_ok=True)

with open(output_file, 'w') as f:
    for prime in primes:
        f.write(f"{prime}\n")
