#Dictionaries and Sets
##Dicts
- Key ordering is preserved as a side effect of a more compact memory layout for
dict in CPython 3.6, which became an official language feature in 3.7.
- Despite its new compact layout, dicts inevitably have a significant memory overhead.
The most compact internal data structure for a container would be an
array of pointers to the items.8 Compared to that, a hash table needs to store
more data per entry, and Python needs to keep at least one-third of the hash table
rows empty to remain efficient
- To save memory, avoid creating instance attributes outside of the __init__
method.
###Dictionary Views

- The dict instance methods .keys(), .values(), and .items() return instances of
classes called dict_keys, dict_values, and dict_items, respectively. These dictionary
views are read-only projections of the internal data structures used in the dict
implementation.
- A view object is a dynamic proxy. If the source dict is updated, you can immediately
see the changes through an existing view

## Sets
- A set is a collection of unique objects. A basic use case is removing duplication
- Example 3-12. Count occurrences of needles in a haystack, both of type set
    ```python
    #finds intersection &
    found = len(needles & haystack)
    #same as:
    found = 0
    for n in needles:
        if n in haystack:
            found += 1
    # same as:
    found = len(set(needles).intersection(haystack))
  ```
- Any one of the preceding examples are capable of searching 1,000 elements in a hay
stack of 10,000,000 items in about 0.3 milliseconds—that’s close to 0.3 microseconds
per element.
- Literal set syntax like {1, 2, 3} is both faster and more readable than calling the
constructor (e.g., set([1, 2, 3])). The latter form is slower because, to evaluate it,
Python has to look up the set name to fetch the constructor, then build a list, and
finally pass it to the constructor. In contrast, to process a literal like {1, 2, 3},
Python runs a specialized BUILD_SET bytecode.10
- There is no special syntax to represent frozenset literals—they must be created by
calling the constructor
- Set elements must be hashable objects.
- Membership testing is very efficient. A set may have millions of elements, but an
element can be located directly by computing its hash code and deriving an index
offset, with the possible overhead of a small number of tries to find a matching
element or exhaust the search
- Sets have a significant memory overhead, compared to a low-level array pointers
to its elements—which would be more compact but also much slower to search
beyond a handful of elements
- Element ordering depends on insertion order, but not in a useful or reliable way.
If two elements are different but have the same hash code, their position depends
on which element is added first
- Adding elements to a set may change the order of existing elements. That’s
because the algorithm becomes less efficient if the hash table is more than twothirds
full, so Python may need to move and resize the table as it grows. When
this happens, elements are reinserted and their relative ordering may change