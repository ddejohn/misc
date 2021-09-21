from typing import Union, List
Number = Union[int, float]


# def deprecated(func):
#     def deprecated_func(*args, **kwargs):
#         print(f"DEPRECATION WARNING: {func.__name__} is deprecated!")
#         return func(*args, **kwargs)
#     return deprecated_func


def deprecated(alt):
    def decorator(f):
        def deprecated_func(*args, **kwargs):
            print("\nDEPRECATION WARNING:")
            print(f"    The '{f.__name__}' function is deprecated.\n")
            print(f"You should use the '{alt.__name__}' function instead.\n")
            return f(*args, **kwargs)
        return deprecated_func
    return decorator


def some_better_function():
    pass


@deprecated(some_better_function)
def some_deprecated_function(*args, **kwargs):
    print(args, kwargs)


def bin_search(lst: List[Number], x: Number) -> int:
    """Returns the index where 'x' is located. Assumes 'lst' is sorted."""
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
    """Returns the index where 'x' is located. Assumes 'lst' is sorted."""
    if lst[0] == x:
        return 0
    elif lst[-1] == x:
        return len(lst) - 1

    mid = len(lst) // 2
    if x < lst[mid]:
        return bin_search(lst[:mid], x)
    return mid + bin_search(lst[mid:], x)


def rec_sum(seq: list) -> float:
    if not seq:
        return 0
    return seq[0] + rec_sum(seq[1:])
