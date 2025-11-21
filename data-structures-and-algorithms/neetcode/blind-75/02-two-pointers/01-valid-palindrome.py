"""
https://neetcode.io/solutions/valid-palindrome
https://youtu.be/jJXJ16kPFWg
Valid Palindrome - Explanation

Given a string s, return true if it is a palindrome, otherwise return false.
A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.
Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

Example 1:
Input: s = "Was it a car or a cat I saw?"

Output: true

Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

Example 2:

Input: s = "tab a cat"

Output: false

Explanation: "tabacat" is not a palindrome.

Constraints:

    1 <= s.length <= 1000
    s is made up of only printable ASCII characters.


Recommended Time & Space Complexity

You should aim for a solution with O(n) time and O(1) space, where n is the length of the input string.
"""


def is_palindrome(s: str):
    """
    Simple solution, tc / sc = O(n)
    """
    new_str = ""
    for c in s:
        if c.isalnum():
            new_str += c.lower()
    return new_str == new_str[::-1]


def is_palindrome_optimal(s: str) -> bool:
    """
    TC O(n)
    SC O(1) - pointers
    """
    l, r = 0, len(s) - 1

    while l < r:
        # skip left
        while l < r and not s[l].isalnum():
            l += 1

        # skip right
        while l < r and not s[r].isalnum():
            r -= 1

        if s[l].lower() != s[r].lower():
            return False

        l += 1
        r -= 1

    return True



def run_is_palindrome_tests():
    GREEN = "\033[92m"
    RED   = "\033[91m"
    RESET = "\033[0m"

    test_cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        ("", True),
        (" ", True),
        ("0P", False),
        ("abba", True),
        ("abcba", True),
        ("ab@a", True),
        ("Madam, I'm Adam", True),
        ("No 'x' in Nixon", True),
    ]

    print("Testing is_palindrome_optimal:\n")

    for i, (s, expected) in enumerate(test_cases, 1):
        result = is_palindrome_optimal(s)
        if result == expected:
            print(f"{GREEN}✅ Test {i}: s='{s}' → {result}{RESET}")
        else:
            print(f"{RED}❌ Test {i}: s='{s}' → {result} (expected {expected}){RESET}")


if __name__ == "__main__":
    run_is_palindrome_tests()