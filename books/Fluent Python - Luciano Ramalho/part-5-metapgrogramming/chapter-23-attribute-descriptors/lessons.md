- User-defined functions are descriptors.
We’ll see how the descriptor protocol allows methods to operate as bound or
unbound methods, depending on how they are called.
- a class implementing a __get__, a __set__, or a
__delete__ method is a descriptor. You use a descriptor by declaring instances of it
as class attributes of another class.
- Descriptor is a protocol-based feature; no subclassing is needed to implement
one.