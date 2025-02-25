To understand an assignment in Python, read the righthand side
first: that’s where the object is created or retrieved. After that, the
variable on the left is bound to the object, like a label stuck to it.

Because variables are mere labels, nothing prevents an object from having several
labels assigned to it. When that happens, you have aliasing.

An object’s identity never changes once it has been created; you may think of it as the
object’s address in memory. The **is** operator compares the identity of two objects; the
id() function returns an integer representing its identity.

In practice, we rarely use the **id()** function while programming. Identity checks are
most often done with the is operator, which compares the object IDs, so our code
doesn’t need to call id() explicitly.

Usually we are more interested in object equality than identity.
Checking for None is the only common use case for the is operator.
Most other uses I see while reviewing code are wrong. If you are
not sure, use ==. It’s usually what you want, and also works with
None—albeit not as fast.

Copies Are Shallow by Default

Working with shallow copies is not always a problem, but sometimes you need to
make deep copies (i.e., duplicates that do not share references of embedded objects).
The copy module provides the deepcopy and copy functions that return deep and
shallow copies of arbitrary objects.

Copy and Deepcopy work on OBJECTs (that you can define, not just built in).

Also, a deep copy may be too deep in some cases. For example, objects may refer
to external resources or singletons that should not be copied. You can control the
behavior of both copy and deepcopy by implementing the __copy__() and
__deepcopy__() special methods, as described in the copy module documentation


## Function Parameters as References
The only mode of parameter passing in Python is call by sharing. Call by sharing
means that each formal parameter of the function gets a copy of each reference in the
arguments. In other words, the parameters inside the function become aliases of the
actual arguments.

yYu should avoid mutable objects as default values for parameters. The problem is that each default value is
evaluated when the function is defined—i.e., usually when the module is loaded—and
the default values become attributes of the function object. So if a default value is
a mutable object, and you change it, the change will affect every future call of the
function.

The issue with mutable defaults explains why None is commonly used as the default
value for parameters that may receive mutable values.

## Defensive Programming with Mutable Parameters

Example is this:
```python
def __init__(self, passengers=None):
    if passengers is None:
        self.passengers = []
    else:
        self.passengers = list(passengers)
```

Unless a method is explicitly intended to mutate an object received
as an argument, you should think twice before aliasing the argument
object by simply assigning it to an instance variable in your
class. If in doubt, make a copy. Your clients will be happier. Of
course, making a copy is not free: there is a cost in CPU and memory.
However, an API that causes subtle bugs is usually a bigger
problem than one that is a little slower or uses more resources.

## del and Garbage Collection

Objects are never explicitly destroyed; however, when they become unreachable they
may be garbage-collected.

**del** deletes references, not objects. Python’s garbage collector may discard an object from memory as an indirect result of del, if
the deleted variable was the last reference to the object. Rebinding a variable may also
cause the number of references to an object to reach zero, causing its destruction.

In CPython, the primary algorithm for garbage collection is reference counting.
Essentially, each object keeps count of how many references point to it. As soon as
del and Garbage Collection that refcount reaches zero, the object is immediately destroyed: CPython calls the
__del__ method on the object (if defined) and then frees the memory allocated to the
object.

weak reference does not prevent the target object from being garbage collected. Weak references are useful in caching applications
because you don’t want the cached objects to be kept alive just because they are
referenced by the cache.

## Tricks Python Plays with Immutables

for a tuple t, t[:] does not make a copy, but returns a reference to the same object. You also get a reference to the same tuple if you write
tuple(t).

The same behavior can be observed with instances of str, bytes, and frozenset.
Note that a frozenset is not a sequence, so fs[:] does not work if fs is a frozenset.
But fs.copy() has the same effect: it cheats and returns a reference to the same
object, and not a copy at all,

Example 6-18. String literals may create shared objects
```
>>> s1 = 'ABC'
>>> s2 = 'ABC'
>>> s2 is s1
True
```

The sharing of string literals is an optimization technique called **interning**. CPython
uses a similar technique with small integers to avoid unnecessary duplication of numbers
that appear frequently in programs like 0, 1, –1, etc. Note that CPython does not
intern all strings or integers, and the criteria it uses to do so is an undocumented
implementation detail.

Never depend on str or int interning! Always use == instead of is
to compare strings or integers for equality. Interning is an optimization
for internal use of the Python interpreter.

Every Python object has an identity, a type, and a value. Only the value of an object
may change over time.

If you don’t override __eq__, the method inherited from object
compares object IDs, so the fallback is that every instance of a user-defined class is
considered different.

There is no mechanism in Python to directly destroy an object, and this omission is
actually a great feature: if you could destroy an object at any time, what would happen
to existing references pointing to it?