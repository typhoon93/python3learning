- NumPy and SciPy are the tools you need for real-world vector math. The PyPI package
gensim, by Radim Řehůřek, implements vector space modeling for natural language
processing and information retrieval, using NumPy and SciPy.
- the best practice for a sequence constructor
is to take the data as an iterable argument in the constructor, like all built-in
sequence types do.
```text
>>> Vector([3.1, 4.2])
Vector([3.1, 4.2])
>>> Vector((3, 4, 5))
Vector([3.0, 4.0, 5.0])
>>> Vector(range(10))
Vector([0.0, 1.0, 2.0, 3.0, 4.0, ...])
```

- When a Vector has more than six components, the string produced
by repr() is abbreviated with ... as seen in the last line of
Example 12-1. This is crucial in any collection type that may contain
a large number of items, because repr is used for debugging—
and you don’t want a single large object to span thousands of lines
in your console or log.

## Protocols and Duck Typing
- In the context of object-oriented programming, a protocol is an informal interface,
defined only in documentation and not in code.
- For example, the sequence protocol in Python entails just the __len__ and __getitem__ methods.
- Any class that implements those methods with the standard signature and semantics can be used
anywhere a sequence is expected.
- An experienced Python coder will look at an object that has __len__ and __getitem__ and understand that it is a
sequence, even if it subclasses object.
- We say it is a sequence because it behaves like one, and that is what matters.
- Because protocols are informal and unenforced, you can often get away with implementing
just part of a protocol, if you know the specific context where a class will be used
- For example, to support iteration, only __getitem__ is required; there is no need to provide __len__.
- supporting the sequence protocol is really easy if you can delegate to a sequence attribute in your object, like our self._compo
nents array. These __len__ and __getitem__ one-liners are a good start
```python
class Vector:
# many lines omitted
# ...
    def __len__(self):
        return len(self._components)
    def __getitem__(self, index):
        return self._components[index] 
```
- the built-in sequence types: every one of them, when sliced, produces a new
instance of its own type, and not of some other type.

## Dynamic attribute access

- The __getattr__ method is invoked by the interpreter when attribute lookup fails.
- In simple terms, given the expression my_obj.x, Python checks if the my_obj instance
has an attribute named x; if not, the search goes to the class (my_obj.__class__), and
then up the inheritance graph.2 If the x attribute is not found, then the __getattr__
method defined in the class of my_obj is called with self and the name of the
attribute as a string (e.g., 'x').
- example below lists our __getattr__ method. Essentially it checks whether the
attribute being sought is one of the letters xyzt and if so, returns the corresponding
vector component.

```python

__match_args__ = ('x', 'y', 'z', 't')
def __getattr__(self, name):
    cls = type(self)
    try:
        pos = cls.__match_args__.index(name)
        except ValueError:
            pos = -1
        if 0 <= pos < len(self._components):
            return self._components[pos]
        msg = f'{cls.__name__!r} object has no attribute {name!r}'
        raise AttributeError(msg)
```

- __setattr__ example:
```python

def __setattr__(self, name, value):
    cls = type(self)
    if len(name) == 1:
        if name in cls.__match_args__:
            error = 'readonly attribute {attr_name!r}'
        elif name.islower():
           error = "can't set attributes 'a' to 'z' in {cls_name!r}"
        else:
            error = ''
        if error:
            msg = error.format(cls_name=cls.__name__, attr_name=name)
            raise AttributeError(msg)
    super().__setattr__(name, value)
```

- The super() function provides a way to access methods of superclasses
dynamically, a necessity in a dynamic language supporting
multiple inheritance like Python. It’s used to delegate some task
from a method in a subclass to a suitable method in a superclass, as
seen above
- Note that we are not disallowing setting all attributes, only single-letter
- very often when you implement __getattr__, you need
to code __setattr__ as well, to avoid inconsistent behavior in your objects.

# Hashing and a Faster ==

- Reducing functions—reduce, sum, any, all—produce a single aggregate
result from a sequence or from any finite iterable object.
- So far we’ve seen that functools.reduce() can be replaced by sum(), but now let’s
properly explain how it works. The key idea is to reduce a series of values to a single
value. The first argument to reduce() is a two-argument function, and the second
argument is an iterable.
- Let’s say we have a two-argument function fn and a list lst.
When you call reduce(fn, lst), fn will be applied to the first pair of elements—
fn(lst[0], lst[1])—producing a first result, r1. Then fn is applied to r1 and the
next element—fn(r1, lst[2])
- producing a second result, r2. Now fn(r2,
lst[3]) is called to produce r3 … and so on until the last element, when a single
result, rN, is returned.
- The zip function is named after the zipper fastener because the
physical device works by interlocking pairs of teeth taken from
both zipper sides, a good visual analogy for what zip(left,
right) does. No relation to compressed files.

## ZIP
- zip stops without warning when one of the iterables is exhausted.
- 3.10 adds strict option to exit on error
- The itertools.zip_longest function behaves differently: it uses an optional
fillvalue (None by default) to complete missing values so it can generate tuples
until the last iterable is exhausted.

In the Python documentation, you can often tell when a protocol is being discussed
when you see language like “a file-like object.” This is a quick way of saying “something
that behaves sufficiently like a file, by implementing the parts of the file interface
that are relevant in the context.”  

if you want to use a type checker to verify your protocol implementations,
then a stricter definition of protocol is required. That’s what typing.Pro
tocol provides

overloading - methods that do different
things depending on their arguments' types