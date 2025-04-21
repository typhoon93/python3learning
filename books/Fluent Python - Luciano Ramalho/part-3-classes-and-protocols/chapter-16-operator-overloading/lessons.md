- Operators that appear between operands, like 1 + rate, are infix operators.
- Operator overloading allows user-defined objects to interoperate with infix operators
such as + and |, or unary operators like - and ~.
- function invocaton (()), attribute access (.), and item access/slicing ([]) are also operators in Python,
but this chapter covers unary and infix operators.
- We cannot change the meaning of the operators for the built-in types.
- We cannot create new operators, only overload existing ones.
- A few operators can’t be overloaded: is, and, or, not (but the bitwise &, |, ~, can).
- Use whatever logic makes sense in
your class, but stick to the general rule of operators: always return a new object  
- Special methods implementing unary or infix operators should
never change the value of the operands. Expressions with such
operators are expected to produce results by creating new objects.
Only augmented assignment operators may change the first
operand (self),
- Given an expression
a + b, the interpreter will perform these steps (also see Figure 16-1):
  1. If a has __add__, call a.__add__(b) and return result unless it’s NotImplemented.
  2. If a doesn’t have __add__, or calling it returns NotImplemented, check if b has
  __radd__, then call b.__radd__(a) and return result unless it’s NotImplemented.
  3. If b doesn’t have __radd__, or calling it returns NotImplemented, raise TypeError
  with an unsupported operand types message.
- Do not confuse NotImplemented with NotImplementedError. The
first, NotImplemented, is a special singleton value that an infix
operator special method should return to tell the interpreter it
cannot handle a given operand. In contrast, NotImplementedError
is an exception that stub methods in abstract classes may raise to
warn that subclasses must implement them.
- if an operator special method cannot return a valid result because of type
incompatibility, it should return NotImplemented and not raise TypeError. By
returning NotImplemented, you leave the door open for the implementer of the other
operand type to perform the operation when Python tries the reversed method call.

# using @ as infix operator
- The @ sign is well-known as the prefix of function decorators, but since 2015, it can
also be used as an infix operator. For years, the dot product was written as
numpy.dot(a, b) in NumPy
- Today, you can write a @ b to
compute the dot product of two NumPy arrays.
- The @ operator is supported by the special methods __matmul__, __rmatmul__, and
__imatmul__, named for “matrix multiplication.”
- The same set of methods is used in forward and reverse operator calls. The rules
are summarized in Table 16-2. For example, in the case of ==, both the forward
and reverse calls invoke __eq__, only swapping arguments; and a forward call to
__gt__ is followed by a reverse call to __lt__ with the arguments swapped.
- In the case of == and !=, if the reverse method is missing, or returns NotImplemen
ted, Python compares the object IDs instead of raising TypeError.
- The “Zen of Python” says:
In the face of ambiguity, refuse the temptation to guess.
- Our Vector class already supports the augmented assignment operators += and *=.
That’s because augmented assignment works with immutable receivers by creating
new instances and rebinding the lefthand variable.
- If a class does not implement the in-place operators listed in Table 16-1, the augmented
assignment operators work as syntactic sugar: a += b is evaluated exactly as a =
a + b. That’s the expected behavior for immutable types, and if you have __add__,
then += will work with no additional code.
- if you do implement an in-place operator method such as __iadd__, that
method is called to compute the result of a += b. As the name says, those operators
are expected to change the lefthand operand in place, and not create a new object as
the result.
- Writing my_list + x, you can only
concatenate one list to another list, but if you write my_list +=
x, you can extend the lefthand list with items from any iterable x
on the righthand side. This is how the list.extend() method
works: it accepts any iterable argument.
- A clever example of operator overloading appeared in the pathlib package, added in
Python 3.4. Its Path class overloads the / operator to build filesystem paths from
strings, as shown in this example from the documentation:
p = Path('/etc')  
q = p / 'init.d' / 'reboot'
q  
PosixPath('/etc/init.d/reboot')
- Go
doesn’t have operator overloading, but Rust does.