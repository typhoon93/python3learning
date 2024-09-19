"""
https://leetcode.com/problems/balanced-binary-tree/
Given a binary tree, determine if it is
height-balanced. A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.



Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:

Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isBalanced(self, root):
        """
        Recursive approach
        A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node
        never differs by more than one.
        SC O(h) = height
        TC O(n**2) = n = nodes = for everu subnoe we will calculate its depth and compare
        :type root: TreeNode
        :rtype: bool
        """
        # we need to compare the heights of each subroot,
        # aka we get the heights of each subroot recursively

        if not root:
            return True

        def traverse(node, height=0):
            if not node:
                return height
            l_height = traverse(node.left, height)
            r_height = traverse(node.right, height)
            return 1 + max(l_height, r_height)

        l_height = traverse(root.left)
        r_height = traverse(root.right)
        if abs(l_height - r_height) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def isBalanced(self, root):
        """
        GPT code, using recursion again, optimized
        SC = O(h)
        TC = O(n)
        """

        def check(node):
            if not node:
                return 0  # height of empty tree is 0

            left_height = check(node.left)
            if left_height == -1:
                return -1  # not balanced

            right_height = check(node.right)
            if right_height == -1:
                return -1  # not balanced

            if abs(left_height - right_height) > 1:
                return -1

            return 1 + max(left_height, right_height)

        return check(root) != -1

    def isBalanced(self, root):
        """
        Optimized recursive approach using True/False GPT code.
        Space Complexity: O(h)
        Time Complexity: O(n)
        """

        def check(node):
            if not node:
                return True, 0  # An empty tree is balanced with height 0

            # Check the left subtree
            left_balanced, left_height = check(node.left)
            if not left_balanced:
                return False, 0  # Left subtree is not balanced

            # Check the right subtree
            right_balanced, right_height = check(node.right)
            if not right_balanced:
                return False, 0  # Right subtree is not balanced

            # Check the balance condition at the current node
            if abs(left_height - right_height) > 1:
                return False, 0  # Current node is not balanced

            # Current node is balanced, return True and its height
            return True, 1 + max(left_height, right_height)

        balanced, _ = check(root)
        return balanced


sol = Solution()
root = TreeNode(1, TreeNode(2))
expected = True
print(sol.isBalanced(root))
print(f"{expected=}")
