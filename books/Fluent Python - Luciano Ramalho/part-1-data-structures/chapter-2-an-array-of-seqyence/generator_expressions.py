symbols = "$¢£¥€¤"

t = tuple(ord(symbol) for symbol in symbols)
print(t)

import array

a = array.array("I", (ord(symbol) for symbol in symbols))
print(a)
