Basics:
-The identity of a character—its code point—is a number from 0 to 1,114,111
(base 10), shown in the Unicode standard as 4 to 6 hex digits with a “U+” prefix,
from U+0000 to U+10FFFF
-Converting from code points to bytes is encoding; converting from bytes to code
points is decoding.
- Garbled characters are known as gremlins or mojibake (文字化け—Japanese for “transformed text”).
Handling errors:
```python
city = 'São Paulo'
city.encode('utf_8')
b'S\xc3\xa3o Paulo'
city.encode('utf_16')
b'\xff\xfeS\x00\xe3\x00o\x00 \x00P\x00a\x00u\x00l\x00o\x00'
city.encode('iso8859_1')
b'S\xe3o Paulo'
city.encode('cp437')
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# File "/.../lib/python3.4/encodings/cp437.py", line 12, in encode
# return codecs.charmap_encode(input,errors,encoding_map)
# UnicodeEncodeError: 'charmap' codec can't encode character '\xe3' in
# position 1: character maps to <undefined>
city.encode('cp437', errors='ignore')
b'So Paulo'
city.encode('cp437', errors='replace')
b'S?o Paulo'
city.encode('cp437', errors='xmlcharrefreplace')
b'S&#227;o Paulo'
```

- if you cannot open a specific python file due to encoding, add the encoding of the file as a magic comment:
- # coding: cp1252
- Code that has to run on multiple machines or on multiple occasions should never depend on encoding defaults. Always pass an
explicit encoding= argument when opening text files, because the default may change from one machine to the next, or from one day
to the next.
- The 'rb' flag opens a file for reading in binary mode. (in open function). Ordinary code should only use binary mode to open binary files, like raster
images.
- Keyboard drivers usually generate composed characters, so text typed by users will be
in NFC by default. However, to be safe, it may be good to normalize strings with
normalize('NFC', user_text) before saving. NFC is also the normalization form
recommended by the W3C in “Character Model for the World Wide Web: String
Matching and Searching”.
- NFKC and NFKD normalization cause data loss and should be
applied only in special cases like search and indexing, and not for
permanent storage of text.
- There are nearly 300 code points for which str.casefold() and str.lower() return
different results.
- Case folding is essentially converting all text to lowercase, with some additional
transformations. It is supported by the str.casefold() method.
- If you work with text in many languages, a pair of functions like nfc_equal and
fold_equal in Example 4-13 are useful additions to your toolbox.
- 
```python
from unicodedata import normalize
def nfc_equal(str1, str2):
    return normalize('NFC', str1) == normalize('NFC', str2)
def fold_equal(str1, str2):
    return (normalize('NFC', str1).casefold() ==
normalize('NFC', str2).casefold())
```
- The Google Search secret sauce involves many tricks, but one of them apparently is
ignoring diacritics (e.g., accents, cedillas, etc.), at least in some contexts.