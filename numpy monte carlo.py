import numpy as np
from numpy.random import MT19937
from numpy.random import RandomState, SeedSequence
import timeit


def f(x: float) -> float:
    return np.exp(-x**2 / 2) / (np.sqrt(2 * np.pi))


def mc1(f: callable, n: int, domain: tuple) -> float:
    rng = RandomState(MT19937(SeedSequence(36297823785)))
    x_bound, y_bound = domain
    area_dom = x_bound * y_bound
    x_vals = x_bound * rng.rand(n)
    y_vals = y_bound * rng.rand(n)

    count = 0
    for x, y in zip(x_vals, y_vals):
        if y <= f(x):
            count += 1

    approx_area = area_dom * (count / n)
    return 2 * approx_area


def monte_carlo(f: callable, n: int, x_bound: float, y_bound: float) -> float:
    """A basic Monte Carlo integrator.

    Note: this integrator assumes that f is an even function,
    and that the bounds of integration are -x_bound to x_bound,
    and that f >= 0 for all x in the integrating domain.

    Parameters
    ----------
    f : callable
        The function object whose definite integral MC approximates.
    n : int
        The number of random points to generate in the domain.
    x_bound : float
        The horizontal bound of the integrating domain.
    y_bound : float
        The vertical bound of the integrating domain.

    Returns
    -------
    float
        The approximate area under f between -x_bound and x_bound.
    """
    rng = RandomState(MT19937(SeedSequence(36297823785)))
    x_vals = x_bound * rng.rand(n)
    y_vals = y_bound * rng.rand(n)
    # x_vals = x_bound * np.random.rand(n)
    # y_vals = y_bound * np.random.rand(n)

    return 2 * x_bound * y_bound * len(y_vals[y_vals <= f(x_vals)]) / n


# y_bound = f(0)
# x_bound = 2
# n = 10000


# t1 = timeit.timeit(
#     "mc1(f=std_nrm_dst, n=n, domain=(x_bound, y_bound))",
#     number=1000,
#     globals=globals()
# )


# t2 = timeit.timeit(
#     "mc2(f=std_nrm_dst, n=n, domain=(x_bound, y_bound))",
#     number=1000,
#     globals=globals()
# )


a = monte_carlo(f=f, n=100000000, x_bound=2, y_bound=f(0))
b = monte_carlo(f=f, n=100000000, x_bound=2, y_bound=10*f(0))

print(a)
print(b)
# print(a == b)
# print(f"mc1: {round(t1, 2)} s")
# print(f"mc2: {round(t2, 2)} s")
