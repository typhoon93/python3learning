"""
https://leetcode.com/problems/remove-outermost-parentheses/

A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.

For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into s = A + B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.

Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.



Example 1:

Input: s = "(()())(())"
Output: "()()()"
Explanation:
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
Example 2:

Input: s = "(()())(())(()(()))"
Output: "()()()()(())"
Explanation:
The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".
Example 3:

Input: s = "()()"
Output: ""
Explanation:
The input string is "()()", with primitive decomposition "()" + "()".
After removing outer parentheses of each part, this is "" + "" = "".

Details from gpt:

To clarify:

A valid parentheses string is one where each opening parenthesis ( has a corresponding closing parenthesis ), and they are properly nested.
A string is called primitive if there’s no way to divide it into two smaller non-empty valid parentheses strings.
For example:

The string () is primitive because there’s no way to split it into two valid parentheses strings.
The string (()) is also primitive because, although it's a valid string, you cannot split it into two non-empty valid parentheses strings.
However, the string ()() is not primitive because you can split it into () + (), which are both valid non-empty parentheses strings.
Essentially, a primitive string is like the smallest building block of valid parentheses strings that cannot be broken down further into smaller valid parts.


Constraints:

1 <= s.length <= 105
s[i] is either '(' or ')'.
s is a valid parentheses string.

"""


class Solution(object):
    # def removeOuterParentheses(self, s):
    #     """
    #     Initial solution.
    #     SC = O(n)
    #     TC = O(n)
    #     :type s: str
    #     :rtype: str
    #     """
    #     primitives = []
    #     i = -1
    #     closing_needed = 0
    #     for c in s:
    #         if closing_needed == 0:
    #             primitives.append([])
    #             i += 1
    #         if c == "(":
    #             closing_needed += 1
    #         if c == ")":
    #             closing_needed -= 1
    #         primitives[i].append(c)
    #
    #     return ("".join(["".join(primitive[1:-1]) for primitive in primitives]))

    # def removeOuterParentheses(self, s):
    #     """
    #     A bit optimized, still sc / tc same.
    #     """
    #     count = 0
    #     result = []
    #     for c in s:
    #         if c == '(':
    #             if count > 0:
    #                 result.append(c)
    #             count += 1
    #         else:
    #             count -= 1
    #             if count > 0:
    #                 result.append(c)
    #     return ''.join(result)

    def removeOuterParentheses(self, s):
        """
        Solution using stacks
        nitialize:

        An empty stack: stack = [].
        An empty result list: result = [].
        Iterate Over Each Character in the string S:

        If the character is '(':
            If the stack is not empty:
                We are inside a primitive substring; append '(' to result.
            Push '(' onto the stack.
        If the character is ')':
            Pop the top element from the stack.
            If the stack is not empty after popping:
                We are still inside a primitive; append ')' to result.
        """
        stack = []
        result = []
        for c in s:
            if c == "(":
                if stack:
                    # If stack is not empty, we are inside a primitive; append '('
                    result.append(c)
                stack.append(c)
            else:
                stack.pop()
                if stack:
                    # If stack is not empty after popping, we are inside a primitive; append ')'
                    result.append(c)
        return ''.join(result)


sol = Solution()
s = "(())"
print(sol.removeOuterParentheses(s))
print("Expected: ()")