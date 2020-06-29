def listify(*args):
    if len(args) == 1:
        return str(args[0])
    *first_n, last = args
    return ", ".join(map(str, first_n)) + f" and {last}"


def format_duration(s):
    if not s:
        return "now"

    convs = {"year": 31536000, "day": 86400, "hour": 3600, "minute": 60, "second": 1}
    res = []
    rem = s
    
    for word, n in convs.items():
        x, rem = divmod(rem, n)
        if x > 0:
            res.append(f"{x} {word}s" if x > 1 else f"{x} {word}")
    
    return listify(*res)


print(format_duration(51871234))
