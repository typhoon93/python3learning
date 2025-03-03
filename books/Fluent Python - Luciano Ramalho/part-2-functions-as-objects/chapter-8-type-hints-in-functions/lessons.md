- variadic - parameters a variadic function is a function of indefinite arity, i.e., one which accepts a variable number of arguments
- You may very well write an excellent
piece of Python code, with good test coverage and passing tests, but still be unable to
add type hints that satisfy a type checker. That’s OK; just leave out the problematic
type hints and ship it!
- pip install mypy
  - mypy filename.py

- Instead of memorizing such silly rules, use tools like flake8 and blue. flake8 reports on
code styling, among many other issues, and blue rewrites source code according to
(most) rules embedded in the black code formatting tool.
### Using None as a Default

- the parameter plural is annotated as str, and the default value is '', so there is no type conflict. I like that solution, but in other contexts None is a better default
- If the optional  parameter expects a mutable type, then None is the only sensible default
- To have None as the default for the plural parameter, here is what the signature  would look like:
- `def show_count(count: int, singular: str, plural: Optional[str] = None) -> str:`
- When importing types, it’s good practice to use the syntax from typing import X to reduce the length of the function signatures.
- Optional[str] just means: the type of this parameter may be str or NoneType. In the Haskell and Elm  languages, a similar type is named Maybe. 

### Duck typing
Objects have types, but variables (including parameters) are untyped. In practice, it doesn’t matter what the declared type of  the object is, only what operations it actually supports. If I can invoke
birdie.quack(), then birdie is a duck in this context. By definition, duck typing
is only enforced at runtime, when operations on objects are attempted. This
is more flexible than nominal typing, at the cost of allowing more errors at runtime.
### Nominal typing
The view adopted by C++, Java, and C#, supported by annotated Python. Objects
and variables have types. But objects only exist at runtime, and the type checker
only cares about the source code where variables (including parameters) are
annotated with type hints. If Duck is a subclass of Bird, you can assign a Duck
instance to a parameter annotated as birdie: Bird. But in the body of the function,
the type checker considers the call birdie.quack() illegal, because birdie
is nominally a Bird, and that class does not provide the .quack() method. It
doesn’t matter if the actual argument at runtime is a Duck, because nominal typing
is enforced statically. The type checker doesn’t run any part of the program, it
only reads the source code. This is more rigid than duck typing, with the advantage
of catching some bugs earlier in a build pipeline, or even as the code is typed
in an IDE.

## Types usable in annotations

- typing.Any
    - def double(x): **is same as**
    - def double(x: Any) -> Any:
- Simple types and classes: 
  - Simple types like int, float, str, and bytes may be used directly in type hints
  - Concrete classes from the standard library, external packages, or user defined—French Deck, Vector2d, and Duck
  - int Is Consistent-With complex
- typing.Optional and typing.Union
  - Optional: It solves the problem of having None as a default, as in this example from that section:
  - Better Syntax for Optional and Union in Python 3.10: We can write str | bytes instead of Union[str, bytes] since Python 3.10
  - plural: Optional[str] = None # before 
  - plural: str | None = None # after
  - If possible, avoid creating functions that return Union types, as they put an extra burden on the user—forcing them to check the type of the returned value at runtime to know what to do with it.
  - Nested Union types have the same effect as a flattened Union. So these type hints are the same :
    - Union[A, B, Union[C, D, E]]
    - Union[A, B, C, D, E]
- Generic collections, including tuples and mappings
  - list[str] - constrains the list to be of str items
- Abstract base classes
- Generic iterables: Like Sequence, Iterable is best used as a parameter type. It’s too vague as a return type. A function should be more precise about the concrete type it returns.
- Parameterized generics and TypeVar:
  - A parameterized generic is a generic type, written as list[T], where T is a type variable that will be bound to a specific type with each usage. This allows a parameter  type to be reflected on the result type.
    ```python
    from typing import TypeVar
    T = TypeVar('T')
    def sample(population: Sequence[T], size: int) -> list[T]:
        #...
    ```
  - Here are two examples of why I used a type variable in sample:
    - If called with a tuple of type tuple[int, ...]—which is consistent-with Sequence[int]—then the type parameter is int, so the return type is list[int].
    - If called with a str—which is consistent-with Sequence[str]—then the type parameter is str, so the return type is list[str].
  - Why Is TypeVar Needed?: The authors of PEP 484 wanted to introduce type hints by adding
the typing module and not changing anything else in the language.
With clever metaprogramming they could make the [] operator
work on classes like Sequence[T]. But the name of the T variable
inside the brackets must be defined somewhere—otherwise the
Python interpreter would need deep changes to support generic
type notation as special use of []. That’s why the typing.TypeVar
constructor is needed: to introduce the variable name in the current
namespace. Languages such as Java, C#, and TypeScript don’t
require the name of type variable to be declared beforehand, so
they have no equivalent of Python’s TypeVar class.
  - Restricted TypeVar: TypeVar accepts extra positional arguments to restrict the type parameter.
    ```python
    from collections.abc import Iterable
    from decimal import Decimal
    from fractions import Fraction
    from typing import TypeVar
    NumberT = TypeVar('NumberT', float, Decimal, Fraction)
    def mode(data: Iterable[NumberT]) -> NumberT:
        pass
    ```
  - Bounded TypeVar:
    - HashableT = TypeVar('HashableT', bound=Hashable)
    - this means that the type parameter may be Hashable or any subtype of it.
  - A restricted type variable will be set to one of the types named in the TypeVar declaration.
  - A bounded type variable will be set to the inferred type of the expression—as long as the inferred type is consistent-with the boundary declared in the bound=  keyword argument of TypeVar.
  - The typing module includes a predefined TypeVar named AnyStr. It’s defined like this:
    - AnyStr = TypeVar('AnyStr', bytes, str)
    - AnyStr is used in many functions that accept either bytes or str, and return values of the given type.
- typing.Protocols—the key to static duck typing
  - The Protocol type, is similar to interfaces in Go: a protocol type is defined by specifying  one or more methods, and the type checker verifies that those methods are implemented  where that protocol type is required.
  - 
    ```python
    from typing import Protocol, Any
    class SupportsLessThan(Protocol):
        def __lt__(self, other: Any) -> bool: ...
    ```
  - A type T is consistent-with a protocol P if T implements all the methods defined in P,with matching type signatures.
  - 
    ```python 
    from collections.abc import Iterable
    from typing import TypeVar
    from comparable import SupportsLessThan
    LT = TypeVar('LT', bound=SupportsLessThan)
      def top(series: Iterable[LT], length: int) -> list[LT]:
    ```

- typing.Callable: used to annotate callback parameters or callable objects returned by higher-order functions - aka when you pass a function to a function, or it returns a function
  - Callable[[ParamType1, ParamType2], ReturnType]
  - def repl(input_fn: Callable[[Any], str] = input]) -> None:
  - If you need a type hint to match a function with a flexible signature, replace the whole parameter list with ...—like this:
    - Callable[..., ReturnType]
- typing.NoReturn—a good way to end this list
  - This is a special type used only to annotate the return type of functions that never return.
  - Usually, they exist to raise exceptions. There are dozens of such functions in the standard library. 
  - For example, sys.exit() raises SystemExit to terminate the Python process:
    - def exit(__status: object = ...) -> NoReturn: ...

The PEP 484 convention is to prefix each positional-only parameter name with two underscores. Here is the tag signature
again, now in two lines, using the PEP 484 convention:

    def tag(__name: str, *content: str, class_: Optional[str] = None,
        **attrs: str) -> str:

The point of a CI pipeline is to reduce software failures, and
automated tests catch many bugs that are beyond the reach of type hints.