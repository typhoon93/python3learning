"""
https://leetcode.com/problems/intersection-of-two-arrays-ii/

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.



Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.


Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000


Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
"""


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        My solution.
        SC = O(n + m)
        TC = O(n + m)
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        nums1_frequencies = {}
        nums2_frequencies = {}
        for num1 in nums1:
            if num1 in nums1_frequencies:
                nums1_frequencies[num1] += 1
            else:
                nums1_frequencies[num1] = 1

        for num2 in nums2:
            if num2 in nums2_frequencies:
                nums2_frequencies[num2] += 1
            else:
                nums2_frequencies[num2] = 1

        for num in nums1_frequencies:
            if num in nums2_frequencies:
                for _ in range(min(nums1_frequencies[num], nums2_frequencies[num])):
                    result.append(num)

        return result

    def intersect(self, nums1, nums2):
        """
        Considering different size arrays and optimizing for that
        SC = O(n + h) n is len of the smaller array, h is the len of the intersection list
        TC = O(n + m) len of both arrays

        This also the algo I would use for this case:

        What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
        -> we load the nums from nums2 in batcher or whatever streaming type of mechanism we have when we start the second for loop.
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        result = []
        nums1_frequencies = {}
        for num1 in nums1:
            if num1 in nums1_frequencies:
                nums1_frequencies[num1] += 1
            else:
                nums1_frequencies[num1] = 1

        for num in nums2:
            if num in nums1_frequencies and nums1_frequencies[num] > 0:
                result.append(num)
                nums1_frequencies[num] -= 1 # reducing the count so we can stop when all intersectin duplicates are gone.

        return result

    def intersect(self, nums1, nums2):
        """
        If the arrays are sorted: (i am sorting them here to ensure tests pass and simulate sorted arrays).
        SC = 0(h) - intersecting numbers
        TC = O(n+m) - len or arrays (we do not consider the sorting below as in the question they say arrays will be sorted)
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        result = []
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j +=1
        return result


sol = Solution()
nums1 = [1,2,2,1]
nums2 = [2,2]

print(sol.intersect(nums1, nums2))
expected = [2,2]
print(f"{expected=}")