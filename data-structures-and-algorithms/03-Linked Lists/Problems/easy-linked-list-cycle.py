"""
https://leetcode.com/problems/linked-list-cycle/

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

 

Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
Example 2:


Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
Example 3:


Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
 

Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.
 

Follow up: Can you solve it using O(1) (i.e. constant) memory?

"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycleInitial(self, head: Optional[ListNode]) -> bool:
        """
        Initial Solution, will try for space complexity O(1)
        Time complexity - O(n)
        Space complexity - O(n)
        """
        ids = set()
        hasCycle = False
        temp = head
        while temp:
            node_id = id(temp)
            if node_id in ids:
                hasCycle = True
                break
            ids.add(node_id)
            temp = temp.next

        return hasCycle

    def hasCycleSecond(self, head: Optional[ListNode]) -> bool:
        """
        This is my second solution.
        After my initial solution, I realized i can store all nodes as is in a set, instead of finding ids and checking them.
        The set contains only the pointers, and I preseumed this will not take up more space.
        After double checking I was wrong:
         - The hasCycleInitial stores in a set, and each would take up about 24 bytes
         - this funciton only stores references so on 64 bit system it will take up 8 bytes
        The difference is negligable and the complexity is the same.
        Time complexity - O(n)
        Space complexity - O(n)
        """
        nodes = set()
        hasCycle = False
        temp = head
        while temp:
            if temp in nodes:
                hasCycle = True
                break
            nodes.add(temp)
            temp = temp.next

        return hasCycle

    def hasCycleLeetCode(self, head: Optional[ListNode]) -> bool:
        """
        Solution from leetcode. Floyd's Cycle-Finding Algorithm
        The space complexity is O(1), time complexity O(n).
        Not intuitive for me, because although this saves up on space complexity, the pointers will probably loop through the list many times.
        We drop constants of course and time complexity remains O(n), but somehow intuitively i feel like it may approach n**2, so I never considered it.
        After double checking the logic, it seems that my intuitive understanding here is wrong, it is indeed O(n) for time complexity.
        Check this video for details:
        https://www.youtube.com/watch?v=S5TcPmTl6ww
        """
        slow_pointer = head
        fast_pointer = head
        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            if slow_pointer == fast_pointer:
                return True
        return False


if __name__ == "__main__":
    head = ListNode(1)
    node1 = ListNode(2)
    head.next = node1
    # node3 = ListNode(3)
    # node1.next = node3
    # node3.next = head

    solution = Solution()
    res = solution.hasCycleLeetCode(head)
    print(res)
