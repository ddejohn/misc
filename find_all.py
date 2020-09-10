import timeit
from random import randint


def find_all(x: list, n: int) -> list:
    result = []
    start = 0

    for _ in range(x.count(n)):
        idx = x.index(n, start)
        result.append(idx)
        start = result[-1] + 1
    
    return result


x = [randint(0, 10) for _ in range(10000)]

t1 = timeit.timeit(
    "find_all(x, 2)",
    number=10000,
    globals=globals()
)

t2 = timeit.timeit(
    "[idx for idx, val in enumerate(x) if val == 2]",
    number=10000,
    globals=globals()
)

print(f"index method: {t1:.2f} s")
print(f"   enumerate: {t2:.2f} s")
