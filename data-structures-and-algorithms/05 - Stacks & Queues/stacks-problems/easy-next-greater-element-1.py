"""
https://leetcode.com/problems/next-greater-element-i/

The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

 

Example 1:

Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
Example 2:

Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
- 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.
 

Constraints:

1 <= nums1.length <= nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 104
All integers in nums1 and nums2 are unique.
All the integers of nums1 also appear in nums2.
 

Follow up: Could you find an O(nums1.length + nums2.length) solution?

"""

import collections
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Initial solution.
        Space complexity = O(n) n mainly coming from len(nums1)
        Time complexity = O(n * m) where n = len(nums1) and m = len(nums2)
        """
        result = []
        for i in range(len(nums1)):
            current_number_found = False
            nge_found = False
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    current_number_found = True
                    continue
                if current_number_found and nums1[i] < nums2[j]:
                    nge_found = True
                    result.append(nums2[j])
                    break
            if not nge_found:
                result.append(-1)
        return result

    def nextGreaterElementBetter(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Not my solution, GPT
        TC = O(n + m) where n = len(nums1) and m = len(nums2)

        KEY: Implicit Non-Decreasing Order: As you push elements onto the stack,
        any element that remains on the stack does so because a greater element has not yet been encountered.
        Thus, the stack maintains a sort of "waiting list" of elements in non-decreasing order,
        where the topmost element is always the smallest among those awaiting their NGE.

        """

        next_greater_map = {}
        # has map for efficient access, adding elements to it as we find specific element / next_greater_element (NGE) pairs
        stack = []
        # list will be used as stack, tracking elements for which we haven't yet found the next greater element.
        for num in nums2:
            while stack and stack[-1] < num:  # pay attention to the while loop here;
                # if we enter the loop, it means we have a STACK, plus the current number is greater than the last one in the stack.
                # we repeat this however many times necassary - this ensure that we effectively find all elements for which the current num is
                # the NGE for.
                # the sequence of events here ensures that any element remaining in the stack will not have any NGEs
                next_greater_map[stack.pop()] = num
            stack.append(num)
        while stack:
            next_greater_map[stack.pop()] = -1
        result = [next_greater_map[num] for num in nums1]
        return result


if __name__ == "__main__":

    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    solution = Solution()
    res = solution.nextGreaterElementBetter(nums1, nums2)
    print(res)
