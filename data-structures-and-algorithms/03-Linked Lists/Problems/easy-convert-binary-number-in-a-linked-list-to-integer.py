"""
https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

The most significant bit is at the head of the linked list.



Example 1:


Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10
Example 2:

Input: head = [0]
Output: 0


Constraints:

The Linked List is not empty.
Number of nodes will not exceed 30.
Each node's value is either 0 or 1.

"""


class Solution(object):
    def getDecimalValue(self, head):
        """
        TC = O(n)
        SC = O(n)
        :type head: ListNode
        :rtype: int
        """
        binary_list = []
        current = head
        while current:
            binary_list.append(str(current.val))
            current = current.next
        binary_str = "".join(binary_list)
        return int(binary_str, 2)

    def getDecimalValue(self, head: ListNode) -> int:
        """
        A solution from LC, using binary conversion directly.
        TC = n
        SC = 1
        """

        answer = 0
        while head:
            answer = 2 * answer + head.val
            head = head.next
        return answer
