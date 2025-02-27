"""
Lessons:
1. abs built-in function returns the absolute value of integers and floats, and the magnitude of complex numbers,
2. infix operators - nfix expressions are mathematical expressions where the operator is placed between its operands.
This is the most common mathematical notation used by humans.
For example, the expression “2 + 3” is an infix expression, where the operator “+” is placed between the operands “2” and “3”
3. Expected behavior for Infix operators return a new instance, without modifying either operand, self or other.
4. Without a custom __repr__, Python’s consolewould display a Vector instance <Vector object at 0x10e100070.
    The string returned by __repr__ should be unambiguous and, if possible, match the
    source code necessary to re-create the represented object. That is why our Vector
    representation looks like calling the constructor of the class (e.g., Vector(3, 4)).
5. In contrast, __str__ is called by the str() built-in and implicitly used by the print function.
It should return a string suitable for display to end users.
6. __str__ falls back to __repr__ if not implemented, and if __repr__ is user friendly enough, you do not need a separate __str__
7. By default, instances of user-defined classes are considered truthy, unless either
__bool__ or __len__ is implemented.
8. Since Python 3.7, the dict type is officially “ordered,” but that only
means that the key insertion order is preserved. You cannot
rearrange the keys in a dict however you like.
"""

"""
vector2d.py: a simplistic class demonstrating some special methods

It is simplistic for didactic reasons. It lacks proper error handling,
especially in the ``__add__`` and ``__mul__`` methods.

This example is greatly expanded later in the book.

Addition::

    >>> v1 = Vector(2, 4)
    >>> v2 = Vector(2, 1)
    >>> v1 + v2
    Vector(4, 5)

Absolute value::

    >>> v = Vector(3, 4)
    >>> abs(v)
    5.0

Scalar multiplication::

    >>> v * 3
    Vector(9, 12)
    >>> abs(v * 3)
    15.0

"""

import math


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x!r}, {self.y!r})'

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        v = self.x + other.x
        y = self.y + other.y

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
