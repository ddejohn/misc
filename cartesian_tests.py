import itertools
import timeit
from typing import List, Tuple


def seq(n, p, k):
    return flatten([*map(lambda x: [x]*n**(k-p), range(n))]*n**p)
# end


def combs(n, k):
    return [*zip(*(seq(n, p, k-1) for p in range(k)))]
# end


def flatten(x: list) -> list:
    x = sum(x, [])
    if isinstance(x[0], list):
        return flatten(x)
    return x
# end


# def cartesian(n: int, k: int) -> List[Tuple]:
#     """Pure Python implementation of the cartesian product.

#     Args:
#         n (int): the number of subdivisions of the hypergrid
#         k (int): the number of dimensions of the hypercube

#     Returns:
#         List[Tuple]: A list of coordinate tuples in a k-dimensional
#             hypercube subdivided n times, with one 'corner' at the origin.
#     """
#     x = []
#     for i in range(1, k+1):
#         y = []
#         for j in range(n**k):
#             y.append(j//(n**(k-i))%n)
#         x.append(y)
#     return [*zip(*x)]
# # end


def cartesian(n: int, k: int) -> List[Tuple]:
    """Pure Python implementation of the cartesian product.

    Args:
        n (int): the number of subdivisions of the hypergrid
        k (int): the number of dimensions of the hypercube

    Returns:
        List[Tuple]: A list of coordinate tuples in a k-dimensional
            hypercube subdivided n times, with one 'corner' at the origin.
    """
    return [*zip(*[[j//(n**(k-i)) % n for j in range(n**k)] for i in range(1, k+1)])]
# end


def nested():
    x = []
    r = range(5)
    for i in r:
        for j in r:
            for k in r:
                for p in r:
                    for q in r:
                        x.append((i, j, k, p, q))
    return x


def built_in(n, k):
    x = [[*range(n)]]*k
    return [*itertools.product(*x)]


if __name__ == "__main__":
    # print(nested()==combs(5,5)==cartesian(5,5)==built_in(5,5))

    # t0 = timeit.timeit(
    #     "nested()",
    #     number=10000,
    #     globals=globals()
    # )

    # print("nested done")

    # t1 = timeit.timeit(
    #     "combs(5,5)",
    #     number=10000,
    #     globals=globals()
    # )

    # print("combs done")

    t2 = timeit.timeit(
        "cartesian(5,5)",
        number=10000,
        globals=globals()
    )

    print("cartesian done")

    t3 = timeit.timeit(
        "built_in(5,5)",
        number=10000,
        globals=globals()
    )

    print("cart done")

    # print(f"nested:    {t0}")
    # print(f"combs:     {t1}")
    print(f"cartesian: {t2}")
    print(f"itertools: {t3}")
