def poly(*coefs):
    return lambda x: sum(c*x**p for p, c in enumerate(reversed(coefs)))
