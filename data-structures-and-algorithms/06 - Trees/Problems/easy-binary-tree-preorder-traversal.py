"""
https://leetcode.com/problems/binary-tree-preorder-traversal/

Given the root of a binary tree, return the preorder traversal of its nodes' values.



Example 1:

Input: root = [1,null,2,3]

Output: [1,2,3]

Explanation:



Example 2:

Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

Output: [1,2,4,5,6,7,3,8,9]

Explanation:



Example 3:

Input: root = []

Output: []

Example 4:

Input: root = [1]

Output: [1]



Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100


Follow up: Recursive solution is trivial, could you do it iteratively?


"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        TC O(n)
        SC O(h)
        My solution, simple as i already know the algo
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if not root:
            return result

        def traverse(node):
            result.append(node.val)
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
        traverse(root)
        return result

    def preorderTraversal(self, root):
        """
        Iterative, again i know the algo
        once again sc is O(h) tc is O(n)
        """
        result = []
        if not root:
            return result
        stack = [root]


        while stack:
            current = stack.pop()
            result.append(current.val)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

        return result
