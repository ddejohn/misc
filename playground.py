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


def seq(n, p, k):
    return flatten([*map(lambda x: [x]*n**(k-p), range(n))]*n**p)


def combs(n, k):
    return [*zip(*(seq(n, p, k-1) for p in range(k)))]


def truth_table():
    d = {True: "T", False: "F"}

    print("A | B | not A | not B | not A and not B | A or B")
    print("--|---|-------|-------|-----------------|-------")
    for A in (True, False):
        for B in (True, False):
            print(f"{d[A]} | {d[B]} | {d[not A].center(5)} | {d[not B].center(5)} | {d[not A and not B].center(15)} | {d[A or B].center(5)}")




if __name__ == "__main__":
    from itertools import product
    import timeit

    # while True:
    n, k = 3, 3
    # n = int(input("n: "))
    # if n < 2:
    #     break
    # k = int(input("k: "))

    t1 = timeit.timeit(
        "combs(n,k)",
        number=100000,
        globals=globals()
    )
    t2 = timeit.timeit(
        "product(*[[*range(n)]]*k)",
        number=100000,
        globals=globals()
    )

    # for comb in combs(n, k):
    #     print(comb,)
    # print()
    for comb in product(range(n), repeat=k):
        print(comb,)

    print(t1, t2)

    # k = int(input("k: "))
    # print(combs(n, k))
    