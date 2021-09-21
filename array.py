import operator
from typing import List, Union

Numeric = Union[bool, int, float, complex]


class Array:
    def __init__(self, array: List[Numeric]) -> None:
        self.array, self.dtype = self.type_check(array)

    def __repr__(self):
        return f"Array({self.array})"

    def __len__(self):
        return len(self.array)

    def __neg__(self):
        return Array([-a for a in self.array])

    def __invert__(self):
        if self.dtype == bool:
            return Array([not x for x in self.array])
        raise TypeError("Negation is ambiguous for non-boolean arrays.")

    def __le__(self, other):
        return self.operate(operator.le, other)

    def __rle__(self, other):
        return self.operate(operator.le, other)

    def __ge__(self, other):
        return self.operate(operator.ge, other)

    def __rge__(self, other):
        return self.operate(operator.ge, other)

    def __lt__(self, other):
        return self.operate(operator.lt, other)

    def __rlt__(self, other):
        return self.operate(operator.lt, other)

    def __gt__(self, other):
        return self.operate(operator.gt, other)

    def __rgt__(self, other):
        return self.operate(operator.gt, other)

    def __eq__(self, other):
        return self.operate(operator.eq, other)

    def __add__(self, other):
        return self.operate(operator.add, other)

    def __mod__(self, other):
        return self.operate(operator.mod, other)

    def __mul__(self, other):
        return self.operate(operator.mul, other)

    def __truediv__(self, other):
        return self.operate(operator.truediv, other)

    def __floordiv__(self, other):
        return self.operate(operator.floordiv, other)

    def __pow__(self, other):
        return self.operate(operator.pow, other)

    def __ne__(self, other):
        return self.operate(operator.ne, other)

    def __sub__(self, other):
        return self.__add__(-other)

    def __matmul__(self, other):
        other_as_array = self.validate(other)
        return sum(self.__mul__(other_as_array))

    def __getitem__(self, key):
        if isinstance(key, int):
            return self.array[key]
        elif isinstance(key, slice):
            slice_indices = key.indices(len(self))
            return Array([self.array[i] for i in range(*slice_indices)])
        elif isinstance(key, Array):
            if key.dtype == bool:
                return Array([a for a, k in zip(self, key) if k])
        return Array([self.array[i] for i in key])

    def operate(self, op, other):
        allowable = (bool, int, float, complex)
        if type(other) in allowable:
            return Array([op(a, other) for a in self])
        other_as_array = self.validate(other)
        result = [op(a, b) for a, b in zip(self, other_as_array)]
        types = tuple(set(map(type, result)) & set(allowable))
        if len(types) > 1:
            promote = max(types, key=lambda t: allowable.index(t))
            result = [promote(v) for v in result]
        return Array(result)

    def norm(self, p=2):
        return sum(x**p for x in self)**(1/p)

    def unit(self):
        return self / self.norm()

    # TODO: turn into decorator
    def validate(self, other):
        if type(other) != Array:
            if type(other) in {list, set, tuple}:
                if {type(o) for o in other} & {bool, int, float, complex}:
                    return self.validate(Array(other))
            else:
                raise TypeError(f"The type of 'other' must be 'Array' or 'List[Numeric]' but got type {type(other)}.")

        if len(self.array) != len(other):
            raise ValueError("Elementwise comparison not possible for arrays of different length.")
        return other

    def type_check(self, array):
        if len(types := set(map(type, array))) != 1:
            raise TypeError(f"Arrays must be homogeneous, but received {types}")
        elif len(types & {bool, int, float, complex}) != 1:
            raise ValueError(f"Arrays must contain only Numeric types, but received {types}")
        return list(array), types.pop()
