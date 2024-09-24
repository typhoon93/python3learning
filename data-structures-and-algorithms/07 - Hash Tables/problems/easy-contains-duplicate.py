"""
https://leetcode.com/problems/contains-duplicate

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.



Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true



Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109


"""
import collections


class Solution(object):
    def containsDuplicate(self, nums):
        """
        SC = O(n)
        TC = O(n)
        :type nums: List[int]
        :rtype: bool
        """
        nums_d = collections.defaultdict(int)
        for num in nums:
            nums_d[num] += 1
            if nums_d[num] > 1:
                return True
        return False

    def containsDuplicate(self, nums):
        """
        A bit better.
        SC = O(n)
        TC = O(n)
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False