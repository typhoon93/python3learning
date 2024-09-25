"""
https://leetcode.com/problems/valid-anagram/


Given two strings s and t, return true if t is an anagram  of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, using all the original letters exactly once.


Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false



Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.


Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

"""
from collections import defaultdict


class Solution(object):
    def isAnagram(self, s, t):
        """
        My solution
        sc = O(n)
        tc = O(n)
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_char_count = {}
        t_char_count = {}
        for char in s:
            if char not in s_char_count:
                s_char_count[char] = 1
            else:
                s_char_count[char] += 1

        for char in t:
            if char not in t_char_count:
                t_char_count[char] = 1
            else:
                t_char_count[char] += 1

        return s_char_count == t_char_count

    def isAnagram(self, s, t):
        """
        My solution using 1 dct
        sc = O(n)
        tc = O(n)
        :type s: str
        :type t: str
        :rtype: bool
        """
        char_count = {}
        for char in s:
            if char not in char_count:
                char_count[char] = 1
            else:
                char_count[char] += 1

        for char in t:
            if char not in char_count:
                return False
            else:
                char_count[char] -= 1

        for value in char_count.values():
            if value != 0:
                return False
        return True

    def isAnagram(self, s, t):
        """
        Optimized solution using 1 dictionary, from GPT
        SC = O(n)
        TC = O(n)
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        char_count = defaultdict(int)

        # Increment for characters in s and decrement for characters in t
        for i in range(len(s)):
            char_count[s[i]] += 1
            char_count[t[i]] -= 1

        # Check if all counts are zero
        for count in char_count.values():
            if count != 0:
                return False

        return True
sol = Solution()
s = "anagram"
t = "nagaram"
print(sol.isAnagram(s, t))

expected = True
print(f"{expected=}")