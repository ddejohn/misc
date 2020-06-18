from random import randint, choices, choice, seed

seed(1)


def prob_vec(n: int) -> list:
    """Return an `n`-length list of randomly generated
       non-zero floats, the sum of which will be `1.0`.
    """
    T = 1000
    p = T
    x = []
    for _ in range(n):
        x.append(randint(p//n, p//2))
        p = T - sum(x)
    x[randint(0, n-1)] += p
    return [*map(lambda num: round(num/T, 3), x)]


def markov_step(w: list) -> int:
    seq = [*range(len(w))]
    x = choices(seq, w, k=len(w))
    return choice(x)


if __name__ == "__main__":
    x = prob_vec(10)
    m = [x[markov_step(x)] for _ in range(1000)]
    for i in set(m):
        print(f"{i}: {m.count(i)}")
