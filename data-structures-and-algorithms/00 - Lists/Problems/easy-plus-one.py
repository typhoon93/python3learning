"""
https://leetcode.com/problems/plus-one/

You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

 
Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
 
 """

from typing import List


class Solution:
    """
    I have two solutions, practically the same, but one of them uses a try / except block.
    Space complexity O(1), time complexity worst case will be O(n).

    I do not like the other solutions in leetcode, the best ones generally use something like:

    return [1] + digits

    in the end, and they have the same complexity as mine.
    The reason I do not like [1] + digits is because it reindexes the list.
    This doesn't change the complexity since if it got to that point, we already are at O(n), but it's not necassary.
    """

    def plusOne(self, digits: List[int]) -> List[int]:
        i = -1
        digits[i] += 1
        while digits[i] == 10:
            try:
                digits[i - 1] += 1
            except IndexError:
                digits[i] = 1
                digits.append(0)
                break
            digits[i] = 0
            i -= 1
        return digits

    def plusOneVersion2(self, digits: List[int]) -> List[int]:
        i = -1
        digits[i] += 1
        while digits[i] == 10:
            if i == -len(digits):
                digits[i] = 1
                digits.append(0)
                break
            digits[i - 1] += 1
            digits[i] = 0
            i -= 1

        return digits


if __name__ == "__main__":
    solution = Solution()
    digits = [9, 9, 9]
    print(solution.plusOneVersion2(digits))
