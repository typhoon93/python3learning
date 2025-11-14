- It’s essential to recall that the __getattr__ special method is only invoked by the interpreter when the
usual process fails to retrieve an attribute (i.e., when the named attribute cannot be
found in the instance, nor in the class or in its superclasses).
- Flexible Object Creation with __new__
  - We often refer to __init__ as the constructor method, but that’s because we adopted
jargon from other languages. In Python, __init__ gets self as the first argument,
therefore the object already exists when __init__ is called by the interpreter. Also,
__init__ cannot return anything. So it’s really an initializer, not a constructor.
  - When a class is called to create an instance, the special method that Python calls on
that class to construct an instance is __new__.
  - We rarely need to code __new__, because the implementation inherited
from object suffices for the vast majority of use cases.
    ```python
    # pseudocode for object construction
    def make(the_class, some_arg):
        new_object = the_class.__new__(some_arg)
        if isinstance(new_object, the_class):
            the_class.__init__(new_object, some_arg)
        return new_object
    
    ```
  - As a class method, the first argument __new__ gets is the class itself, and the
  remaining arguments are the same that __init__ gets, except for self.
    
      ```python
          class Record:
            def __init__(self, **kwargs):
                self.__dict__.update(kwargs)
            def __repr__(self):
                return f'<{self.__class__.__name__} serial={self.serial!r}>'
      ```
  - The Python standard library provides classes similar to Record,
  where each instance has an arbitrary set of attributes built from
  keyword arguments given to __init__: types.SimpleNamespace,
  argparse.Namespace, and multiprocessing.managers.Name
  space. I wrote the simpler Record class to highlight the essential
  idea: __init__ updating the instance __dict__.
  - When creating instance attribute names from data, there is always
the risk of bugs due to shadowing of class attributes—such as
methods—or data loss through accidental overwriting of existing
instance attributes. These problems may explain why Python dicts
are not like JavaScript objects in the first place.
  - Inside the speakers method, trying to read self.speakers will invoke the property
itself, quickly raising a RecursionError. However, if we read the same data via
self.__dict__['speakers'], Python’s usual algorithm for retrieving attributes is
bypassed, the property is not called, and the recursion is avoided. For this reason,
reading or writing data directly to an object’s __dict__ is a common Python metaprogramming
trick.
- Simple cachine trick
  ```python
  class Event(Record):
    def __init__(self, **kwargs):
      self.__speaker_objs = None
        super().__init__(**kwargs)
    #15 lines omitted...
    @property
    def speakers(self):
      if self.__speaker_objs is None:
        spkr_serials = self.__dict__['speakers']
        fetch = self.__class__.fetch
        self.__speaker_objs = [fetch(f'speaker.{key}')
              for key in spkr_serials]
      return self.__speaker_objs
    ```
- The functools.cached_property decorator caches the result of the method in an
instance attribute with the same name
  - cached_property is a misnomer. The @cached_property
decorator does not create a full-fledged property, it creates a nonoverriding descriptor.
A descriptor is an object that manages the access to an attribute in another class.
  - @cached_property cannot be used as a drop-in replacement to @property if the
decorated method already depends on an instance attribute
with the same name.
  - The main point of this section is that an expression like obj.data does not start the
search for data in obj. The search actually starts at obj.__class__, and only if there
is no property named data in the class, Python looks in the obj instance itself. This
applies to overriding descriptors in general, of which properties are just one example.
  - Attribute access using either dot notation or the built-in functions getattr, hasattr,
and setattr triggers the appropriate special methods listed here. Reading and writing
attributes directly in the instance __dict__ does not trigger these special methods
—and that’s the usual way to bypass them if needed.