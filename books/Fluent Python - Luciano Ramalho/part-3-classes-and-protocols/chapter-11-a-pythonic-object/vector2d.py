from array import array
import math


class Vector2d:
    typecode = 'd'  # used when converting bytes

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __iter__(self):
        # this is what makes unpacking work, eg:  x, y = my_vector
        # it is also what makes *self work;
        # you can use list(v1) here because of this.
        return (i for i in (self.x, self.y))

    def __repr__(self):
        # should be a able to call eval(repr(vector)) to get the same class
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name,
                                       *self)  # *self works because of __iter__ here; feeds x, y components to format

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        """
        Traced whole method with GPT, here are the findings.

        self.typecode is a string character that represents the type of the numbers used in the vector (in this case 'd' for double precision float). The ord function gets the Unicode code point of that character, which is a number.
        Wrapping ord(self.typecode) in a list and passing it to bytes creates a bytes object containing a single byte, which represents the typecode of the vector data.

        The array type from the array module is used here (note: you need to import array from the array module at the top of your file for this code to work).
        self.typecode is used again as the first argument to array, specifying the data type of the elements in the array.
        self is passed to the array constructor, which expects an iterable to convert into an array of the specified type. Since Vector2d has an __iter__ method, it can be iterated to yield self.x and self.y, effectively creating an array of two double-precision floats.
        Finally, converting this array to bytes gives a bytes object that represents the binary form of the vector's components.

        The typecode 'd' is converted to a single byte which identifies the type of the data in the following bytes.
        The vector components (x and y) are then converted to bytes according to this type specification ('d' for double), and these bytes follow the typecode byte in the final bytes object.

        This approach ensures that the vector can be efficiently serialized and deserialized, maintaining the data type and the exact values of the vector's components. For completeness, don't forget to import the necessary modules (math for math.hypot and array for array.array) at the beginning of your code.


        1. Why use ord and why pass it as a list to bytes?

        The bytes function requires an iterable where each item is an integer in the range 0-255, which represents a byte value. When using ord(self.typecode), it converts the character 'd' into its corresponding ASCII integer value, which is 100. This integer is the byte representation of the character 'd'.
        When you pass this value in a list to bytes, like bytes([ord(self.typecode)]), you're effectively creating a bytes object that starts with the byte 100. If you were to pass the character 'd' directly to bytes without using ord, like bytes(self.typecode, 'utf-8'), it would also give you the same result because encoding 'd' in UTF-8 results in a single byte with the value 100.
        So, in this context, you could indeed directly create a bytes object from the string without converting it first to its ASCII integer value, like so:
        Significance of using array instead of list:

        # Significance of using array instead of list
        The key reason for using an array from the array module instead of a list relates to the efficiency and compactness of data storage and processing. Here’s why using array can be advantageous:
        Efficiency in storage: array objects are more space efficient than lists because they directly store the underlying bytes representing the data type specified (in this case, 'd' for double precision floats), rather than storing pointers to Python float objects as in lists.
        Consistency in data type: Using array enforces a single data type for all elements, which is crucial when handling numerical data for operations like serialization or mathematical computation where type consistency matters.
        Performance: Operations on array can be faster than on lists because they are tightly packed and directly correspond to C-level arrays in memory. This can lead to performance gains especially in data processing or computational contexts.

        Passing things to bytes:

        Strings: Need an encoding specified to convert to bytes because they are made of Unicode characters.
        Iterables (like lists): Must contain integer values 0-255, directly representing byte values.
        Array objects: Can be passed directly to bytes if their data type is such that it represents binary data (like 'd' for double precision floats), making them suitable for direct memory conversion.
        """
        typecode_bytes = bytes([ord(self.typecode)])

        object_bytes = bytes(array(self.typecode, self))

        combined = typecode_bytes + object_bytes

        return combined
        # return (bytes([ord(self.typecode)])
        #         + bytes(array(self.typecode, self)))

    def __eq__(self, other):
        # will also work if comparing to [x, y] - a list; feature or a bug depending on what you need
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

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
        return cls(*memv)

    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('p'):
            fmt_spec = fmt_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = '<{}, {}>'
        else:
            coords = self
            outer_fmt = '({}, {})'
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(*components)

    def angle(self):
        return math.atan2(self.y, self.x)

    def __hash__(self):
        return hash((self.x, self.y))

if __name__ == "__main__":
    # TODO understand this completely
    v1 = Vector2d(3, 4)
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
    print(bool(v1), bool(Vector2d(0, 0)))
    print(format(v1, '.3e'))
    hash(v1)
    print(hash(v1))
