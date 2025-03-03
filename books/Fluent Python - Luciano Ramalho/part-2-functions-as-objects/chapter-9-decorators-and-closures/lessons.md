closures— is what we get when functions capture variables defined outside of their bodies.


Aside from their application in decorators, closures are also essential for any type of
programming using callbacks, and for coding in a functional style when it makes
sense

Powerful decorators in the standard library: @cache, @lru_cache, and @single
dispatch

### When Python Executes Decorators
they run right after the decorated function is
defined. That is usually at import time (i.e., when a module is loaded by Python).


The main point of our example is to emphasize that function decorators are **executed**
**as soon as the module is imported**, but the **decorated** functions only run when they
are **explicitly invoked**. This highlights the difference between what Pythonistas call
import time and runtime.

Similar decorators (to the code in "decorators-exuction-time-demo.py") are used in many Python
frameworks to add functions to some central registry—for example, a registry mapping
URL patterns to functions that generate HTTP responses. Such registration decorators
may or may not change the decorated function.

Most decorators do change the decorated function. They usually do it by defining an
inner function and returning it to replace the decorated function.

# Scopes
- The module global scope -Made of names assigned to values outside of any class or function block
- The f3 function local scope - Made of names assigned to values as parameters, or directly in the body of the function.
- There is one other scope where variables can come from, which we call **nonlocal** and is fundamental for closures;

# Closers
a closure is a function—let’s call it f—with an extended scope that encompasses
variables referenced in the body of f that are not global variables or local variables
of f. Such variables must come from the local scope of an outer function that
encompasses f.

It does not matter whether the function is anonymous or not; what matters is that it
can access nonglobal variables that are defined outside of its body.

Example in notebook in this folder.

A closure is a function that retains the bindings of the free variables
that exist when the function is defined, so that they can be used later when the function
is invoked and the defining scope is no longer available.

Note that the only situation in which a function may need to deal with external variables
that are nonglobal is when it is nested in another function and those variables
are part of the local scope of the outer function.


nonlocal- lets you declare a variable as a free variable even when it is assigned within the function.
If a new value is assigned to a nonlocal variable, the binding stored in the closure is
changed. A correct implementation of our newest make_averager looks like

```python
def make_averager():
    count = 0
    total = 0
    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count
    return averager
```

## Variable Lookup Logic

- If there is a global x declaration, x comes from and is assigned to the x global
variable module. (Python does not have a program global scope, only module global scopes.)
- If there is a nonlocal x declaration, x comes from and is assigned to the x local
variable of the nearest surrounding function where x is defined.
- If x is a parameter or is assigned a value in the function body, then x is the local
variable.
- If x is referenced but is not assigned and is not a parameter: —x will be looked up in the local scopes of the surrounding function bodies (nonlocal scopes).
- If not found in surrounding scopes, it will be read from the module global scope.
- If not found in the global scope, it will be read from __builtins__.__dict__.

## Decorators

In Design Patterns by Gamma et al., the short description of the
decorator pattern starts with: “Attach additional responsibilities to
an object dynamically.” Function decorators fit that description.
But at the implementation level, Python decorators bear little
resemblance to the classic decorator described in the original
Design Patterns work.

### Memoization with functools.cache
memoization - is a computer science term vaguely related to “memorization,” but
not the same. In computing, memoization or memoisation is an optimization technique used primarily to speed up computer programs by storing the results of expensive function calls to pure functions and returning the cached result when the same inputs occur again


To make sense of stacked decorators, recall that the @ is syntax
sugar for applying the decorator function to the function below it.
If there’s more than one decorator, they behave like nested function
calls. This:
@alpha
@beta
def my_fn():
...
is the same as this:
my_fn = alpha(beta(my_fn))


## singledispatch

The functools.singledispatch decorator allows different modules to contribute to
the overall solution, and lets you easily provide specialized functions even for types
that belong to third-party packages that you can’t edit. If you decorate a plain function
with @singledispatch, it becomes the entry point for a generic function: a group
of functions to perform the same operation in different ways, depending on the type
of the first argument. This is what is meant by the term single dispatch. If more arguments
were used to select the specific functions, we’d have multiple dispatch.