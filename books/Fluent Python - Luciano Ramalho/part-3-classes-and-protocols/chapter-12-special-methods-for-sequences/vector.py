from array import array
import math
import reprlib

my_list = [1, 2, 3, 4]


class Vector:
    typecode = 'd'  # used when converting bytes

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __iter__(self):
        # this is equivalent to self._components.__iter__()
        return iter(self._components)

    def __repr__(self):
        # should be a able to call eval(repr(vector)) to get the same class
        components = reprlib.repr(
            self._components)  # truncates data to have a shorter repr and not to overload the terminal
        components = components[components.find('['):-1]  # cleans up unnecassary parts
        return f'Vector({components})'

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)])
                + bytes(self._components))

    def __eq__(self, other):
        # will also work if comparing to [x, y] - a list; feature or a bug depending on what you need
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(*self)

    def __bool__(self):
        # if abs is 0 this is false (aka perpendicular vectors)
        return bool(abs(self))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        # Using notation similar to the array module, the memoryview.cast method lets you
        # change the way multiple bytes are read or written as units without moving bits
        # around. memoryview.cast returns yet another memoryview object, always sharing the
        # same memory.
        memv = memoryview(octets[1:].cast(typecode))
        return cls(memv)

    # def __format__(self, fmt_spec=''):
    #     if fmt_spec.endswith('p'):
    #         fmt_spec = fmt_spec[:-1]
    #         coords = (abs(self), self.angle())
    #         outer_fmt = '<{}, {}>'
    #     else:
    #         coords = self
    #         outer_fmt = '({}, {})'
    #     components = (format(c, fmt_spec) for c in coords)
    #     return outer_fmt.format(*components)
    #
    # def angle(self):
    #     return math.atan2(self.y, self.x)
    #
    # def __hash__(self):
    #     return hash((self.x, self.y))


if __name__ == "__main__":
    # TODO understand this completely
    v1 = Vector(3, 4)
    print(v1.x, v1.y)
    x, y = v1
    print(x, y)
    print(repr(v1))
    v1_clone = eval(repr(v1))  # TODO eval understand
    print(v1 == v1_clone)
    print(v1)
    octets = bytes(v1)
    print(octets)
    print(abs(v1))
    print(bool(v1), bool(Vector(0, 0)))
    print(format(v1, '.3e'))
    hash(v1)
    print(hash(v1))



