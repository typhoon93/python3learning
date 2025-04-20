
- If you want to learn about @overload by reading code, typeshed has hundreds of
examples
- For runtime checking of JSON-like structures using type hints, check out the
pydantic package on PyPI.
- TypedDict exists only for
the benefit of type checkers, and has no runtime effect.
- Without a type checker, TypedDict is as useful as comments: it may help people read
the code, but that’s it. In contrast, the class builders from Chapter 5 are useful even if
you don’t use a type checker, because at runtime they generate or enhance a custom
class that you can instantiate.
- The point of this demonstration: when handling data with a dynamic structure, such
as JSON or XML, TypedDict is absolutely not a replacement for data validation at
runtime. For that, use pydantic.
- Casts are used to silence spurious type checker warnings and give the type checker a
little help when it can’t quite understand what is going on.
- Don’t get too comfortable using cast to silence Mypy, because
Mypy is usually right when it reports an error. If you are using
cast very often, that’s a code smell. Your team may be misusing
type hints, or you may have low-quality dependencies in your
codebase.
- At import time, Python reads the type hints in functions, classes, and modules, and
stores them in attributes named __annotations__.

# Problems with Annotations at Runtime
- The increased use of type hints raised two problems:
  - Importing modules uses more CPU and memory when many type hints are used.
  - Referring to types not yet defined requires using strings instead of actual types.
- Since the class object is not defined until Python completely evaluates the
class body, type hints must use the name of the class as a string. Here is an example: