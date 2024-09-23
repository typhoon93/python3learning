"""
https://leetcode.com/problems/count-complete-tree-nodes

Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.



Example 1:


Input: root = [1,2,3,4,5,6]
Output: 6
Example 2:

Input: root = []
Output: 0
Example 3:

Input: root = [1]
Output: 1


Constraints:

The number of nodes in the tree is in the range [0, 5 * 104].
0 <= Node.val <= 5 * 104
The tree is guaranteed to be complete.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):


    # def countNodes(self, root):
    #     """
    #     Recursive solution.
    #     TC = O(log n * log n) this is because each time we do a recursive step (which will happen log n times since we are halving the tree at each step),
    #     we are also performing a log n operation (the get_height_for_side)
    #
    #     SC = O(log n) = height -> this is the recursive stack.
    #     """
    #
    #     def get_height_left(node):
    #         """
    #         side is left or right
    #         TC = O(log n) = height
    #         SC = O(1)
    #         """
    #         height = 0
    #         while node:
    #             node = node.left
    #             height += 1
    #         return height
    #
    #     def get_height_right(node):
    #         """
    #         side is left or right
    #         TC = O(log n) = height
    #         SC = O(1)
    #         """
    #         height = 0
    #         while node:
    #             node = node.right
    #             height += 1
    #         return height
    #
    #     left_h = get_height_left(root)
    #     right_h = get_height_right(root)
    #     if left_h == right_h:
    #         return 2 ** left_h - 1
    #     return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    #
    def countNodes(self, root):
        """
        GPT solution, iterative, using binary search
        """
        if not root:
            return 0

        # Calculate the depth of the tree
        def get_depth(node):
            depth = 0
            while node.left:
                node = node.left
                depth += 1
            return depth

        def exists(idx, h, node):
            left, right = 0, 2 ** h - 1
            for _ in range(h):
                mid = (left + right) // 2
                if idx <= mid:
                    node = node.left
                    right = mid
                else:
                    node = node.right
                    left = mid + 1
            return node is not None

        depth = get_depth(root)
        if depth == 0:
            return 1  # Only the root exists

        # Binary search to find the number of nodes in the last level
        left, right = 0, 2 ** depth - 1
        while left <= right:
            mid = (left + right) // 2
            if exists(mid, depth, root):
                left = mid + 1
            else:
                right = mid - 1

        # Total number of nodes is full levels' nodes + last level nodes found
        return (2 ** depth - 1) + left
    #

#
sol = Solution()
root = TreeNode(1,
                TreeNode(2,
                         TreeNode(4), TreeNode(5)),
                TreeNode(3,
                         TreeNode(6)))
expected = 6
res = sol.countNodes(root)
print(res)
print(f"{expected=}")

# print(sol.exists(2, 2, root))
