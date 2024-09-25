"""
https://leetcode.com/problems/contains-duplicate-ii/


Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

This basically means:

Find 2 numbers in the array that are equal and are AT MOST  k apart from each other.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false

"""


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        My solution
        SC = O(n)
        TC = O(n)
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        nums_indices = {}
        for i, num in enumerate(nums):
            if num in nums_indices:
                if abs(nums_indices[num] - i) <= k:
                    return True
            nums_indices[num] = i
        return False

    class Solution(object):
        def containsNearbyDuplicate(self, nums, k):
            """
            GPT provided sliding window, slightly better SC; Interesting as it is the first time I am seeing
            the sliding window algo, at least with its real name.
            SC = O(k)
            TC = O(n)
            :type nums: List[int]
            :type k: int
            :rtype: bool
            """
            # Use a set to represent the sliding window of the last k elements
            sliding_window = set()

            for i, num in enumerate(nums):
                # If the current number is already in the sliding window, return True
                if num in sliding_window:
                    return True

                # Add the current number to the sliding window
                sliding_window.add(num)

                # If the size of the sliding window exceeds k, remove the oldest element
                if len(sliding_window) > k:
                    sliding_window.remove(nums[i - k])

            return False

nums = [1, 2, 3, 1];
k = 3
sol = Solution()
print(sol.containsNearbyDuplicate(nums, k))
