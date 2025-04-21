- Whenever Python needs to iterate over an object x, it automatically calls iter(x).
- The iter built-in function:
1. Checks whether the object implements __iter__, and calls that to obtain an
iterator.
2. If __iter__ is not implemented, but __getitem__ is, then iter() creates an iterator
that tries to fetch items by index, starting from 0 (zero).
3. If that fails, Python raises TypeError, usually saying 'C' object is not itera
ble, where C is the class of the target object.
4. Python’s iteration machinery will
call __getitem__ with indexes starting from 0, and will take an IndexError as a
signal that there are no more items.
- That is why all Python sequences are iterable: by definition, they all implement
__getitem__.
- As of Python 3.10, the most accurate way to check whether an
object x is iterable is to call iter(x) and handle a TypeError exception
if it isn’t.

## Using iter with a Callable
We can call iter() with two arguments to create an iterator from a function or any
callable object. In this usage, the first argument must be a callable to be invoked
repeatedly (with no arguments) to produce values, and the second argument is a sentinel:
a marker value which, when returned by the callable, causes the iterator to raise
StopIteration instead of yielding the sentinel.
```python
"""sentinel is 1 - equals stopiter exception;"""
from random import randint  
def d6():
     return randint(1, 6)    
d6_iter = iter(d6, 1)
# d6_iter
# <callable_iterator object at 0x10a245270>
for roll in d6_iter:
     print(roll)
    
# 4
# 3
# 6
# 3
```
- StopIteration signals that the iterator is exhausted. This exception is handled internally
by the iter() built-in that is part of the logic of for loops and other iteration
contexts like list comprehensions, iterable unpacking, etc.
- it’s not possible to “reset” an iterator. If you need to start
over, you need to call iter() on the iterable that built the iterator in the first place.
- Don’t Make the Iterable an Iterator for Itself
- To “support multiple traversals,” it must be possible to obtain multiple independent
iterators from the same iterable instance, and each iterator must keep its own internal
state, so a proper implementation of the pattern requires each call to iter(my_itera
ble) to create a new, independent, iterator
- Python incorporated the yield keyword from Barbara Liskov’s CLU language, so we
don’t need to “generate by hand” the code to implement iterators.

## How a Generator Works
- Any Python function that has the yield keyword in its body is a generator function: a
function which, when called, returns a generator object. In other words, a generator
function is a generator factory.
- Generator expressions are syntactic sugar: they can always be replaced by generator
functions, but sometimes are more convenient.
- When a generator expression is passed as the single argument to a
function or constructor, you don’t need to write a set of parentheses
for the function call and another to enclose the generator
expression.
- To create a generator, we don’t implement
__next__. Instead, we use the yield keyword to make a generator function,
which is a factory of generator objects
- In the case of all and any, there is an important optimization functools.reduce
does not support: all and any short-circuit—i.e., they stop consuming the iterator as
soon as the result is determined.


## Classic Coroutines

- Generators able to consume and return values are coroutines, our next topic.
- classic coroutines still work as originally designed, although they
are no longer supported by asyncio.
- Generators produce data for iteration
- Coroutines are consumers of data
- To keep your brain from exploding, don’t mix the two concepts together
- Coroutines are not related to iteration
- Note: There is a use of having `yield` produce a value in a coroutine, but it’s not
tied to iteration.12

```python
from collections.abc import Generator
def averager() -> Generator[float, float, None]:
    total = 0.0
    count = 0
    average = 0.0
    while True:
        term = yield average
        total += term
        count += 1
        average = total/count

coro_avg = averager()
next(coro_avg)
coro_avg.send(10)
coro_avg.send(30)
coro_avg.send(5)
```
0.0
10.0
20.0
15.0
