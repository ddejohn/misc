import timeit
from random import random, randint


rows = randint(20, 120)
cols = randint(20, 120)

x = [[random() for _ in range(cols)] for _ in range(rows)]


def my_transpose(x):
    return [[*t] for t in zip(*x)]
# end


def ugly_transpose(x):
    return [[r[i] for r in x] for i in range(len(x[0]))]
# end


print(f"testing transpose on {rows}x{cols} matrix . . .\n")
print(my_transpose(x) == ugly_transpose(x))


t1 = timeit.timeit(
    "my_transpose(x)",
    number=10000,
    globals=globals()
)

t2 = timeit.timeit(
    "ugly_transpose(x)",
    number=10000,
    globals=globals()
)

print(f"       zip method: {round(t1, 2)} s")
print(f"    comprehension: {round(t2, 2)} s")
