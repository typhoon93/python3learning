"""
https://leetcode.com/problems/isomorphic-strings/

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.



Example 1:

Input: s = "egg", t = "add"

Output: true

Explanation:

The strings s and t can be made identical by:

Mapping 'e' to 'a'.
Mapping 'g' to 'd'.
Example 2:

Input: s = "foo", t = "bar"

Output: false

Explanation:

The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.

Example 3:

Input: s = "paper", t = "title"

Output: true



Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
"""


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        My solution go too complex and couldn't handle edge cases, this is a solution from GPT
        TC = O(n) len of strings
        SC = O(n) mapping dicts size; it maps chars so max size is really O(1)
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        map_s_to_t = {}
        map_t_to_s = {}

        for char_s, char_t in zip(s, t):
            if char_s in map_s_to_t:
                if map_s_to_t[char_s] != char_t:
                    return False
            else:
                map_s_to_t[char_s] = char_t

            # check mapping from t to s
            if char_t in map_t_to_s:
                if map_t_to_s[char_t] != char_s:
                    return False
            else:
                map_t_to_s[char_t] = char_s

        return True


sol = Solution()
# s = "bbbaaaba"
# t = "aaabbbba"
# s = "paper"
# t = "title"
# s = "foo"
# t = "bar"
s = "abcdefghijklmnopqrstuvwxyzva"
t = "abcdefghijklmnopqrstuvwxyzck"

print(sol.isIsomorphic(s, t))
expected = False
print(f"{expected=}")
