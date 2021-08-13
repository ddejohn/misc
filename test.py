# def dist(x, y, z):
#     return (x**2 + y**2 + z**2)**(0.5)


# def test1():
#     with open("test.csv", "r") as position_data:
#         data = position_data.readlines()

#     # CSV data wrangling
#     data = map(lambda line: map(float, line), map(lambda s: s.strip().split(","), data))
#     return [dist(*v) for v in data]


# def test2():
#     with open("test.csv", "r") as position_data:
#         data = position_data.readlines()

#     # CSV data wrangling
#     data = [line.strip() for line in data]                      # strip newlines
#     data = [line.split(",") for line in data]                   # split on comma
#     data = [[float(val) for val in line] for line in data]      # convert to float

#     return [dist(*v) for v in data]





from typing import Union, List
Number = Union[int, float]


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
