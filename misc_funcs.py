from random import choice


# generates n random bits
def bits(n: int):
    i = 0
    while i < n:
        i += 1
        yield choice([0,1])


# return the factorial of a positive integer 'n'
def fac(n: int) -> int:
    if n < 2:
        return 1
    return n*fac(n-1)
# end


# the number of ways to choose 'k' things from 'n' total things
def nCk(n: int, k: int) -> int:
    return int(fac(n) / (fac(n - k) * fac(k)))
# end


# probability of 'k' successes in 'n' bernoulli trials with prob of 'p'
def binomial_pmf(n: int, k: int, p: float) -> float:
    return nCk(n, k) * (p**k) * ((1 - p)**(n-k))
# end


def binomial_cdf(n: int, k: int, p: float) -> float:
    return sum(binomial_pmf(n, i, p) for i in range(k+1))
# end


def anagrams(words: list) -> list:
    """Return a list of words with anagrams present in input."""
    scram = [*map(set, words)]
    return [*filter(lambda w: scram.count(set(w)) > 1, words)]
# end


def sort_words(s: str) -> str:
    """Sort a sentence 's' by the first digit in each word of 's'"""
    # filter out words that don't have at least one digit
    s = filter(lambda word: any(map(str.isdigit, word)), s.split())

    # 'next(c for c in w if c.isdigit())' yields the first digit
    # in each word so 'sorted' can make its value comparisons
    s = sorted(s, key=lambda w: next(c for c in w if c.isdigit()))

    # return a sentence
    return " ".join(s)
# end


# our test string
# s = "4of Fo1r pe6ople (*) aofwj1 g3ood!e the2 st8 wan2 0a ssss aaa0a"
# print(sort_words(s))

print(anagrams(["abcdcba", "radar", "cow", "bat", "tab"]))

