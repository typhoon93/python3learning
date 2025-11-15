- Metaclasses are powerful, but hard to justify and even harder to get right. Class decorators
solve many of the same problems and are easier to understand.
- For the sake of readability and maintainability, you should probably
avoid the techniques described in this chapter in application
code.
- On the other hand, these are the tools of the trade if you want to
write the next great Python framework.
- Some of the best refactorings are removing code made redundant
by newer and simpler ways of solving the same problems. This
applies to production code as well as books.
- When called with no arguments, the constructor should return a default value of its
type.
  - int(), float(), bool(), str(), list(), dict(), set()
  - (0, 0.0, False, '', [], {}, set())
- A class decorator is a callable that behaves similarly to a function decorator: it gets
the decorated class as an argument, and should return a class to replace the decorated
class. Class decorators often return the decorated class itself, after injecting more
methods in it via attribute assignment.
- Probably the most common reason to choose a class decorator over the simpler
__init_subclass__ is to avoid interfering with other class features, such as inheritance
and metaclasses.

# Import timve vs runtime
- the import statement is not merely a declaration,11 but it actually runs
all the top-level code of a module when it is imported for the first time in the process.
Further imports of the same module will use a cache, and then the only effect will be
binding the imported objects to names in the client module
- the border between “import time” and “runtime”
is fuzzy: the import statement can trigger all sorts of “runtime” behavior. Conversely,
“import time” can also happen deep inside runtime, because the import statement
and the __import__() built-in can be used inside any regular function.
- [Metaclasses] are deeper magic than 99% of users should ever worry about. If you

# metaclasses
- If you wonder whether you need them, you don’t (the people who actually need them know
with certainty that they need them, and don’t need an explanation about why).
- By default, Python classes are instances of type. In other
words, type is the metaclass for most built-in and user-defined classes:
- What I am saying is that str and LineItem are instances of type. They all are subclasses of
object.
- The classes object and type have a unique relationship: object is
an instance of type, and type is a subclass of object. This relationship
is “magic”: it cannot be expressed in Python because either
class would have to exist before the other could be defined. The fact
that type is an instance of itself is also magical.
- Every class is an instance of type,
directly or indirectly, but only metaclasses are also subclasses of type.