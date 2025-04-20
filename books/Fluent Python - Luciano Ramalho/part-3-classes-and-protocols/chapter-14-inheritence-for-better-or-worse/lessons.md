# the super() function
- Consistent use the of the super() built-in function is essential for maintainable
object-oriented Python programs
- Not recommended approach - hardcoding the class method: 
  - because it hardcodes the class, and if it changes, this method needs to change it too
  - super implements logic to handle class hierarchies with multiple inheritecne
```python
class NotRecommended(OrderedDict):
    """This is a counter example!"""
    def __setitem__(self, key, value):
        OrderedDict.__setitem__(self, key, value)
        self.move_to_end(key)
```
- recommended approach:
```python
class LastUpdatedOrderedDict(OrderedDict):
    """Store items in the order they were last updated"""
    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        self.move_to_end(key)
```
- Subclassing built-in types like dict or list or str directly is errorprone
because the built-in methods mostly ignore user-defined
overrides. Instead of subclassing the built-ins, derive your classes
from the collections module using UserDict, UserList, and
UserString, which are designed to be easily extended.
- If you subclass a base class coded in Python, such as
UserDict or MutableMapping, you will not be troubled by this.
- When a method calls super(), it is a cooperative method. Cooperative methods
enable cooperative multiple inheritance. These terms are intentional: in order to work,
multiple inheritance in Python requires the active cooperation of the methods
involved
A noncooperative method can be the cause of subtle bugs. Many
coders reading Example 14-4 may expect that when method
A.pong calls super.pong(), that will ultimately activate Root.pong.
But if B.pong is activated before, it drops the ball. That’s why it is
recommended that every method m of a nonroot class should call
super().m().
- Cooperative methods must have compatible signatures, because you never know
whether A.ping will be called before or after B.ping. The activation sequence
depends on the order of A and B in the declaration of each subclass that inherits from
both.

# Mixin Classes
- A mixin class is designed to be subclassed together with at least one other class in a
multiple inheritance arrangement. A mixin is not supposed to be the only base class
of a concrete class, because it does not provide all the functionality for a concrete
object, but only adds or customizes the behavior of child or sibling classes
- Mixin classes are a convention with no explicit language support in
Python and C++. Ruby allows the explicit definition and use of
modules that work as mixins—collections of methods that may be
included to add functionality to a class. **C#, PHP, and Rust** implement
**traits**, which are also an explicit form of mixin.
- To make its contribution,
a mixin usually needs to appear before other classes in the MRO of a subclass
that uses it. In practice, that means mixins must appear first in the tuple of base
classes in a class declaration
- In modern Python, if a class is intended to define an interface, it should be an explicit
ABC or a typing.Protocol subclass. An ABC should subclass only abc.ABC or other
ABCs. Multiple inheritance of ABCs is not problematic.
- A mixin should never be instantiated, and concrete classes should
not inherit only from a mixin.
- There is no formal way in Python to state that a class is a mixin, so it is highly recommended
that they are named with a Mixin suffix.
- provide aggregate classes to users. A class that is constructed primarily by inheriting from mixins and does not add its
own structure or behavior is called an aggregate class.
- Avoid Subclassing from Concrete Classes
- perhaps the best advice about inheritance is: avoid it if you can. But often, we
don’t have a choice: the frameworks we use impose their own design choices
# Inheritence rulse:
- Favor Object Composition over Class Inheritance
Anki:

Do a CLOZE with multiple inheritence demos __mro__