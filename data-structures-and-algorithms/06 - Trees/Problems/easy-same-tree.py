"""
https://leetcode.com/problems/same-tree

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.



Example 1:


Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:


Input: p = [1,2], q = [1,null,2]
Output: false
Example 3:


Input: p = [1,2,1], q = [1,1,2]
Output: false


Constraints:

The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104

"""

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        THis is my original solution which tries to serialize the trees but it gets weird and complex quick, and has issues.
        The solution that i have below is done with GPT.
        """
        nodes_p = self.inOrderTraversalWithNoneNodes(p)
        nodes_q = self.inOrderTraversalWithNoneNodes(q)
        return nodes_p == nodes_q

    def inOrderTraversalWithNoneNodes(self, root):
        result = []

        def traverse(node):
            if node.left:
                if not node.left.left:
                    result.append(None)

                traverse(node.left)

                if not node.left.right:
                    result.append(None)
            result.append(node.val)
            # if node.right:
            if node.right:
                if not node.right.left:
                    result.append(None)
                traverse(node.right)
                if not node.right.right:
                    result.append(None)

        if root:
            traverse(root)
        return result

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        GPT solution.
        TC = O(n)
        SC = O(n) worst case, for a skewed tree. for a balanced tree it would be O(log n).
        """
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

if __name__ == "__main__":
    root1 = TreeNode(
        30,
        left=TreeNode(25, TreeNode(24), TreeNode(26)),
        right=TreeNode(35, TreeNode(34), TreeNode(36)),
    )

    root2 = TreeNode(
        30,
        left=TreeNode(25, TreeNode(24), TreeNode(26)),
        right=TreeNode(35, TreeNode(34), TreeNode(36)),
    )

    solution = Solution()
    print(solution.isSameTree(root1, root2))
