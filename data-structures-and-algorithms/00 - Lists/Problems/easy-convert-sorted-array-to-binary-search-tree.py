"""
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree

Given an integer array nums where the elements are sorted in ascending order, convert it to a
height-balanced
 binary search tree.



Example 1:

Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:


Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.


Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in a strictly increasing order.

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums):
        """
        This is a gpt solution, I couldn't come up with my in a reasonable time.
        TC = O(n) - each element is used exactly once to create a TreeNode in the BST.
        SC = log n - maximum depth of the recursive stack, if we have a balanced tree.
        """
        def helper(start, end):
            if start > end:
                return None
            mid = (start + end) // 2
            root = TreeNode(nums[mid])
            root.left = helper(start, mid - 1)
            root.right = helper(mid + 1, end)
            return root

        return helper(0, len(nums) - 1)

if __name__ == "__main__":
    sol = Solution()
    nums = [0, 1, 2, 3, 4, 5]
    res = sol.sortedArrayToBST(nums)
    print(res.val)
