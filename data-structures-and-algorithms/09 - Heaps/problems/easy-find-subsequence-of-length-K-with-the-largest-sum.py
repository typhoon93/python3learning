"""
https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum


You are given an integer array nums and an integer k. You want to find a subsequence of nums of length k that has the largest sum.

Return any such subsequence as an integer array of length k.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.



Example 1:

Input: nums = [2,1,3,3], k = 2
Output: [3,3]
Explanation:
The subsequence has the largest sum of 3 + 3 = 6.
Example 2:

Input: nums = [-1,-2,3,4], k = 3
Output: [-1,3,4]
Explanation:
The subsequence has the largest sum of -1 + 3 + 4 = 6.
Example 3:

Input: nums = [3,4,3,3], k = 2
Output: [3,4]
Explanation:
The subsequence has the largest sum of 3 + 4 = 7.
Another possible subsequence is [4, 3].


Constraints:

1 <= nums.length <= 1000
-105 <= nums[i] <= 105
1 <= k <= nums.length
"""
import heapq


class Solution(object):
    def maxSubsequence(self, nums, k):
        """
        My solution
        SC = O(k)
        TC = O(n log k + k log k)
        My solution
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        max_k_heap = []
        for index, num in enumerate(nums): # this whole loop is O( n log k )
            if len(max_k_heap) >= k:
                heapq.heappushpop(max_k_heap, (num, index)) # we need to preserve original order in output
            else:
                heapq.heappush(max_k_heap, (num, index))
        max_k_heap.sort(key=lambda num: num[1]) # O (k log k)
        result = [num[0] for num in max_k_heap] # O (k)
        return result



nums = [-1,-2,3,4]

k = 3

expected = [-1,3,4]
sol = Solution()
print(sol.maxSubsequence(nums, k))
print(f'{expected=}')
