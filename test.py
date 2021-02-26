@profile
def t1():
    el = [x*2 for x in range(1000)]
    return ['foo', *el, 'bar']

@profile
def t2():
    g = (x*2 for x in range(1000))
    return ['foo', *g, 'bar']


if __name__ == "__main__":
    t1()
    t2()
