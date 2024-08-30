"""

https://leetcode.com/problems/symmetric-tree/

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:

Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:


Input: root = [1,2,2,null,3,null,3]
Output: false


Constraints:

The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100


Follow up: Could you solve it both recursively and iteratively?

"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        Easy solution after finding the answer to easy-same-tree.py question.
        We use the same approch, but we check opposite nodes: left with right, and right with left respectively.
        TC = O(n)
        SC = O(log n) this is the worst case really, since we will stop the stack at the first non mirroring node, so it is possible for a skewed tree to fill the stack at all, on the skewed side
        """
        if not root:
            return True
        return self.is_mirror(root.left, root.right)

    def is_mirror(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        return self.is_mirror(left.left, right.right) and self.is_mirror(left.right, right.left)


    def isSymmetric_PreOrder(self, root: Optional[TreeNode]) -> bool:
        """
        Iterative solution
        General approach was mine but had help from GPT to get to this.
         traversing one subtree in normal pre-order (root-left-right) and the other subtree in mirrored pre-order (root-right-left)
        """
        if not root:
            return True

        stack_l = [root.left]
        stack_r = [root.right]

        while stack_l and stack_r:
            current_l = stack_l.pop()
            current_r = stack_r.pop()

            # Check if both nodes are None
            if not current_l and not current_r:
                continue

            # If one of them is None, or their values don't match, tree isn't symmetric
            if not current_l or not current_r or current_l.val != current_r.val:
                return False

            # Mirror push to stacks: left subtree's left with right subtree's right
            stack_l.append(current_l.left)
            stack_r.append(current_r.right)

            # Mirror push to stacks: left subtree's right with right subtree's left
            stack_l.append(current_l.right)
            stack_r.append(current_r.left)

        # If both stacks are empty, it means we have checked all corresponding nodes
        return len(stack_l) == 0 and len(stack_r) == 0

    def isSymmetric_level_order(self, root):
        """
        This is the most intuitive iterative approach I believe. From ChatGPT
        """
        from collections import deque

        if not root:
            return True
        queue = deque([(root.left, root.right)])
        while queue:
            left, right = queue.popleft()
            if not left and not right:
                continue
            if not left or not right:
                return False

            queue.append((left.left, right.right))

            queue.append((left.right, right.left))

        return True


if __name__ == "__main__":
    root = TreeNode(
        1,
        left=TreeNode(2, TreeNode(3), TreeNode(4)),
        right=TreeNode(2, TreeNode(4), TreeNode(3)),
    )

    solution = Solution()
    print(solution.isSymmetric(root))
