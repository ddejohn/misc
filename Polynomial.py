from __future__ import annotations
import numpy as np
from typing import Union
Number = Union[int, float]


class Polynomial:
    """A polynomial object using coefficient representation form in which
        the ith coefficient corresponds to the ith power of `x`."""
    def __init__(self, *coefs) -> None:
        first_valid = self._validate(coefs)
        last_valid = len(coefs) - self._validate(reversed(coefs))
        self.coefs = coefs[first_valid:last_valid]
        self.degree = len(self.coefs) - 1

    def _validate(self, lst):
        for idx, val in enumerate(lst):
            if val:
                return idx
        raise ValueError(f"The zero polynomial is not supported.")

    def __call__(self, x: Number) -> Number:
        """Evaluate this polynomial at the given `x` value."""
        return np.array([x**i for i in range(len(self))]).dot(self.coefs)
    
    def __eq__(self, other):
        return self.coefs == other.coefs

    def __len__(self) -> int:
        return self.degree + 1

    def __add__(self, other) -> Polynomial:
        p1_len = len(self)
        p2_len = len(other)
        terms_to_pad = [0] * abs(p1_len - p2_len)

        if p1_len < p2_len:
            p1 = np.array(other.coefs)
            p2 = np.array([*self.coefs] + terms_to_pad)
        else:
            p1 = np.array(self.coefs)
            p2 = np.array([*other.coefs] + terms_to_pad)

        return Polynomial(*(p1 + p2))

    def __sub__(self, other) -> Polynomial:
        return self + (-other)

    def __neg__(self) -> Polynomial:
        return Polynomial(*-np.array(self.coefs))

    def __mul__(self, other) -> Polynomial:
        p = np.zeros(len(self) + len(other) - 1, dtype="int64")
        for i, coef_i in enumerate(self.coefs):
            for j, coef_j in enumerate(other.coefs):
                p[i + j] += coef_i * coef_j
        return Polynomial(*p)

    def __truediv__(self, other):
        raise NotImplementedError("This operation is not supported because polynomials are not closed under division.")

    def __floordiv__(self, other):
        raise NotImplementedError("This operation is not supported because polynomials are not closed under division.")

    def __repr__(self) -> str:
        return f"Polynomial{self.coefs} of degree {self.degree}."

    def __str__(self) -> str:
        res = []

        for p, coef in enumerate(self.coefs[:-1]):
            sign = " - " if coef < 0 else " + "
            x = f"x^{p}" if p > 1 else "x" if p == 1 else ""
            k = 1 if coef else 0
            res.append(f"{sign}{abs(coef)}{x}"*k)

        leading_sign = "-" if self.coefs[-1] < 0 else ""
        leading_coef = f"{abs(self.coefs[-1])}"
        leading_term = f"{leading_sign}{leading_coef}" + (f"x^{self.degree}" if self.degree > 1 else "x" if self.degree == 1 else "")

        return "".join([leading_term] + res[::-1])

    def derivative(self) -> Polynomial:
        """Return this polynomial's derivative."""
        n = len(self)
        A = np.array([[0 if (i + 1) != (j + 1) else j for j in range(n)]
                                                      for i in range(n)])
        return Polynomial(*A.dot(np.array(self.coefs))[1:])

    def __rshift__(self, d):
        """Recursively calculate the dth derivative of this polynomial."""
        if d == 0:
            return self
        n = len(self)
        A = np.array([[0 if (i + 1) != (j + 1) else j for j in range(n)]
                                                      for i in range(n)])
        return Polynomial(*A.dot(np.array(self.coefs))[1:]) >> (d - 1)


# Demonstrations

p1 = Polynomial(0, 0, 0, 0, 0, 0, 0, 2, -3, 0, 0, 0, 4, 5, 0, 0, 0, 0, 0, 0, 0)
p2 = Polynomial(5, 3, -1, -2)


try:
    Polynomial(0)
except ValueError as e:
    print(e)

try:
    p1 / p2
except NotImplementedError as e:
    print(e)


print(p1)
print(p2)
print(p1 == p2)
print(p1 + p2)
print(p1 - p2)
print(p1 * p2)
print(p1(2))


# Differentiation by method chaining or by operator repetition
print((p1 * p2).derivative().derivative().derivative().derivative().derivative().derivative())
print((p1 * p2) >> 6) # differentiate 6 times


p3 = Polynomial(3, 4, 7)
print(p3)

try:
    p3 >> 3
except ValueError as e:
    print(e)
