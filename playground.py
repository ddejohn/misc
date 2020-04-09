def divisors(n: int) -> list:
    return [*filter(lambda x: n % x == 0, range(1,n+1))]
# end


def squarish(n: int) -> int:
    d = divisors(n)
    return d[len(d)//2]
# end


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
# end


def flatten(x: list) -> list:
    x = sum(x, [])
    if isinstance(x[0], list):
        return flatten(x)
    return x
# end


def binary_combs():
    # [[(i&n**2)//n**2, (i&n)//n, (i&1)] for i in range(n**3)]
    return [((i&4)//4, (i&2)//2, i&1) for i in range(8)]
# end


def seq(n, p, k):
    return flatten([*map(lambda x: [x]*n**(k-p), range(n))]*n**p)
# end


def combs(n, k):
    return [*zip(*(seq(n, p, k-1) for p in range(k)))]
# end


if __name__=="__main__":
    while True:
        n = int(input("n: "))
        if n < 2:
            break
        k = int(input("k: "))
        print(combs(n, k))
    # end
# end

