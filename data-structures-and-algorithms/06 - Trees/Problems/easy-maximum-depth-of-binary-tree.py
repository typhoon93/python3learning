"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2


Constraints:

The number of nodes in the tree is in the range [0, 104].
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
    # def maxDepth(self, root):
    #     """
    #     My solution, recursive approach.
    #     TC = O(n), where n = all nodes
    #     SC = O(d), where d = depth
    #     :type root: TreeNode
    #     :rtype: int
    #     """
    #     # tree example:
    #     #         1
    #     #     1
    #     # 1
    #
    #     depth = 0
    #
    #     def traverse(node, depth):
    #         if not node:
    #             return depth
    #         depth += 1
    #         l_depth = traverse(node.left, depth)
    #         r_depth = traverse(node.right, depth)
    #         return max(l_depth, r_depth)
    #
    #     max_depth = traverse(root, depth)
    #     return max_depth
    def maxDepth(self, root):
        """
        My solution, iterative approach.
        TC = O(n), where n = all nodes
        SC = O(n), where n is the number of nodes
        :type root: TreeNode
        :rtype: int
        """
        # tree example:
        #         1
        #     1
        # 1
        depth = 0
        max_depth = 0
        if not root:
            return depth
        queue = deque([(root, depth+1)])
        while queue:
            current, depth = queue.popleft()
            if depth > max_depth:
                max_depth = depth
            if current.left:
                queue.append((current.left, depth+1))
            if current.right:
                queue.append((current.right, depth+1))

        return max_depth

    def maxDepth(self, root):
        """
        Iterative DFS approach with explicit stack. This is from GPT.
        Key difference between mine and the GPT solution is that:
            - it is doing DFS -> so it will store the deepest depth of the tree at most in the stack.
            - then it will pop it fully, and go to the right branch of it, doing the same.
            - in my case I will be storing the whole breadth of the tree (in the queue)
            Here's a convo i had with that will give a perspective:

            n a full binary tree of depth D, the total number of nodes is: 2*d -1
            if d = 10, nodes are 1023
            at the deepest level L, the nodes will be 512 (l=2**(d-1))
            in my queue algo, O will be about 512 (1/2 n == n)
            in the below algo, O will be 10
        TC = O(n)
        SC = O(d), where d is the depth of the tree
        """
        if not root:
            return 0

        max_depth = 0
        stack = [(root, 1)]  # Stack holds tuples of (node, current_depth)

        while stack:
            node, depth = stack.pop()
            if node:
                max_depth = max(max_depth, depth)
                # Push children onto the stack with incremented depth
                if node.left:
                    stack.append((node.left, depth + 1))
                if node.right:
                    stack.append((node.right, depth + 1))

        return max_depth



sol = Solution()
root = TreeNode(1, None, TreeNode(2))
expected = 2
print(sol.maxDepth(root))
print(f"{expected=}")
