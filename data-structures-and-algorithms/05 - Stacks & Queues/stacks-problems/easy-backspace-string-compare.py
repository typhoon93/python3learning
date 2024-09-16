"""
https://leetcode.com/problems/backspace-string-compare/

Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.



Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".


Constraints:

1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.


"""


class Solution(object):
    # def backspaceCompare(self, s, t):
    #     """
    #     My solution.
    #     TC = O(n + m)
    #     SC = O(n + m)
    #     :type s: str
    #     :type t: str
    #     :rtype: bool
    #     """
    #     s_entered = []
    #     for c in s:
    #         if c == "#":
    #             if s_entered:
    #                 s_entered.pop()
    #         else:
    #             s_entered.append(c)
    #     t_entered = []
    #     for c in t:
    #         if c == "#":
    #             if t_entered:
    #                 t_entered.pop()
    #         else:
    #             t_entered.append(c)
    #
    #     return t_entered == s_entered

    def backspaceCompare(self, s, t):
        """
        Optimized solution using two pointers. This is code from GPT,
        I was going in this same direction but spent way too much time so I asked GPT / checked LC for the solution.
        Given more time I believe I could have reached this same solution.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        i, j = len(s) - 1, len(t) - 1  # Initialize pointers for s and t
        skip_s = skip_t = 0            # Skip counters for s and t

        while i >= 0 or j >= 0:
            # Process backspaces in s
            while i >= 0:
                if s[i] == '#':
                    skip_s += 1
                    i -= 1
                elif skip_s > 0:
                    skip_s -= 1
                    i -= 1
                else:
                    break  # Found a valid character in s

            # Process backspaces in t
            while j >= 0:
                if t[j] == '#':
                    skip_t += 1
                    j -= 1
                elif skip_t > 0:
                    skip_t -= 1
                    j -= 1
                else:
                    break  # Found a valid character in t

            # Compare the characters
            if i >= 0 and j >= 0:
                if s[i] != t[j]:
                    return False
            elif i >= 0 or j >= 0:
                # One string has characters left
                return False

            i -= 1
            j -= 1

        return True


sol = Solution()
# s = "bbbextm"
# t = "bbb#extm"
s = "ab##"

t = "c#d#"








print(sol.backspaceCompare(s, t))
expected = True
print(f"{expected=}")
