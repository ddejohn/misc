from typing import List, Tuple, Set


def divisors(n: int) -> list:
    return [*filter(lambda x: n % x == 0, range(1, n+1))]


def squarish(n: int) -> int:
    d = divisors(n)
    return d[len(d)//2]


def block_print(x: list):
    w = squarish(len(x))
    s = ""
    i = 0
    for n in x:
        s += f"{n}"
        i += 1
        if i == w:
            s += "\n"
            i = 0
        else:
            s += "  "
    print(s)


def flatten(x: list) -> list:
    x = sum(x, [])
    if isinstance(x[0], list):
        return flatten(x)
    return x


def binary_combs(n: int) -> list:
    return [tuple((i & 2**j)//(2**j) for j in range(n)) for i in range(2**n)]


def set_power(s, n):
    return [[]] if not n else [t + [x] for t in set_power(s, n - 1) for x in s]


def seq(n, p, k):
    return flatten([*map(lambda x: [x]*n**(k-p), range(n))]*n**p)


def combs(n, k):
    return [*zip(*(seq(n, p, k-1) for p in range(k)))]


def truth_table():
    d = {True: "T", False: "F"}
    print(" A | B | not A | not B | not A and not B | A or B ")
    print("---|---|-------|-------|-----------------|--------")
    for A in (True, False):
        for B in (True, False):
            print("|".join([d[A].center(3),
                              d[B].center(3),
                              d[not A].center(7),
                              d[not B].center(7),
                              d[not A and not B].center(17),
                              d[A or B].center(8)]))


def find_reversed_words(L: List[str]) -> Set[Tuple[str]]:
    """Returns a set of word, reversed_word tuples"""
    pairs = [(w, w[::-1]) for w in L if w[::-1] in L]
    return {tuple(sorted(t)) for t in pairs}
