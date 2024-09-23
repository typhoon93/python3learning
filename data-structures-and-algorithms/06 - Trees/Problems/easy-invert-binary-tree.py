"""
https://leetcode.com/problems/invert-binary-tree

Given the root of a binary tree, invert the tree, and return its root.



Example 1:


Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Example 2:


Input: root = [2,1,3]
Output: [2,3,1]
Example 3:

Input: root = []
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""


# Definition for a binary tree node.
from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def invertTree(self, root):
        """
        My solution, recursive approach:
        SC = O(log n) - height of tree in best case, O(n) in worst case, skewed tree
        TC = O(n) since every node is visited
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

    def invertTree(self, root):
        """
        Iterative solution using a queue.
        SC = O(n) in the worst case when the tree is completely unbalanced, O(log n) for balanced
        TC = O(n)
        """
        if not root:
            return None

        queue = deque([root])
        while queue:
            current = queue.popleft()
            # Swap the children
            current.left, current.right = current.right, current.left

            # Add children to the queue if they exist
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        return root


    def display_dfs(self, root):
        if root is None:
            return

        # Initialize the queue with the root node
        queue = deque([root])

        # Perform BFS
        while queue:
            # Get the current node from the queue
            current_node = queue.popleft()
            print(current_node.val, end=" ")

            # Add left child to the queue if it exists
            if current_node.left:
                queue.append(current_node.left)

            # Add right child to the queue if it exists
            if current_node.right:
                queue.append(current_node.right)


sol = Solution()
root = TreeNode(1, TreeNode(2), TreeNode(3))
sol.display_dfs(root)
root = sol.invertTree(root)
sol.display_dfs(root)

