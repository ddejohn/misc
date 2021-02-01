import timeit
# from random import choice
# from string import whitespace, punctuation


# def w1(string):
#     count = 0

#     for whitespace in " \t\n\v\f\r":
#         count += string.count(whitespace)

#     return count


# def w2(string):
#     count = 0

#     for char in string:
#         if char.isspace():
#             count += 1

#     return count


# s = "".join(choice(whitespace + punctuation) for _ in range(100000))

def rec_fib(n: int) -> int:
    if n in [0, 1, 2]:
        return [0, 1, 1][n]
    return rec_fib(n - 1) + rec_fib(n - 2)


fib_lookup = {0: 0, 1: 1, 2: 1}


def rec_fib_memo(n: int) -> int:
    if n in fib_lookup:
        return fib_lookup[n]
    else:
        fib_lookup[n] = rec_fib_memo(n - 1) + rec_fib_memo(n - 2)
    return fib_lookup[n]


t1 = timeit.timeit(
    "rec_fib(40)",
    number=10,
    globals=globals()
)

t2 = timeit.timeit(
    "rec_fib_memo(40)",
    number=10,
    globals=globals()
)

print(f"non-memoized: {t1:.2f} s")
print(f"memoized: {t2:.2f} s")
