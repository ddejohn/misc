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

t1 = timeit.timeit(
    "[num for num in range(1000)]",
    number=100000,
    globals=globals()
)

t2 = timeit.timeit(
    "[*range(1000)]",
    number=100000,
    globals=globals()
)

print(f"comprehension: {t1:.2f} s")
print(f"unpacking: {t2:.2f} s")
