"""
https://leetcode.com/problems/merge-two-sorted-lists/

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

# import sys
# import os

# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# # from linked_lists_full_code_from_course import LinkedList, Node


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        Time Comlexity is O(n + m) where n and m are the length of the linked lists.
        Space complexity is O(1),  This is because it reuses the nodes of the input lists without allocating any new nodes;
        it only uses a fixed number of pointers (like new_head and new_list_current_pos).
        There are no additional data structures consuming space proportional to the size of the input lists.
        Therefore, the space complexity is constant
        """
        if not list1 or not list2:
            return list1 or list2

        new_head = None
        new_list_current_pos = None
        while list1:
            if not list2 or list1.val < list2.val:
                temp = list1
                list1 = list1.next
            else:
                temp = list2
                list2 = list2.next
            temp.next = None

            if not new_head:
                new_head = temp
                new_list_current_pos = new_head
            else:
                new_list_current_pos.next = temp
                new_list_current_pos = temp

        new_list_current_pos.next = list2
        return new_head

    def mergeTwoListsLEETCODESOLUTION(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        This is a solution I found in leetcode, it is shorter and more elegantly done than mine.
        It creates a dummy node to hold the head at it's next position, avoiding the last if in my while loop
        It also exits the while loop whenever any of the lists is exhausted, which is better approach than mine (i loop the whole list1 regardless if list2 is exhausted).
        While the O in mine and this are the same, this one is more efficient, specifically due to exiting the while loop earlier than me.
        """
        cur = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2

        if list1 or list2:
            cur.next = list1 if list1 else list2

        return dummy.next


if __name__ == "__main__":
    list1 = ListNode(1, ListNode(2, ListNode(4, None)))
    list2 = ListNode(1, ListNode(3, ListNode(4, None)))
    solution = Solution()
    result = solution.mergeTwoLists(list1, list2)
    temp = result
    while temp:
        print(temp.val)
        temp = temp.next
