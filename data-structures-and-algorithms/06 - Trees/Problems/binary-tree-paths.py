"""
https://leetcode.com/problems/binary-tree-paths

Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.



Example 1:


Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]
Example 2:

Input: root = [1]
Output: ["1"]


Constraints:

The number of nodes in the tree is in the range [1, 100].
-100 <= Node.val <= 100

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    # def binaryTreePaths(self, root):
    #     """
    #     My code
    #     SC = O(log n), height; + sc paths = num paths * height (paths)
    #     TC = O(n) in worst case scanario
    #     :type root: TreeNode
    #     :rtype: List[str]
    #     """
    #     paths = []
    #
    #     def traverse(current, path=[]):
    #         path = path[:] # O(n) complexity, needs optimization; this makes TC = O(n**2)
    #         path.append(str(current.val))
    #         if current.left is not None:
    #             traverse(current.left, path)
    #         if current.right is not None:
    #             traverse(current.right, path)
    #         if current.left is None and current.right is None:
    #             paths.append(path)
    #
    #     traverse(root)
    #     return ["->".join(path) for path in paths]
    #


    def binaryTreePaths(self, root):
        """
        Improved solution with help from GPT;
        this is similar to mine except we do not use a copy of the PATH to pass to the recursive calls.
        This decrases sc and tc; once we reach the end of the path, we turn it into strings and store it in PATHS
        we pop the last item of the path to ensure that the recursive stack backwards doesn't have unneeded nodes from prev calls.
        In this case only
        SC = O(n), each node is visited
        TC = O(n) in worst case scanario
        :type root: TreeNode
        :rtype: List[str]
        """
        paths = []

        def traverse(current, path = []):
            path.append(str(current.val))
            if current.left is not None:
                traverse(current.left)
            if current.right is not None:
                traverse(current.right)
            if not current.left and not current.right:
                path_str = "->".join(path) # O(n) complexity)
                paths.append(path_str)
            path.pop() # popping last element of path, as we have traversed it fully, and prev level of call stack won't need it

        traverse(root)

        return paths

sol = Solution()
root = TreeNode(1, TreeNode(2), TreeNode(3))
expected = ["1"]
print(sol.binaryTreePaths(root))
print("Expected: ", expected)
