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
- The standard way to sort non-ASCII text in Python is to use the locale.strxfrm
function which - if you need non-ASCII sort check it out. Different system may render different results so do extensive tests if you need to use it.
  - There are some caveats, though:
    - Because locale settings are global, calling setlocale in a library is not recommended.
Your application or framework should set the locale when the process
starts, and should not change it afterward. 
    - The locale must be installed on the OS, otherwise setlocale raises a
locale.Error: unsupported locale setting exception. 
    - You must know how to spell the locale name. 
    - The locale must be correctly implemented by the makers of the OS.
- A simpler solution is the **pyuca** library, available on PyPI.
- The unicodedata module has functions to retrieve character metadata, including uni
codedata.name():
  - You can use the name() function to build apps that let users search for characters by
name.
    - check cf.py for usage
  - unicodedata.numeric() can be used to see if a char is numeric
- The re module is not as savvy about Unicode so it may miss non standard unicode numbers
- If you build a regular expression with bytes, patterns such as \d and \w only match
ASCII characters; in contrast, if these patterns are given as str, they match Unicode
digits or letters beyond ASCII
- For str regular expressions, there is a re.ASCII flag that makes \w, \W, \b, \B, \d, \D,
\s, and \S perform ASCII-only matching
- The GNU/Linux kernel is not Unicode savvy, so in the real world you may find filenames
made of byte sequences that are not valid in any sensible encoding scheme,
and cannot be decoded to str. File servers with clients using a variety of OSes are
particularly prone to this problem.
- In order to work around this issue, all os module functions that accept filenames or
pathnames take arguments as str or bytes. If one such function is called with a str
argument, the argument will be automatically converted using the codec named by
sys.getfilesystemencoding(), and the OS response will be decoded with the same
codec. This is almost always what you want, in keeping with the Unicode sandwich
best practice.
- To help with manual handling of str or bytes sequences that are filenames or pathnames,
the os module provides special encoding and decoding functions os.fsen
code(name_or_path) and os.fsdecode(name_or_path). Both of these functions
accept an argument of type str, bytes, or an object implementing the os.PathLike
interface since Python 3.6
- Unicode is a deep rabbit hole.