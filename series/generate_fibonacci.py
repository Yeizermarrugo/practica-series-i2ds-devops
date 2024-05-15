import os

def generate_fibonacci(max_value):
    fibonacci_series = [0, 1]
    while True:
        next_value = fibonacci_series[-1] + fibonacci_series[-2]
        if next_value > max_value:
            break
        fibonacci_series.append(next_value)
    return fibonacci_series

fibonacci_series = generate_fibonacci(10946)

output_dir = './'
output_file = os.path.join(output_dir, 'fibonacci.txt')

os.makedirs(output_dir, exist_ok=True)

with open(output_file, 'w') as f:
    for number in fibonacci_series:
        f.write(f"{number}\n")
