#Intro
Data classes covered in this chapter provide the necassary __init__, __repr__ and __eq__ methods automatically,
as well as other userful features. The default class will have repr show the object name, eq compare object ids; 
Compare the following:

```python
class Coordinate:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
moscow = Coordinate(55.76, 37.62)
moscow
# <coordinates.Coordinate object at 0x107142f10>
location = Coordinate(55.76, 37.62)
location == moscow
## False
(location.lat, location.lon) == (moscow.lat, moscow.lon)
## True
```
Using namedtuple - here we automatically have a useful repr + meaningful eq

```python
from collections import namedtuple
Coordinate = namedtuple('Coordinate', 'lat lon')
issubclass(Coordinate, tuple)
#True
moscow = Coordinate(55.756, 37.617)
moscow
# Coordinate(lat=55.756, lon=37.617)
moscow == Coordinate(lat=55.756, lon=37.617)
# True
```
The new typing namedtuple provides the same func but with a type annotation;
```python
import typing
Coordinate = typing.NamedTuple('Coordinate', [('lat', float), ('lon', float)])
issubclass(Coordinate, tuple)
#True
typing.get_type_hints(Coordinate)
#{'lat': <class 'float'>, 'lon': <class 'float'>}
```

- Class decorators are covered in Chapter 24, “Class Metaprogramming,” along with metaclasses. Both are ways
of customizing class behavior beyond what is possible with inheritance.
- A key difference between these class builders is that collections.namedtuple and
typing.NamedTuple build tuple subclasses, therefore the instances are immutable. 
- By default, @dataclass produces mutable classes. But the decorator accepts a keyword argument frozen When frozen=True, the class will
raise an exception if you try to assign a value to a field after the instance is initialized.
- Only typing.NamedTuple and dataclass support the regular class statement syntax,
making it easier to add methods and docstrings to the class you are creating.

## Classic Named Tuples
- collections.namedtuple function is a factory that builds subclasses of tuple
enhanced with field names, a class name, and an informative __repr__.
How to define a named tuple
```python
from collections import namedtuple
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
tokyo
# City(name='Tokyo', country='JP', population=36.933, coordinates=(35.689722,139.691667))
tokyo.population
#36.933
tokyo.coordinates
#(35.689722, 139.691667)
tokyo[1]
#'JP'
```
 - ._asdict() returns a dict built from the named tuple instance.

## Typed Named Tuples
```python
from typing import NamedTuple
class Coordinate(NamedTuple):
    lat: float
    lon: float
    reference: str = 'WGS84'
```
 - Every instance field must be annotated with a type.
 - The reference instance field is annotated with a type and a default value
 - The first thing you need to know about type hints is that they are not enforced at all
by the Python bytecode compiler and interpreter
 - The type hints are intended primarily to support third-party type checkers, like Mypy
or the PyCharm IDE built-in type checker. These are static analysis tools: they check
Python source code “at rest,” not running code.
 - To see the effect of type hints, you must run one of those tools on your code—like a
linter.