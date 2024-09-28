"""
https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array

Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).


Example 1:

Input: nums = [3,4,5,2]
Output: 12
Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12.
Example 2:

Input: nums = [1,5,4,5]
Output: 16
Explanation: Choosing the indices i=1 and j=3 (indexed from 0), you will get the maximum value of (5-1)*(5-1) = 16.
Example 3:

Input: nums = [3,7]
Output: 12


Constraints:

2 <= nums.length <= 500
1 <= nums[i] <= 10^3

"""
import heapq
from typing import List


class Solution(object):
    # def maxProduct(self, nums):
    #     """
    #     My solution initial, brute force.
    #     SC = O(1)
    #     TC = O(n**2)
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     biggest = float("-inf")
    #     for i in range(len(nums)-1):
    #         for j in range(i+1, len(nums)):
    #             current = (nums[i] - 1) * (nums[j]-1)
    #             if current > biggest:
    #                 biggest = current
    #     return biggest
    #
    def maxProduct(self, nums: List):
        """
        Second solution, optimized and uses heap. This exercise can be solved by finding the first and second biggest number in a list (without discarding duplicate nums) very easily too.
        SC / TC will remain as the below solution.
        SC = O(1) -> list size can grow to 2 at max
        TC = O(n) -> pushing into the heap is log n, however since the heap size is 2 at max, we consider it constant.
        so the only TC is the main loop.
        :type nums: List[int]
        :rtype: int
        """
        top_2_heap = []
        for num in nums:
            if len(top_2_heap) >= 2:  # this way only the the top 2 biggest nums are always in the heap.
                heapq.heappushpop(top_2_heap, num)
            else:
                heapq.heappush(top_2_heap, num)

        return (top_2_heap[0] - 1) * (top_2_heap[1] - 1)

    def maxProduct(self, nums):
        """
        same complexity as above, but using iteration and keepign track of 2 biggest elements
        """
        if len(nums) < 2:
            return 0  # Not possible case based on constraints but safe check

        # Initialize the two largest values
        max1 = max2 = float('-inf')

        # Find the two largest numbers
        for num in nums:
            if num > max1:
                max2 = max1  # Update second max
                max1 = num  # Update first max
            elif num > max2:
                max2 = num  # Update only second max

        # Compute the result using the two largest numbers
        return (max1 - 1) * (max2 - 1)


nums = [3, 4, 5, 2]

expected = 12
sol = Solution()
print(sol.maxProduct(nums))
print(f'{expected=}')
