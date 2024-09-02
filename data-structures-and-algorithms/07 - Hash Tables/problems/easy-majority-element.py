"""
https://leetcode.com/problems/majority-element/

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.



Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2


Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109


Follow-up: Could you solve the problem in linear time and in O(1) space?
"""
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        tc and sc = O(1)
        """
        count = {}
        maj_count = len(nums) / 2
        for elem in nums:
            count.setdefault(elem, 0)
            count[elem] += 1
            if count[elem] >= maj_count:
                return elem

    def majorityElement(self, nums: List[int]) -> int:
        """attempt at sc o(1), but tc is O(n**2)"""
        maj_count = len(nums) / 2
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[i] == nums[j]:
                    count += 1
            if count >= maj_count:
                return nums[i]

    def majorityElement(self, nums: List[int]) -> int:
        """Leetcode tc O(n) sc O(1) boyer-moore algo
        works fine having in mind the constraints that we will always have a majority element.
        if the list might not have one you need to then do a second pass of the selected candidate, get its count
        and then check if it is majority"""
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num

            if candidate == num:
                count += 1
            else:
                count -= 1
        return candidate


if __name__ == "__main__":
    sol = Solution()
    lst = [3, 2, 3]
    print(sol.majorityElement(lst))
