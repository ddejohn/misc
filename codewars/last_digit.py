lookup = {
    2: [6, 2, 4, 8],
    3: [1, 3, 9, 7],
    4: [6, 4, 6, 4],
    7: [1, 7, 9, 3],
    8: [6, 8, 4, 2],
    9: [1, 9, 1, 9]
}


def last_digit(n, p):
    k = n % 10
    if not p:
        return 1
    if k in [0, 1, 5, 6] or p == 1:
        return k
    return lookup[k][p % 4]


def reduce(f, args):
    if len(args) == 2:
        return f(args[0], args[1])
    return f(args[0], reduce(f, args[1:]))


x = [776402, 517479, 843559, 517424, 159445, 605444, 458246] # -> 8
# x = [776402, 517479, 843559, 517424, 159445, 605444, 458246, 103959] # -> 8
# x = [226001, 625681, 879174, 566096, 100234] # -> 1

print(reduce(last_digit, x))
