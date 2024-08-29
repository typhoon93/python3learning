"""

https://leetcode.com/problems/first-unique-character-in-a-string/

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1
 

Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.

"""

from collections import defaultdict


class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        TC = O(n)
        SC = O(1) - this is due ot this constraint: "s consists of only lowercase English letters."; aka at most it is 26 chars. We drop constants so it becomes O(1).
        If we didn't have this constraint, SC would be O(n)
        """
        char_map = defaultdict(lambda: [0, 0])

        for index, char in enumerate(s):
            if char_map[char][0] == 0:
                char_map[char][1] = index
            char_map[char][0] += 1

        for count, index in char_map.values():
            if count == 1:
                return index

        return -1


if __name__ == "__main__":
    s = "leetcode"
    solution = Solution()
    res = solution.firstUniqChar(s)
    print(res)
