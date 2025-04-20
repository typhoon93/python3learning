**Duck typing** Python’s default approach to typing from the beginning. We’ve been studying duck typing since Chapter
1.  
**Goose typing** - The approach supported by abstract base classes (ABCs) since Python 2.6, which relies on runtime
checks of objects against ABCs. Goose typing is a major subject in this chapter.  
**Static typing** - The traditional approach of statically-typed languages like C and Java; supported since Python 3.5
by the typing module, and enforced by external type checkers compliant with PEP 484—Type Hints.

------

# Two Kinds of Protocols

- the sequence protocol: the methods that allow a Python object to behave as a sequence.
- Implementing a full protocol may require several methods, but often it is OK to implement only part of it.

```python
class Vowels:
    def __getitem__(self, item):
        return 'AEIOU'[item]
```
- Implementing __getitem__ is enough to allow retrieving items by index, and also to
support iteration and the in operator. The __getitem__ special method is really the
key to the sequence protocol.
- We expect a sequence to also support len(), by implementing __len__. Vowels has
no __len__ method, but it still behaves as a sequence in some contexts.
- Except in pages about network programming, most uses of the word “protocol” in
the Python documentation refer to these informal interfaces.
- **Dynamic protocol**
The informal protocols Python always had. Dynamic protocols are implicit,
defined by convention, and described in the documentation.
- **Static protocol**
A protocol as defined by PEP 544—Protocols: Structural subtyping (static duck
typing), since Python 3.8. A static protocol has an explicit definition: a typ
ing.Protocol subclass.

- **Monkey Patching: Implementing a Protocol at Runtime** - Monkey patching is dynamically changing a module, class, or function at runtime, to
add features or fix bugs. For example, the gevent networking library monkey patches
parts of Python’s standard library to allow lightweight concurrency without threads
or async/await.2
- When you follow established protocols, you improve your chances
of leveraging existing standard library and third-party code, thanks
to duck typing.
- every Python method starts life as a plain function, and naming the first argument
self is merely a convention.
- Failing fast means raising runtime errors as soon
as possible, for example, rejecting invalid arguments right a the beginning of a function
body.
- When needed - assume it’s a string (EAFP = it’s easier to ask forgiveness than permission).
- An abstract class represents an interface.
- Python doesn’t have an interface keyword. We use abstract base classes (ABCs) to
define interfaces for explicit type checking at runtime—also supported by static type
checkers.
- Python’s ABCs add one major practical advantage:
the **register** class method, which lets end-user code “declare” that a certain class
becomes a “virtual” subclass of an ABC (for this purpose, the registered class must
meet the ABC’s method name and signature requirements, and more importantly,
the underlying semantic contract—but it need not have been developed with any
awareness of the ABC, and in particular need not inherit from it!).
- goose typing entails:
  - Subclassing from ABCs to make it explict that you are implementing a previously
defined interface.
  - Runtime type checking using ABCs instead of concrete classes as the second
argument for isinstance and issubclass.
  - Alex makes the point that inheriting from an ABC is more than implementing the
required methods: it’s also a clear declaration of intent by the developer. That intent
can also be made explicit through registering a virtual subclass.
  - if a component does not implement an
ABC by subclassing—but does implement the required methods—it can always be
registered after the fact so it passes those explicit type checks.
  - Polymorphism: The word "polymorphism" means "many forms", and in programming it refers to methods/functions/operators with the same name that can be executed on many objects or classes.
  - https://www.w3schools.com/Python/python_polymorphism.asp
  - However, even with ABCs, you should beware that excessive use of isinstance
checks may be a code smell—a symptom of bad OO design
  - It’s usually not OK to have a chain of if/elif/elif with isinstance checks performing
different actions depending on the type of object: you should be using polymorphism
for that—i.e., design your classes so that the interpreter dispatches calls to
the proper methods, instead of you hardcoding the dispatch logic in if/elif/elif
blocks.
  - On the other hand, it’s OK to perform an isinstance check against an ABC if you
must enforce an API contract: “Dude, you have to implement this if you want to call
me,” as technical reviewer Lennart Regebro put it. That’s particularly useful in systems
that have a plug-in architecture. Outside of frameworks, duck typing is often
simpler and more flexible than type checks.
  - ABCs are meant to encapsulate very general concepts, abstractions, introduced by a
framework—things like “a sequence” and “an exact number.” [Readers] most likely
don’t need to write any new ABCs, just use existing ones correctly, to get 99.9% of the
benefits without serious risk of misdesign.
  - As the coder of a concrete subclass, you may be able to override
methods inherited from ABCs with more efficient implementations.
For example, __contains__ works by doing a sequential scan
of the sequence, but if your concrete sequence keeps its items sorted,
you can write a faster __contains__ that does a binary search
using the bisect function from the standard library
  - The only reliable way to determine whether an object is iterable is to call iter(obj).
  - ABCs, like descriptors and metaclasses, are tools for building frameworks. Therefore,
only a small minority of Python developers can create ABCs without imposing unreasonable
limitations and needless work on fellow programmers
  - An abstract method is marked with the @abstractmethod decorator, and often its
body is empty except for a docstring
  - Virtual subclasses do not inherit from their registered ABCs, and
are not checked for conformance to the ABC interface at any time,
not even when they are instantiated.
  - inheritance is guided by a special class attribute named __mro__—the
Method Resolution Order. It basically lists the class and its superclasses in the order
Python uses to search for methods.15 If you inspect the __mro__ of TomboList, you’ll
see that it lists only the “real” superclasses—list and object:
>>> TomboList.__mro__
(<class 'tombolist.TomboList'>, <class 'list'>, <class 'object'>)
- Very often at runtime, duck typing is the best approach for type checking: instead of
calling isinstance or hasattr, just try the operations you need to do on the object,
and handle exceptions as needed.
# Static Protocols