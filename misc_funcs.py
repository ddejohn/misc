from random import choice


def bits(n: int):
    """n-length bit sequence generator."""
    i = 0
    while i < n:
        i += 1
        yield choice([0,1])


def fac(n: int) -> int:
    """Returns n!"""
    return 1 if n < 2 else n*fac(n-1)


def nCk(n: int, k: int) -> int:
    """Returns n choose k."""
    return int(fac(n) / (fac(n - k) * fac(k)))


def binomial_pmf(n: int, p: float, k: int) -> float:
    """Returns P(X = k)."""
    return nCk(n, k) * (p**k) * ((1 - p)**(n-k))


def binomial_cdf(n: int, p: float, k: int) -> float:
    """Returns P(X <= k)."""
    return sum(binomial_pmf(n, i, p) for i in range(k+1))


def anagrams(words: list) -> list:
    """Returns a list of words with anagrams present in input."""
    scram = [*map(set, words)]
    return [*filter(lambda w: scram.count(set(w)) > 1, words)]


def sort_words(s: str) -> str:
    """Sort a sentence 's' by the first digit in each word of 's'."""
    # filter out words that don't have at least one digit
    s = filter(lambda word: any(map(str.isdigit, word)), s.split())

    # 'next(c for c in w if c.isdigit())' yields the first digit
    # in each word so 'sorted' can make its value comparisons
    s = sorted(s, key=lambda w: next(c for c in w if c.isdigit()))

    # return a sentence
    return " ".join(s)


# our test string
# s = "4of Fo1r pe6ople (*) aofwj1 g3ood!e the2 st8 wan2 0a ssss aaa0a"
# print(sort_words(s))

print(anagrams(["abcdcba", "radar", "cow", "bat", "tab"]))

