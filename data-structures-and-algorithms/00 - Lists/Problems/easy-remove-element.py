"""
https://leetcode.com/problems/remove-element/

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

 

Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).
 

Constraints:

0 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= val <= 100

"""

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """My solution
        # Complexity
        - Time complexity:
        O(n)
        - Space complexity:
        O(n)
        """
        val_indexes = []
        length = len(nums)
        for i in range(length):
            if nums[i] == val:
                val_indexes.append(i)

        k = length - len(val_indexes)
        if k == 0:
            return k

        switch_index = -1
        for val_i in val_indexes:
            if val_i >= length + switch_index:
                break
            while nums[switch_index] == val:
                if val_i + (-switch_index) >= length:
                    break
                switch_index -= 1

            nums[val_i] = nums[switch_index]
            nums[switch_index] = val
            switch_index -= 1
        return k

    def removeElement2(self, nums: List[int], val: int) -> int:
        """A solution that is better and found on leetcode.
        This solution is simpler and faster, but does not preserve the original values in the array as I did,
        Time complexity: O(n)
        Space complexity: O(1)
        """
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        return index


lst = [3, 2, 2, 3]

val = 3
solution = Solution()
print(solution.removeElement2(lst, val))
print(lst)
