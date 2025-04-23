- with open('mirror.py') as fp:
- The fp variable is still available—with blocks don’t define a new scope, as functions
do.
- When control flow exits the with block in any way, the __exit__ method is invoked
on the context manager object, not on whatever was returned by __enter__.
- The as clause of the with statement is optional. In the case of open, we always need it
to get a reference to the file, so that we can call methods on it.
- When real applications take over standard output, they often want
to replace sys.stdout with another file-like object for a while, then
switch back to the original. The contextlib.redirect_stdout
context manager does exactly that: just pass it the file-like object
that will stand in for sys.stdout.
- Python 3.10 adopted a new, more powerful parser, allowing new
syntax beyond what was possible with the older LL(1) parser. One
syntax enhancement was to allow parenthesized context managers,
like this:
with (
CtxManager1() as example1,
CtxManager2() as example2,
CtxManager3() as example3,
)
# Do This, Then That: else Blocks Beyond if

- for = The else block will run only if and when the for loop runs to completion (i.e.,
not if the for is aborted with a break). 
- while = The else block will run only if and when the while loop exits because the condition
became falsy (i.e., not if the while is aborted with a break).
- try = The else block will run only if no exception is raised in the try block. The official
docs also state: “Exceptions in the else clause are not handled by the preceding
except clauses.”
- EAFP
Easier to ask for forgiveness than permission. This common Python coding style
assumes the existence of valid keys or attributes and catches exceptions if the
assumption proves false. This clean and fast style is characterized by the presence
of many try and except statements. The technique contrasts with the LBYL style
common to many other languages such as C.
- LBYL
Look before you leap. This coding style explicitly tests for pre-conditions before
making calls or lookups. This style contrasts with the EAFP approach and is characterized
by the presence of many if statements. In a multi-threaded environment,
the LBYL approach can risk introducing a race condition between “the looking”
and “the leaping.” For example, the code, if key in mapping: return mapping[key]
can fail if another thread removes key from mapping after the test, but before the
lookup. This issue can be solved with locks or by using the EAFP approach.
- For real-life
uses, don’t forget that Python has math.factorial, written in C without recursion
- Python does not have PTC, so there’s no advantage in writing tail recursive functions.
- If PTC is supported by the language, when the interpreter sees a tail call, it jumps into
the body of the called function without creating a new stack frame, saving memory.

Anki Qs:

1. Do variables define in the context manager block, continue existing after the block finishes - True
2. The with open() as f: -> the as part is optional in a context manager - True
3. What are the two methods we need to implement in a context manager class:
   __enter__ and __exit__ 