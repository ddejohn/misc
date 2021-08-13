from typing import Union, List, Set, Tuple, Dict
from random import choice
import numpy as np
Number = Union[int, float]


def random_binary_tensor() -> np.ndarray:
    x = np.random.rand(5, 3, 2)
    return (x == x.max(axis=(1, 2))[:, None, None]).astype(int)


def random_probability_vector(n: int) -> np.ndarray:
    x = np.random.randint(0, n**2, n)
    return x / np.sum(x)


# for/else structure
def primes_up_to_n(n: int) -> List[int]:
    primes = []
    for val in range(2, n+1):
        for x in range(2, int(val**(1/2)) + 1):
            if val % x == 0:
                break
        else:
            primes.append(val)
    return primes


# simple decorator class to print the call count of a recursive function
class CallCount:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"calls: {self.count}")
        return self.func(*args, **kwargs)


@CallCount
def bin_search(lst: List[Number], x: Number) -> int:
    """Returns the index where 'x' is located. Assumes 'lst' is sorted."""
    if lst[0] == x:
        return 0
    elif lst[-1] == x:
        return len(lst) - 1

    mid = len(lst) // 2
    if x < lst[mid]:
        return bin_search(lst[:mid], x)
    return mid + bin_search(lst[mid:], x)


def memoize(f: callable) -> callable:
    cache = {}
    def lookup(x):
        if x not in cache:
            cache[x] = f(x)
        return cache[x]
    return lookup


@memoize
def fibonacci(n: int) -> int:
    """Returns the `n`th Fibonacci number."""
    return n if  n < 2 else fibonacci(n - 2) + fibonacci(n - 1)


print(bin_search([*range(1000)], 523))


def bits(n: int):
    """n-length bit sequence generator."""
    i = 0
    while i < n:
        i += 1
        yield choice((0, 1))


@CallCount
def dig_root(n: int) -> int:
    """Recursively compute the digital root of n."""
    q, m = divmod(n, 10)
    return n if n == m else dig_root(q + dig_root(m))


@CallCount
def flatten(data: list) -> list:
    """Recursively flatten 'data' into a 1D list"""
    data = sum(data, [])
    if not isinstance(data[0], list):
        return data
    return flatten(data)


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


def dict_print(data, calls=0):
    out = ""
    t = "   "
    for key, val in data.items():
        if isinstance(val, dict):
            out += t*calls + f"{key}:\n{dict_print(val, calls+1)}"
        else:
            out += t*calls + f"{key}: {val}\n"
    return out


def factorial(n: int) -> int:
    """Returns n!"""
    return 1 if n < 2 else n*factorial(n-1)


def nCk(n: int, k: int) -> int:
    """Returns n choose k."""
    return factorial(n) // (factorial(n - k) * factorial(k))


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


def binomial_pmf(n: int, p: float, k: int) -> float:
    """Returns P(X = k)."""
    return nCk(n, k) * (p**k) * ((1 - p)**(n-k))


def binomial_cdf(n: int, p: float, k: int) -> float:
    """Returns P(X <= k)."""
    return sum(binomial_pmf(n, i, p) for i in range(k+1))


def anagrams(words: list) -> list:
    """Returns a list of words with anagrams present in input."""
    scram = [*map(sorted, words)]
    return [*filter(lambda w: scram.count(sorted(w)) > 1, words)]


def sort_words(s: str) -> str:
    """Sort a string by the first digit in each 'word'"""
    f = filter(lambda w: any(map(str.isdigit, w)), s.split())
    return " ".join(sorted(f, key=lambda w: next(c for c in w if c.isdigit())))


def poly(*coefs):
    """Return a polynomial in x, arranged in standard form"""
    return lambda x: sum(c*x**p for p, c in enumerate(reversed(coefs)))


# our test string
# s = "4of Fo1r pe6ople (*) aofwj1 g3ood!e the2 st8 wan2 0a ssss aaa0a"
# print(sort_words(s))

# print(sort_words("i a0m a se3nten!ce f1ul#l of w7ords w/ith nu2mbe8rs a@nd sym&*%#3bols"))

# print(anagrams(["arrda", "radar", "cow", "bat", "tab", "batt"]))

