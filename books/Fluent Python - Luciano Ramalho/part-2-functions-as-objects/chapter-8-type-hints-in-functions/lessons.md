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