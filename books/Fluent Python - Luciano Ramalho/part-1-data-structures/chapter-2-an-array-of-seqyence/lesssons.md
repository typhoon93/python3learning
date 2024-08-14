###Container sequences
Can hold items of different types, including nested containers. Some examples:
list, tuple, and collections.deque.

###Flat sequences
Hold items of one simple type. Some examples: str, bytes, and array.array


###Mutable sequences
For example, list, bytearray, array.array, and collections.deque.
###Immutable sequences
For example, tuple, str, and bytes

###Line Breaks
= In Python code, line breaks are ignored inside pairs of [], {}, or ().
So you can build multiline lists, listcomps, tuples, dictionaries, etc.,
without using the \ line continuation escape, which doesn’t work if
you accidentally type a space after it.
- best to add a comma after the last item on the list, making it easier for the next voder ot add a new item

###Generator Expressions
-To initialize tuples, arrays, and other types of sequences, you could also start from a
listcomp, but a genexp (generator expression) saves memory because it yields items
one by one using the iterator protocol instead of building a whole list just to feed
another constructor.

>>> colors = ['black', 'white']
>>> sizes = ['S', 'M', 'L']
>>> for tshirt in (f'{c} {s}' for c in colors for s in sizes):
... print(tshirt)

The generator expression yields items one by one; a list with all six T-shirt variations
is never produced in this example.

## Tuples

###Tuples as Records
Tuples hold records: each item in the tuple holds the data for one field, and the position
of the item gives its meaning.
You can laverage tuple unpacking instead of using named fields like in dict


###Tuples as Immutable Lists
- The Python interpreter and standard library make extensive use of tuples as immutable
lists, and so should you. This brings two key benefits:
- Clarity
When you see a tuple in code, you know its length will never change.
- Performance
A tuple uses less memory than a list of the same length, and it allows Python
to do some optimizations.
- Tuples with mutable items can be a source of bugs
- an object is only hashable if its value cannot ever change.
- to ensure that a tuple only has immutable items, you can try to hash them
>>> def fixed(o):
... try:
... hash(o)
... except TypeError:
... return False
... return True

##Unpacking Sequences and Iterables

unpacking works with any iterable object as the data source—including iterators, which don’t support index notation
([]).

## Pattern Matching

- The _ symbol is special in patterns: it matches any single item in that position, but it
is never bound to the value of the matched item. Also, the _ is the only variable that
can appear more than once in a pattern
- The optional guard clause starting with if is evaluated only if the pattern matches,
and can reference variables bound in the patter

- This is an important Python API convention: functions or methods that change an object in
place should return None to make it clear to the caller that the receiver was changed,
and no new object was created

## List Alternatives
- if a list contains only numbers, use array.array it is more efficient. A Python array is as lean as a C array.
    - Use memoryview if you do lots of array operations.
    - use numpy for advanced array and matrix operations
    - scipy is built on top of numpy
    - numpy and scipy are foundation for Pandas and scikit-learn
    - Most NumPy and SciPy functions are implemented in C or C++, and can leverage all CPU cores because they release Python’s GIL(Global Interpreter Lock)
- collections.deque is a thread-safe double-ended queue designed for fast inserting and removing from both end
- other queue type built ins you can use:
    - queue
    - multiprocessing
    - asyncio
    - heapq

## Other
- Some objects contain references to other objects; these are called containers.
- key parameter in the sorted(), max(), and min() functions in Python works similarly