def factorial(n: int) -> int:  # with loop
    fact = 1
    for number in range(2, n + 1):
        fact *= number
    return fact


def factorial2(n: int) -> int:  # with recursion
    if n == 1:
        return n
    return n * factorial2(n - 1)


for num in range(2, 12, 3):
    print(factorial(num))
    print(factorial2(num))
