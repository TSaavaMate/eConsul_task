import random
import string


def min_and_max(sequence: list) -> str:
    minimum = sequence[0]
    maximum = sequence[0]
    for item in sequence:
        if minimum > item:
            minimum = item
        if maximum < item:
            maximum = item
    return f'minimum number in list is {minimum} and maximum is {maximum}'


def rand_password(length: int) -> str:
    characters = string.printable

    return ''.join(random.choice(characters) for _ in range(length))


print(min_and_max([1, 2, 3, 4]))
print(min_and_max([-10, 22, -433, 44]))

print(rand_password(2))
print(rand_password(20))
