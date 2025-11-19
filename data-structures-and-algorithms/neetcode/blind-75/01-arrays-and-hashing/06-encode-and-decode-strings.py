"""
https://neetcode.io/solutions/encode-and-decode-strings


Problem Link
Description

Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode
Example 1:
Input: ["neet","code","love","you"]
Output:["neet","code","love","you"]

Example 2:
Input: ["we","say",":","yes"]
Output: ["we","say",":","yes"]

Constraints:
    0 <= strs.length < 100
    0 <= strs[i].length < 200
    strs[i] contains only UTF-8 characters.



Recommended Time & Space Complexity
You should aim for a solution with O(m) time for each encode() and decode() call and O(m+n) space, where m is the sum of lengths of all the strings and n is the number of strings.

"""

# Original solution
from typing import List


def encode(strs: List[str]) -> str:
    """
    Due to how string concat works in python, TC here is O(n**2)
    Strictly speaking in Python, string concatenation in a loop is costly:
    Each res += ... creates a new string and copies over the previous contents of res.
    On iteration 1 you copy ~O(chunk1), on iteration 2 you copy ~O(chunk1 + chunk2), ..., so overall you get about:
    O(1+2+⋯+M)=O(M**2)

    So the time complexity is O(M²) with this exact implementation.
    """
    res = ""
    for s in strs:
        res += str(len(s)) + "#" + s

    return res


def encode_optimized(strs: List[str]) -> str:
    """
    Due to using join here we get O(n), SC remains O(n)
    """
    new_list = []
    for s in strs:
        new_list.append(f"{len(s)}#")
        new_list.append(s)
    res = "".join(new_list)
    return res


def decode(s: str) -> List[str]:
    """
    o(n) sc ant tc;
    we need the # to remove ambiguity, we cannot just prepend the length since a string may be longer than 1 digit;
    aka if a string is 12 len, how do you know when to stop catching numbers from the start, esp if the string starts with a number?
    # is a tool to stop ambiguity.
    """
    res = []
    i = 0
    while i < len(s):
        j = i
        while s[j] != "#":
            j += 1
        length = int(s[i:j])
        i = j + 1
        j = i + length
        res.append(s[i:j])
        i = j
    return res

def run_encode_decode_tests():
    GREEN = "\033[92m"
    RED   = "\033[91m"
    RESET = "\033[0m"

    test_cases = [
        (["lint", "code", "love", "you"]),
        (["", "a", ""]),
        (["#", "##", "###"]),
        (["123", "001", "10#abc"]),
        (["", "", "", ""]),
        (["a" * 1000, "b" * 500]),
        (["weird#string", "another#one#here"]),
        ([" "]),                   # single space
        (["", " ", "   "]),        # mixing blank and spaces
        ([]),                      # empty list
    ]

    print("Testing encode_optimized + decode:\n")

    for i, strs in enumerate(test_cases, 1):
        encoded = encode_optimized(strs)
        decoded = decode(encoded)

        if decoded == strs:
            print(f"{GREEN}✅ Test {i}: strs={strs} → PASS{RESET}")
        else:
            print(f"{RED}❌ Test {i}:\n  original={strs}\n  encoded={encoded}\n  decoded={decoded}{RESET}")


if __name__ == "__main__":
    run_encode_decode_tests()

