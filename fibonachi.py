def generate_fibonacci(n: int) -> list:
    sequence = [0, 1]

    for number in range(n - 2):  # generating list according the amount passed in parameter
        sequence.append(sequence[-1] + sequence[-2])

    return sequence


def fibonacci_generator():
    a, b = 0, 1
    while True:  # generating new number only when called
        yield a
        a, b = b, a + b


print(generate_fibonacci(3))
print(generate_fibonacci(15))

generator = fibonacci_generator()
fib_sequence = []
for _ in range(15):
    fib_sequence.append(next(generator))
print(fib_sequence)
