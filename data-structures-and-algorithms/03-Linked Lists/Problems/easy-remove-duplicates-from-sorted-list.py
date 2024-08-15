"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 
Example 1:

Input: head = [1,1,2]
Output: [1,2]
Example 2:

Input: head = [1,1,2,3,3]
Output: [1,2,3]


Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Time complexity O(n) - linear
        Space complexity O(1) - constant
        simple;
        Solution explained here:
        https://leetcode.com/problems/remove-duplicates-from-sorted-list/solutions/5641078/simple-python-best-possible-time-space-complexity/
        """

        temp = head
        while temp and temp.next:
            if temp.val == temp.next.val:
                temp.next = temp.next.next  # drops current next value
                continue  # we continue here to ensure that multiple same numbers (like 1, 1, 1) are caught and eliminated until we move to the next pointer.
            temp = temp.next

        return head


if __name__ == "__main__":

    linked_list = ListNode(1, ListNode(1, ListNode(1, ListNode(1, ListNode(1)))))
    solution = Solution()
    result = solution.deleteDuplicates(linked_list)
    temp = result
    while temp:
        print(temp.val)
        temp = temp.next
