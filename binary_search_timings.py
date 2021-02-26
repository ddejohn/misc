import timeit
from typing import Union, List
Number = Union[int, float]


def bin_search(lst: List[Number], x: Number) -> int:
    """Returns the index where `x` is located. Assumes `lst` is sorted."""
    if lst[0] == x:
        return 0
    elif lst[-1] == x:
        return len(lst) - 1

    idx = 0
    search_space = lst.copy()
    while search_space:
        mid = len(search_space) // 2
        if search_space[0] == x:
            return idx
        elif search_space[-1] == x:
            return idx + len(search_space) - 1

        if x < search_space[mid]:
            search_space = search_space[:mid]
        else:
            idx += mid
            search_space = search_space[mid:]


def rec_bin_search(lst: List[Number], x: Number) -> int:
    """Returns the index where `x` is located. Assumes `lst` is sorted."""
    if lst[0] == x:
        return 0
    elif lst[-1] == x:
        return len(lst) - 1

    mid = len(lst) // 2
    if x < lst[mid]:
        return bin_search(lst[:mid], x)
    return mid + bin_search(lst[mid:], x)


# Timing test

n = 10000000
t = n // 2 + 3
x = [*range(n)]

t1 = timeit.timeit(
    "bin_search(x, t)",
    number=100,
    globals=globals()
)

t2 = timeit.timeit(
    "rec_bin_search(x, t)",
    number=100,
    globals=globals()
)

print(f"non-recursive: {t1:.2f} s")
print(f"recursive: {t2:.2f} s")
