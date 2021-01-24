import numpy as np
from numpy.random import RandomState
import timeit


# Define the Monte Carlo integrator
def monte_carlo_mask(f, x_bounds, y_bounds, n=1000):
    x_min, x_max = sorted(x_bounds)
    y_min, y_max = sorted(y_bounds)

    rng = RandomState(123456)
    y = rng.uniform(y_min, y_max, n)
    points_under_f = y[y <= f(rng.uniform(x_min, x_max, n))]

    return (x_max - x_min) * (y_max - y_min) * len(points_under_f) / n


def monte_carlo_where(f, x_bounds, y_bounds, n=1000):
    x_min, x_max = sorted(x_bounds)
    y_min, y_max = sorted(y_bounds)

    rng = RandomState(123456)
    y = rng.uniform(y_min, y_max, n)
    points_under_f = y[np.where(y <= f(rng.uniform(x_min, x_max, n)))]

    return (x_max - x_min) * (y_max - y_min) * len(points_under_f) / n


def exponential_pdf(x: float) -> float:
    lam = 2*(7/10)
    return lam * np.exp(-lam * x)


x_bounds = (0, 2)
y_bounds = (0, exponential_pdf(0))


t1 = timeit.timeit(
    "monte_carlo_mask(exponential_pdf, x_bounds, y_bounds, n=1000000)",
    number=1000,
    globals=globals()
)

t2 = timeit.timeit(
    "monte_carlo_where(exponential_pdf, x_bounds, y_bounds, n=1000000)",
    number=1000,
    globals=globals()
)

print(f"mask: {t1:.2f} s")
print(f"where: {t2:.2f} s")
