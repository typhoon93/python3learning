- if you are writing a library or a framework, the programmers
who will use your classes may expect them to behave like the classes that
Python provides. Fulfilling that expectation is one way of being “Pythonic.”
- Object Representations:
  - repr() __rerp__ - str of object as the developer want's to seee it; what we get in console / debugger; ideally (guideline but not a strict requirement) this should be implemented in such a way, so that if we do eval(reprt(obj)) we get back the original object
  - str() __str__ - str of object as the user wants to see it
  - bytes() __bytes__ - bytes repr of the object
  - format, .format, f strings; - they  call obj.__format__ to get special string displays of an object
- CLassmethod - most common use is alternative constructors, like "frombytes"; you can invoke the class like cls(*memv)
- Staticmethod - receives no special first arg (self). good use cases for staticmethod are very rare in my experience. Maybe the function is closely related even if it never touches the class, so you may want to place it nearby in the code. Even then, defining the function right before or after the class in the same module is close enough most of the time.
- The term "octet" is often used interchangeably with "byte," but traditionally, they have slightly different meanings that stem from the way data is organized and transmitted, particularly in networking and computing contexts. Octet: Strictly refers to a collection of 8 bits. This term is used to avoid any ambiguity, ensuring that it's clear the unit of measurement is precisely 8 bits, no matter the computing context.
- vector2d -> __format__ shows that it is not hard to extend the format specification mini language to use custm format

# How To Make an attribute private:
```python


class Vector2d:
    typecode = 'd'  # used when converting bytes

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)
    
    @property
    def x(self):
        return self.__x
    @property
    def y(self):
        return self.__y
```

# Hashable objects
- A hash should return an int and ideally take into account the
hashes of the object attributes that are also used in the __eq__ method, because
objects that compare equal should have the same hash. Example:
```python
def __hash__(self):
    return hash((self.x, self.y))
```
- It’s not strictly necessary to implement properties or otherwise
protect the instance attributes to create a hashable type. Implementing
__hash__ and __eq__ correctly is all it takes. But the value
of a hashable object is never supposed to change, so this provided a
good excuse to talk about read-only properties.

## Private and “Protected” Attributes in Python

- if you name an instance attribute in the form __mood (two leading underscores and zero or at most one trailing underscore), Python stores the name in
the instance __dict__ prefixed with a leading underscore and the class name, so in
the Dog class, __mood becomes _Dog__mood, and in Beagle it’s _Beagle__mood. This
language feature goes by the lovely name of name mangling.
- Name mangling is about safety, not security: it’s designed to prevent accidental access
and not malicious prying
- The single underscore prefix has no special meaning to the Python interpreter when
used in attribute names, but it’s a very strong convention among Python programmers
that you should not access such attributes from outside the class.
- To conclude: the Vector2d components are “private” and our Vector2d instances are
“immutable”—with scare quotes—because there is no way to make them really private
and immutable.10
# Saving Memory with __slots__
- By default, Python stores the attributes of each instance in a dict named __dict__.
- a dict has a significant memory overhead—even with the optimizations mentioned in that section.
- But if you define a class attribute named __slots__ holding a sequence of attribute names, Python uses an alternative storage model for the instance attributes: the attributes named in __slots__ are stored in a hidden array or references that use less memory than a dict.
```python
>>> class Pixel:
... __slots__ = ('x', 'y')
...
>>> p = Pixel()
>>> p.__dict__
Traceback (most recent call last):
...
AttributeError: 'Pixel' object has no attribute '__dict__'
>>> p.x = 10
>>> p.y = 20
>>> p.color = 'red'
Traceback (most recent call last):
...
AttributeError: 'Pixel' object has no attribute 'color'
```
- the effect of __slots__ is only partially inherited by a subclass 
- To make sure that instances of a subclass have no __dict__, you must declare
__slots__ again in the subclass.
- If you declare __slots__ = () (an empty tuple), then the instances of the subclass
will have no __dict__ and will only accept the attributes named in the __slots__ of
the base class.
- if the class defines __slots__, and you need the
instances to be targets of weak references, then you need to include '__weakref__'
among the attributes named in __slots__.

Comparison of 10 million Vector objects:

```text
$ time python3 mem_test.py vector2d_v3
Selected Vector2d type: vector2d_v3.Vector2d
Creating 10,000,000 Vector2d instances
Initial RAM usage: 6,983,680
Final RAM usage: 1,666,535,424
real 0m11.990s
user 0m10.861s
sys 0m0.978s

$ time python3 mem_test.py vector2d_v3_slots
Selected Vector2d type: vector2d_v3_slots.Vector2d
Creating 10,000,000 Vector2d instances
Initial RAM usage: 6,995,968
Final RAM usage: 577,839,104
real 0m8.381s
user 0m8.006s
sys 0m0.352s
```
- this reveals, the RAM footprint of the script grows to 1.55 GiB when
instance __dict__ is used in each of the 10 million Vector2d instances, but that is
reduced to 551 MiB when Vector2d has a __slots__ attribute. The __slots__ version
is also faster.
- If you are handling millions of objects with numeric data, you
should really be using NumPy arrays,
which are not only memory efficient but have highly optimized
functions for numeric processing, many of which operate on the
entire array at once.

# Overriding Class Attributes
- If we set the typecode of a Vector2d instance to 'f' prior to exporting, each component will be
exported as a 4-byte single precision float.
- If you want to change a class attribute, you must set it on the class directly, not
through an instance. You could change the default typecode for all instances (that
don’t have their own typecode) by doing this:
- Vector2d.typecode = 'f'
- However, there is an idiomatic Python way of achieving a more permanent effect,
and being more explicit about the change. Because class attributes are public, they are
inherited by subclasses, so it’s common practice to subclass just to customize a class
data attribute. The Django class-based views use this technique extensively as the example show:

```text
>>> from vector2d_v3 import Vector2d
>>> class ShortVector2d(Vector2d):
... typecode = 'f'
...
>>> sv = ShortVector2d(1/11, 1/27)
>>> sv
ShortVector2d(0.09090909090909091, 0.037037037037037035)
>>> len(bytes(sv))
```
- This example also explains why I did not hardcode the class_name in Vector2d.
__repr__, but instead got it from type(self).__name__,

# Concluding thoughts
- An object should be as simple as the requirements dictate—and not a parade of language
features. If the code is for an application, then it should focus on what is
needed to support the end users, not more
- If the code is for a library for other programmers
to use, then it’s reasonable to implement special methods supporting
behaviors that Pythonistas expect.
- To build Pythonic objects, observe how real Python objects behave.
- Fun Quote: Perl doesn’t have an infatuation with enforced privacy. It would prefer that you
stayed out of its living room because you weren’t invited, not because it has a
shotgun. Larry Wall, creator of Perl