from random import randint


def prob_vec(n: int) -> list:
    """Return a list of randomly generated non-zero
       floats, the sum of which will be `1.0`.
    """
    T = 1000
    p = T
    x = []
    for _ in range(n):
        x.append(randint(p//n, p//2))
        p = T - sum(x)
    x[randint(0, n-1)] += p
    return [*map(lambda num: round(num/T, 3), x)]



if __name__ == "__main__":
    for _ in range(10):
        x = prob_vec(10)
        print(sum(x))