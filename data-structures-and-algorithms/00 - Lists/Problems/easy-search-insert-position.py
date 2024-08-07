"""
https://leetcode.com/problems/search-insert-position/

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104"""

from typing import List


class Solution:
    def searchInsertComplexityN(self, nums: List[int], target: int) -> int:
        """this is a time complexity O(n) solution. Space complexity is O[n] using this as a reference point, I built the O(log n) solution."""
        length = len(nums)
        for i in range(length):
            if nums[i] >= target:
                return i
            if nums[i] > target:
                return i
        return i + 1

    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        This is my final solution, has time complexity O(log n), but has a recursive stack so it has a O(log n) space complexity too
        """

        def index_finder(nums, start_index, end, target):
            middle = len(nums[start_index:end]) // 2 + start_index
            if nums[middle] == target:
                return middle
            elif len(nums[start_index:end]) == 1:
                if nums[start_index] > target:
                    return start_index
                elif nums[start_index] < target:
                    return start_index + 1

            elif nums[middle] > target:
                return index_finder(nums, start_index, middle, target)
            else:
                return index_finder(nums, middle, end, target)

        return index_finder(nums, 0, len(nums), target)

    def searchInsertLeetCode(self, nums: List[int], target: int) -> int:
        """
        This is a solution I found on leetcode, using a while loop, which makes the space complexity O(1), with time complexity O(log n),
        very elegant.
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left


lst = [1, 3, 5, 6]
target = 2
solution = Solution()
print(solution.searchInsert(lst, target))
