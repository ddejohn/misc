import timeit
from random import choice
from string import whitespace, punctuation


def w1(string):
    count = 0

    for whitespace in " \t\n\v\f\r":
        count += string.count(whitespace)

    return count


def w2(string):
    count = 0

    for char in string:
        if char.isspace():
            count += 1

    return count


s = "".join(choice(whitespace + punctuation) for _ in range(100000))

t1 = timeit.timeit(
    "w1(s)",
    number=10000,
    globals=globals()
)

t2 = timeit.timeit(
    "w2(s)",
    number=10000,
    globals=globals()
)

print(f"string constant: {round(t1, 2)} s")
print(f" isspace method: {round(t2, 2)} s")
