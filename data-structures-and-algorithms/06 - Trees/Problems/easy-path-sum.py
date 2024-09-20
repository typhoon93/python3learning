"""
https://leetcode.com/problems/path-sum/


Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

Example 1:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.
Example 2:

Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.
Example 3:

Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.


Constraints:

The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        My solution
        TC = O(n)
        SC = O(h) - height of binary tree
        -1000 <= Node.val <= 1000
        -1000 <= targetSum <= 1000
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        # not a binary search tree so nums can be anything on either side.
        # this means that we need to go through all paths and sub paths
        # preorder traversal where we keep track of sums left to right
        # once we reach a leaf, we check the sum;
        # if equal -> return true
        # if not equal, we subtract the current val, and return back one level, to check other levels.
        if not root:
            return False

        def check_has_path(node, current_total=0):
            current_total += node.val
            if not node.left and not node.right: # chck if equal to targetsum only if we have a leaf (no children)
                if targetSum == current_total:
                    return True
                else:
                    return False
            if node.left:
                has_path = check_has_path(node.left, current_total)
                if has_path:
                    return True
            if node.right:
                has_path = check_has_path(node.right, current_total)
                if has_path:
                    return True

            return False

        has_path = check_has_path(root)

        return has_path

    def hasPathSum(self, root, targetSum):
        """
        GPT solution, a bit more concise and clearer perhaps
        Determine if the binary tree has a root-to-leaf path with a sum equal to targetSum.

        Approach:
        - Use a recursive helper function to traverse the tree depth-first.
        - Accumulate the sum of node values along the path.
        - On reaching a leaf, check if the accumulated sum equals targetSum.

        Time Complexity: O(n), where n is the number of nodes, as we might visit all nodes.
        Space Complexity: O(h), where h is the maximum height of the tree, corresponding to the stack size in the worst case.

        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False

        def dfs(node, current_sum):
            if not node:
                return False
            current_sum += node.val
            # Check if it's a leaf node
            if not node.left and not node.right:
                return current_sum == targetSum
            # Otherwise, continue the path to the left and right
            return dfs(node.left, current_sum) or dfs(node.right, current_sum)

        return dfs(root, 0)

    def hasPathSum(self, root, targetSum):
        """
        USING recursion.
        Determine if the binary tree has a root-to-leaf path with a sum equal to targetSum using iterative DFS.

        Time Complexity: O(n), where n is the number of nodes in the tree.
        Space Complexity: O(h), where h is the height of the tree; this typically performs better in practice than recursion.

        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False

        stack = [(root, root.val)]
        while stack:
            current, curr_sum = stack.pop()

            # Check if it's a leaf node
            if not current.left and not current.right:
                if curr_sum == targetSum:
                    return True

            # Push children to stack with updated sums
            if current.right:
                stack.append((current.right, curr_sum + current.right.val))
            if current.left:
                stack.append((current.left, curr_sum + current.left.val))

        return False


sol = Solution()
root = TreeNode(1, (TreeNode(-1)))
target = 0
expected = True
result = sol.hasPathSum(root, target)
print(result)
print(f"{expected=}")
