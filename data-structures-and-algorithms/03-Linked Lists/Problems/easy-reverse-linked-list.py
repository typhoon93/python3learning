"""

Given the head of a singly linked list, reverse the list, and return the reversed list.



Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []


Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000


Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?


"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):
        """
        ITERATIVE.
        My implementation - disclosure - I knew this solution from my DSA course.
        TC = O(n)
        SC = O(1)
        :type head: ListNode
        :rtype: ListNode
        """
        temp = head
        before = None
        while temp:
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        return before

    def reverseList(self, head):
        """
        My recursive solution..
        TC = O(n)
        SC = O(n)
        :type head: ListNode
        :rtype: ListNode
        """

        def helper(prev, head):
            if head.next == None:  # reached end of LL
                head.next = prev
                return head
            else:
                next = head.next
                head.next = prev
                prev = head
                return helper(prev, next)

        if not head:
            return

        return helper(None, head)

    def reverseList(self, head):
        """GPT reversal with recursion"""
        if not head or not head.next:  # not head handles cases where we get an empty node; head.next case handles the case when we are at the last node
            return head
        p = self.reverseList(
            head.next)  # p will be new HEAD (aka always we return the last node here, it never changes once we return it
        head.next.next = head  # this is basically pointing the next nodes next value to the current node.
        head.next = None  # this is here for the pointing the NEXT value of the initial head (now tail) to None;
        # all recusion cases do it, but it is pointless for them,
        # since as the recursion unravels, they will point their next to the prev node in the previous line.
        # only the first recursive stack, the one where we had the original HEAD will keep this head.next=None

        return p  # this is the new head, the intial last node, it never changes after the base case return


if __name__ == "__main__":
    head = ListNode(1,
                    ListNode(2,
                             ListNode(3, )))

    expected = [4, 3, 2, 1]
    sol = Solution()
    res = sol.reverseList(head, )
    temp = res
    while temp:
        print(temp.val, end=", ")
        temp = temp.next
    print()
    print(expected)
