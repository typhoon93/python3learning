"""
https://leetcode.com/problems/make-the-string-great/

Given a string s of lower and upper case English letters.

A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:

0 <= i <= s.length - 2
s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can keep doing this until the string becomes good.

Return the string after making it good. The answer is guaranteed to be unique under the given constraints.

Notice that an empty string is also good.



Example 1:

Input: s = "leEeetcode"
Output: "leetcode"
Explanation: In the first step, either you choose i = 1 or i = 2, both will result "leEeetcode" to be reduced to "leetcode".
Example 2:

Input: s = "abBAcC"
Output: ""
Explanation: We have many possible scenarios, and all lead to the same answer. For example:
"abBAcC" --> "aAcC" --> "cC" --> ""
"abBAcC" --> "abBA" --> "aA" --> ""
Example 3:

Input: s = "s"
Output: "s"


Constraints:

1 <= s.length <= 100
s contains only lower and upper case English letters.

"""


class Solution(object):
    def makeGood(self, s):
        """
        My solution:
        SC = O(n)
        TC = O(n)

        Using the below fact (otherwise we can solve with islower() / isupper() checks
        # In binary, the difference between uppercase and lowercase letters is controlled by just one bit: the 6th bit. This was a clever design choice to simplify conversions between uppercase and lowercase letters.
        #
        # In the binary representation of ASCII:
        #
        # Uppercase 'A' (65 in decimal) is 01000001 in binary.
        # Lowercase 'a' (97 in decimal) is 01100001 in binary
        :type s: str
        :rtype: str
        """
        # s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
        # we can use isupper / islower, but I am using some hack i found - in ascii the difference between upper and lower
        # case letters is 32
        stack = []

        for i in range(len(s)):
            if stack:
                if abs(ord(stack[-1]) - ord(
                        s[i])) == 32:  # current and prev chars are the same one being uppercase, the other lowercase
                    stack.pop()
                    continue
            stack.append(s[i])
        return "".join(stack)


sol = Solution()
s = "leEeetcode"
expected = "leetcode"

print(sol.makeGood(s))
print(f"{expected}")
