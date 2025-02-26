## Higher-Order Functions

A function that takes a function as an argument or returns a function as the result is a higher-order function. One
example is map

## Modern Replacements for map, filter, and reduce

The map and filter functions are still built-ins in Python 3, but since the introduction of list comprehensions and
generator expressions, they are not as important. A listcomp or a genexp does the job of map and filter combined, but is
more readable. Examples:

```
>>> list(map(factorial, range(6)))
[1, 1, 2, 6, 24, 120]
>>> [factorial(n) for n in range(6)]
[1, 1, 2, 6, 24, 120]
>>> list(map(factorial, filter(lambda n: n % 2, range(6))))
[1, 6, 120]
>>> [factorial(n) for n in range(6) if n % 2]
[1, 6, 120]
```

In Python 3, map and filter return generators—a form of iterator—so their direct
substitute is now a generator expression (in Python 2, these functions returned lists,
therefore their closest alternative was a listcomp).

The reduce function was demoted from a built-in in Python 2 to the functools
module in Python 3. Its most common use case, summation, is better served by the
sum built-in available since Python 2.3 was released in 2003. This is a big win in terms
of readability and performance.
```text
Example 7-6. Sum of integers up to 99 performed with reduce and sum
>>> from functools import reduce
>>> from operator import add
>>> reduce(add, range(100))
4950
>>> sum(range(100))

```


### Other reducing built-ins are all and any:
all(iterable)  
Returns True if there are no falsy elements in the iterable; all([]) returns True.
any(iterable)  
Returns True if any element of the iterable is truthy; any([]) returns False.

## Anonymous Functions

The best use of anonymous functions is in the context of an argument list for a
higher-order function

Outside the limited context of arguments to higher-order functions, anonymous
functions are rarely useful in Python. The syntactic restrictions tend to make nontrivial
lambdas either unreadable or unworkable. If a lambda is hard to read, I strongly
advise you follow Fredrik Lundh’s refactoring advice. (https://docs.python.org/3/howto/functional.html)

The lambda syntax is just syntactic sugar: a lambda expression creates a function
object just like the def statement. That is just one of several kinds of callable objects
in Python. The following section reviews all of them.

# The Nine Flavors of Callable Objects
The call operator **()** may be applied to other objects besides functions. To determine
whether an object is callable, use the **callable()** built-in function.

### User-defined functions
Created with def statements or lambda expressions.
### Built-in functions
A function implemented in C (for CPython), like len or time.strftime.
### Built-in methods
Methods implemented in C, like dict.get.
### Methods
Functions defined in the body of a class.
### Classes
When invoked, a class runs its __new__ method to create an instance, then
__init__ to initialize it, and finally the instance is returned to the caller. Because
there is no new operator in Python, calling a class is like calling a function.2
### Class instances
If a class defines a __call__ method, then its instances may be invoked as functions—
that’s the subject of the next section.
### Generator functions
Functions or methods that use the yield keyword in their body. When called,
they return a generator object.
### Native coroutine functions
Functions or methods defined with async def. When called, they return a
coroutine object. Added in Python 3.5.
### Asynchronous generator functions
Functions or methods defined with async def that have yield in their body.
When called, they return an asynchronous generator for use with async for.
Added in Python 3.6.  

Generators, native coroutines, and asynchronous generator functions are unlike
other callables in that their return values are never application data, but objects that
require further processing to yield application data or perform useful work

User-Defined Callable Types

Implementing a __call__ is all it takes to make a python object behave like a function:

```python
import random

class BingoCage:    
    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)
    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')
        
    def __call__(self):
        return self.pick()

```


## Operator module

- **itemgetter** , gets and item from an iterator the specified number
- If you pass multiple index arguments to itemgetter, the function it builds will return
tuples with the extracted values, which is useful for sorting on multiple keys:
- Because itemgetter uses the [] operator, it supports not only sequences but also
mappings and any class that implements __getitem__.
- A sibling of itemgetter is **attrgetter**, which creates functions to extract **object**
**attributes** by name. If you pass attrgetter several attribute names as arguments, it
also returns a tuple of values.
- **methodcaller** - It is somewhat similar to attrgetter and itemgetter in that it creates a function on the
fly. The function it creates calls a method by name on the object given as argument

## functools
- functools.partial - given a callable, it produces a new callable with some of the arguments of the original
callable bound to predetermined values. This is useful to adapt a function that takes
one or more arguments to an API that requires a callback with fewer arguments
```text
>>> from operator import mul
>>> from functools import partial
>>> triple = partial(mul, 3)
>>> triple(7)
21
>>> list(map(triple, range(1, 10)))
[3, 6, 9, 12, 15, 18, 21, 24, 27]

```
- partial takes a callable as first argument, followed by an arbitrary number of positional
and keyword arguments to bind.