"""
https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/

Given a valid parentheses string s, return the nesting depth of s. The nesting depth is the maximum number of nested parentheses.



Example 1:

Input: s = "(1+(2*3)+((8)/4))+1"

Output: 3

Explanation:

Digit 8 is inside of 3 nested parentheses in the string.

Example 2:

Input: s = "(1)+((2))+(((3)))"

Output: 3

Explanation:

Digit 3 is inside of 3 nested parentheses in the string.

Example 3:

Input: s = "()(())((()()))"

Output: 3



Constraints:

1 <= s.length <= 100
s consists of digits 0-9 and characters '+', '-', '*', '/', '(', and ')'.
It is guaranteed that parentheses expression s is a VPS.


"""


class Solution(object):
    def maxDepth(self, s):
        """
        My solution:
        SC = O(1)
        TC = O(n)
        Stack solution
        :type s: str
        :rtype: int
        """
        count = 0
        max_depth = count
        for char in s:
            if char == "(":
                count += 1
                if count > max_depth:
                    max_depth = count
            elif char == ")":
                count -= 1
        return max_depth

    def maxDepth(self, s):
        """
        Stack-based solution, less effective but implemented for practice
        Time Complexity: O(n)
        Space Complexity: O(n)
        :type s: str
        :rtype: int
        """
        stack = []
        max_depth = 0
        for char in s:
            if char == '(':
                stack.append('(')
                if len(stack) > max_depth:
                    max_depth = len(stack)
            elif char == ')':
                if stack:
                    stack.pop()
        return max_depth


sol = Solution()
s = "(1+(2*3)+((8)/4))+1"
expected = 3
print(sol.maxDepth(s))
print(f"{expected=}")
