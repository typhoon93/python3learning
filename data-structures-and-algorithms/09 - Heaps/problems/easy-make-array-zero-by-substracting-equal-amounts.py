"""
https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/

You are given a non-negative integer array nums. In one operation, you must:

Choose a positive integer x such that x is less than or equal to the smallest non-zero element in nums.
Subtract x from every positive element in nums.
Return the minimum number of operations to make every element in nums equal to 0.



Example 1:

Input: nums = [1,5,0,3,5]
Output: 3
Explanation:
In the first operation, choose x = 1. Now, nums = [0,4,0,2,4].
In the second operation, choose x = 2. Now, nums = [0,2,0,0,2].
In the third operation, choose x = 2. Now, nums = [0,0,0,0,0].
Example 2:

Input: nums = [0]
Output: 0
Explanation: Each element in nums is already 0 so no operations are needed.


Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100

"""
import heapq

"""
The best tc we can get is o(n), if we concede that we will have sc = O(n);
The best sc is O(1), but then we need to concede to having a TC of (n log n);
"""


class Solution(object):
    def minimumOperations(self, nums):
        """
        My solution, using heaps;
        SC = O(1)
        TC = O(n**2 + n log n) -> we drop non dominants so tc is O(n**2)
        :type nums: List[int]
        :rtype: int
        """
        operations = 0
        heapq.heapify(nums)
        while nums:
            current = heapq.heappop(nums)
            if current == 0:
                continue
            else:
                operations += 1
                for i in range(len(nums)):
                    nums[i] -= current

        return operations

    def minimumOperations(self, nums):
        """
        My improved solution, using heaps; I have modified it so we have n log n complexity
        SC = O(1)
        TC = 0(n log n);
        we rely on the fact that we only need to substract from the top element; knowing that this is a min heap, any subsequent element
        is going to be bigger or equal to my last element;
        I keep track of substracted up to now and only substract when popping elements.
        This removes the need to do a whole loop inside nums, reducing complexity.
        :type nums: List[int]
        :rtype: int
        """
        operations = 0
        heapq.heapify(nums)  # O(n)
        substracted_up_to_now = 0
        while nums:
            current = heapq.heappop(nums) - substracted_up_to_now
            if current == 0:
                continue
            else:
                operations += 1
                substracted_up_to_now += current

        return operations

    def minimumOperations(self, nums):
        """
        This is from GPT; this approach reduces TC but increases SC to O(n);
        TC = O(n)
        SC = O(n)
        This comes from the realization that the operations is going to be the non zero unique elements in the list.
        Essentially we turn it into a set that doesn't have zeros
        """
        nums_set = {x for x in nums if x > 0}
        return len(nums_set)


sol = Solution()
amount = [1, 5, 0, 3, 5]
expected = 3
print(sol.minimumOperations(amount))
print(f"{expected=}")
