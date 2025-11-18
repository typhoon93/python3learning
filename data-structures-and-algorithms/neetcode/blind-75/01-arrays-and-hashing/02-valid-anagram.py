"""
https://www.youtube.com/watch?v=9UtInBqnCgA
https://leetcode.com/problems/valid-anagram/
https://neetcode.io/problems/is-anagram/solution

Given two strings s and t, return true if t is an
of s, and false otherwise.
Example 1:
Input: s = "anagram", t = "nagaram"
Output: true
Example 2:
Input: s = "rat", t = "car"
Output: false
You should aim for a solution with O(n + m) time and O(1) space, where n is the length of the string s and m is the length of the string t.
"""


def isAnagram(s: str, t: str) -> bool:
    """
    Solutions :
    Time & Space Complexity

    Time complexity: O(n+m)O(n+m)
    Space complexity: O(1)O(1) since we have at most 2626 different characters.

    """
    ## solution 1 TC O(n), SC O(n)
    if len(s) != len(t):
        return False
    countS, countT = {}, {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    return countS == countT

    ## solution 2:
    # Time complexity: O(n log n+m )
    # Space complexity: O(1) or O(n+m)O(n+m) depending on the sorting algorithm.
    # def isAnagram(self, s: str, t: str) -> bool:
    #     if len(s) != len(t):
    #         return False
    #     return sorted(s) == sorted(t)


def run_isAnagram_tests():
    GREEN = "\033[92m"
    RED = "\033[91m"
    RESET = "\033[0m"

    test_cases = [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("a", "a", True),
        ("ab", "ba", True),
        ("aa", "a", False),
        ("listen", "silent", True),
        ("triangle", "integral", True),
        ("hello", "bello", False),
        ("", "", True),
        ("abcdef", "abcdee", False),
    ]

    print("Testing isAnagram:\n")

    for i, (s, t, expected) in enumerate(test_cases, 1):
        result = isAnagram(s, t)
        if result == expected:
            print(f"{GREEN}✅ Test {i}: s='{s}', t='{t}' → {result} (expected: {expected}){RESET}")
        else:
            print(f"{RED}❌ Test {i}: s='{s}', t='{t}' → {result} (expected: {expected}){RESET}")


if __name__ == "__main__":
    run_isAnagram_tests()
