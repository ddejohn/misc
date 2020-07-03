# return the factorial of a positive integer 'n'
def fac(n: int) -> int:
    if n < 2:
        return 1
    return n*fac(n-1)
# end


# simple decorator class to print the call count of a recursive function
class CallCount:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"calls: {self.count}")
        return self.func(*args, **kwargs)


# @CallCount
def rec_dig_sum(n: int) -> int:
    """Recursive digit sum (ex: 101 -> 1 + 0 + 1 -> 2)."""
    if n % 10 == n:
        return n
    return rec_dig_sum(n // 10 + rec_dig_sum(n % 10))


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


def anagram(lst):
    return [i for i in lst for j in lst if i != j and (sorted(i) == sorted(j))]
# end


# our test string
s = "4of Fo1r pe6ople (*) aofwj1 g3ood!e the2 st8 wan2 0a ssss aaa0a"


def sort_words(s: str) -> str:
    """Sort a sentence 's' by the first digit in each word of 's'."""
    # filter out words that don't have at least one digit
    s = filter(lambda word: any(map(str.isdigit, word)), s.split())

    # 'next(c for c in w if c.isdigit())' yields the first digit
    # in each word so 'sorted' can make its value comparisons
    s = sorted(s, key=lambda w: next(c for c in w if c.isdigit()))

    # return a sentence
    return " ".join(s)
# end


print(sort_words(s))
