from random import choice


# simple decorator class to print the call count of a recursive function
class CallCount:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"calls: {self.count}")
        return self.func(*args, **kwargs)


def bits(n: int):
    """n-length bit sequence generator."""
    i = 0
    while i < n:
        i += 1
        yield choice([0,1])


# @CallOut
def dig_root(n: int) -> int:
    """Recursively compute the digital root of n."""
    q, m = divmod(n, 10)
    return n if n == m else dig_root(q + dig_root(m))


def flatten(data: list) -> list:
    """Recursively flatten 'data' into a 1D list"""
    data = sum(data, [])
    if not isinstance(data[0], list):
        return data
    return flatten(data)


def fac(n: int) -> int:
    """Returns n!"""
    return 1 if n < 2 else n*fac(n-1)


def nCk(n: int, k: int) -> int:
    """Returns n choose k."""
    return fac(n) // (fac(n - k) * fac(k))


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

print(sort_words("i a0m a se3nten!ce f1ul#l of w7ords w/ith nu2mbe8rs a@nd sym&*%#3bols"))

# print(anagrams(["arrda", "radar", "cow", "bat", "tab", "batt"]))

