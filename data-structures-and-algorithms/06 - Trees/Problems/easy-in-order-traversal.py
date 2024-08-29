"""
https://leetcode.com/problems/binary-tree-inorder-traversal/
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:


Input: root = [1,null,2,3]
Output: [1,3,2]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
 

Follow up: Recursive solution is trivial, could you do it iteratively?

"""

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal_recursion(self, root: Optional[TreeNode]) -> List[int]:
        """Simple traverse solution with recursion.
        TC = O(n)
        SC = O(n); best case is O(log n), in a balanced tree. In that case the stack of recursion will be log n at its highest.
        It's height will be log n when traversing both sides. For space complexity we consider the highest point of memory used as the top,
        not the total memory used (because in essence we did 2*log n) stack.
        """
        result = []

        def traverse(node):
            if not node:
                return
            if node.left:
                traverse(node.left)
            result.append(node.val)
            if node.right:
                traverse(node.right)

        traverse(root)
        return result

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """Non recursive, while loop solution
        Took me a bit to come up with this, but very satisfying.
        Space complexity is O(n)
        Time complexity is O(n) as well.
        """
        result = []
        stack = []
        node = root
        while node:
            stack.append(node)
            if node.left:
                node = node.left
                continue
            else:
                while stack:
                    temp = stack.pop()
                    result.append(temp.val)
                    if temp.right:
                        node = temp.right
                        break
                    node = None

        return result

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Clearer and simplied solution, with a while loop.
        """

        result = []
        stack = []
        current = root

        while current or stack:
            # Reach the left most Node of the current Node
            while current:
                stack.append(current)
                current = current.left

            # Current must be None at this point
            current = stack.pop()
            result.append(current.val)  # Process the node
            current = current.right  # Move to the right node if available

        return result
if __name__ == "__main__":

    root = TreeNode(
        30,
        left=TreeNode(25, TreeNode(24), TreeNode(26)),
        right=TreeNode(35, TreeNode(34), TreeNode(36)),
    )

    solution = Solution()
    print(solution.inorderTraversal(root))
