"""
https://leetcode.com/problems/remove-linked-list-elements

Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

Example 1:


Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
Example 2:

Input: head = [], val = 1
Output: []
Example 3:

Input: head = [7,7,7,7], val = 7
Output: []


Constraints:

The number of nodes in the list is in the range [0, 104].
1 <= Node.val <= 50
0 <= val <= 50


"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeElements(self, head, val):
        """
        My solution
        TC = O(n)
        SC = O(1)
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        temp = head
        prev = None
        while temp:
            if temp.val == val: # needs to be removed
                if prev == None: # head is val
                    head = temp.next
                    temp = head
                    continue
                else:
                    prev.next = temp.next
                    temp = temp.next
                    continue
            # doesn't need to be removed so we just move
            prev = temp
            temp = temp.next

        return head

    def removeElements(self, head, val):
        """
        Clearer, GPT solution with dummy node
        TC = O(n)
        SC = O(1)
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        return dummy.next

if __name__ == "__main__":
    head = ListNode(7,
                    ListNode(2,
                             ListNode(2,
                                      ListNode(7,
                                               ))))

    remove = 2
    expected = []
    sol = Solution()
    res = sol.removeElements(head, remove)
    temp = res
    while temp:
        print(temp.val, end=", ")
        temp = temp.next
    print()
    print(expected)
