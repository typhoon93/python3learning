"""
https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

"""


class Solution:
    def isValid(self, s: str) -> bool:
        """
        New solution, created after isValidOld, to utilize STACKS better.
        I had already seen the solutions to the problem from others.
        This approach is much better because it utilizes the fact that we use a STACk, so we direclty pop,
        we do not do an expensive check like:  c in pending_closed (first solution)
        Complexity: O(n)
        """
        bracket_pairs = {
            "(": ")",
            "{": "}",
            "[": "]",
        }
        pending_closed = []
        for bracket in s:
            if bracket in bracket_pairs:
                pending_closed.append(bracket_pairs[bracket])
            else:
                if len(pending_closed) == 0 or bracket != pending_closed.pop():
                    return False
        return False if pending_closed else True

    def isValidOld(self, s: str) -> bool:
        """
        Time complexity: O(n)
        Space Complexity: O(n)
        """
        pairs = {
            "(": ")",
            "{": "}",
            "[": "]",
        }
        pending_closed = []
        for c in s:
            if c in pending_closed and pending_closed[-1] == c:
                pending_closed.pop()
            else:
                try:
                    pending_closed.append(pairs[c])
                except:  # case when we have a closing bracking. This means that we did not have an opening bracket for it, hence it makes the string invalid.
                    return False

        if pending_closed:
            return False
        else:
            return True

        # https://chatgpt.com/c/d6262691-8cbc-46fb-b75a-5243c09298e8

    def isValidLeetCode(self, s):
        """Very similar to mine"""
        stack = []  # only use append and pop
        pairs = {"(": ")", "{": "}", "[": "]"}
        for bracket in s:
            if bracket in pairs:
                stack.append(bracket)
            elif len(stack) == 0 or bracket != pairs[stack.pop()]:
                return False

        return len(stack) == 0


if __name__ == "__main__":
    s = ")"
    solution = Solution()
    res = solution.isValid(s)
    print(res)
