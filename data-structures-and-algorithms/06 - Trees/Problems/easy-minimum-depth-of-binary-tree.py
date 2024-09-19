"""
https://leetcode.com/problems/minimum-depth-of-binary-tree/

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 2
Example 2:

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5


Constraints:

The number of nodes in the tree is in the range [0, 105].
-1000 <= Node.val <= 1000


"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def minDepth(self, root):
        """
        My solution.
        SC = O(h) - max height
        TC = O(n) - nodes
        :type root: TreeNode
        :rtype: int
        """
        #        1
        #    1
        # 1
        # answer = 3
        # return case - node that is a left =>  left / right is None
        #
        depth = 0

        def traverse(node, depth):
            if not node:
                return depth

            l_depth, r_depth = None, None
            depth += 1
            if not node.left and not node.right:
                return depth
            if node.left:
                l_depth = traverse(node.left, depth)
            if node.right:
                r_depth = traverse(node.right, depth)

            if l_depth and r_depth:
                return min(l_depth, r_depth)
            else:
                return l_depth if l_depth else r_depth

        min_depth = traverse(root, depth)
        return min_depth

    def minDepth(self, root):
        """
        GPT solution, clearer and more concise.
        """
        if not root: # this really handling the empty tree case, we will never enter this if there is an actual node in the tree
            return 0

        if not root.left and not root.right:  # left and right are leafs, this is our ideal case, this is really the depth we are searching
            return 1

        if not root.left: # we branch to the right since no root left;
            # we will enter this case only when there is a root.right, bacause of the previous check ->
            # if there was no root.right, we would have returned 1 by now
            return 1 + self.minDepth(root.right)

        if not root.right: # we branch to the left since no root right
            # we will enter this case only when there is a root.left, bacause of the previous checks ->
            # if there was not root left, we would have return 1 by now in one of the base cases
            return 1 + self.minDepth(root.left)

        # this is the case when left and right are both present.
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

sol = Solution()
root = TreeNode(1, TreeNode(2))
expected = True
print(sol.minDepth(root))
print(f"{expected=}")
