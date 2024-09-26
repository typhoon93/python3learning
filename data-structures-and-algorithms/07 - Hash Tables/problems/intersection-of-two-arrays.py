"""
https://leetcode.com/problems/intersection-of-two-arrays

Given two integer arrays nums1 and nums2, return an array of their
intersection. The intersection of two arrays is defined as the set of elements that are present in both arrays.
Each element in the result must be unique and you may return the result in any order.



Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.


Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000

"""


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        My solution. Simple to do with set intersection, i will do a manual one though.
        SC = O(n + m) n = len nums 1 ; m = intersection len
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1_set = set(nums1)
        nums_intersection = set()
        for num in nums2:
            if num in nums1_set:
                nums_intersection.add(num)

        return nums_intersection # can be converted to list