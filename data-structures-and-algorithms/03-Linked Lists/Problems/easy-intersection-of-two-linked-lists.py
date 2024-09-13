"""
https://leetcode.com/problems/intersection-of-two-linked-lists

Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

For example, the following two linked lists begin to intersect at node c1:


The test cases are generated such that there are no cycles anywhere in the entire linked structure.

Note that the linked lists must retain their original structure after the function returns.

Custom Judge:

The inputs to the judge are given as follows (your program is not given these inputs):

intersectVal - The value of the node where the intersection occurs. This is 0 if there is no intersected node.
listA - The first linked list.
listB - The second linked list.
skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.
The judge will then create the linked structure based on these inputs and pass the two heads, headA and headB to your program. If you correctly return the intersected node, then your solution will be accepted.



Example 1:


Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'
Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
- Note that the intersected node's value is not 1 because the nodes with value 1 in A and B (2nd node in A and 3rd node in B) are different node references. In other words, they point to two different locations in memory, while the nodes with value 8 in A and B (3rd node in A and 4th node in B) point to the same location in memory.
Example 2:


Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Intersected at '2'
Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.
Example 3:


Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: No intersection
Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.


Constraints:

The number of nodes of listA is in the m.
The number of nodes of listB is in the n.
1 <= m, n <= 3 * 104
1 <= Node.val <= 105
0 <= skipA < m
0 <= skipB < n
intersectVal is 0 if listA and listB do not intersect.
intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect.


Follow up: Could you write a solution that runs in O(m + n) time and use only O(1) memory?


"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution(object):
    # def getIntersectionNode(self, headA, headB):
    #     """
    #     Initial solution -
    #     TC = O(n**2)
    #     SC = O(1)
    #     :type head1, head1: ListNode
    #     :rtype: ListNode
    #     """
    #     if not headA or not headB:
    #         return None
    #     temp1 = headA
    #     while temp1:
    #         temp2 = headB
    #         while temp2:
    #             if id(temp1) == id(temp2):
    #                 return temp1
    #             temp2 = temp2.next
    #         temp1 = temp1.next
    #     # no intersect
    #     return None
    #
    # def getIntersectionNode(self, headA, headB):
    #     """
    #     Second solution
    #     TC = O(n+m)
    #     SC = O(n)
    #     :type headA, headB: ListNode
    #     :rtype: ListNode
    #     """
    #     if not headA or not headB:
    #         return None
    #     memory_ids = set()
    #     temp = headA
    #     while temp:
    #         memory_id = id(temp)
    #         memory_ids.add(memory_id)
    #         temp = temp.next
    #     temp = headB
    #     while temp:
    #         memory_id = id(temp)
    #         if memory_id in memory_ids:
    #             return temp
    #         temp = temp.next
    #     # no intersect
    #     return None


    def getIntersectionNode(self, headA, headB):
        """
        Most efficient solution, from leetcode;

        Visualization:

        Linked Lists:
        headA = A1 → A2 → C1 → C2 → C3 → None
        headB = B1 → B2 → B3 → C1 → C2 → C3 → None

        With our algo, the pointer traverses this:
        pointerA = A1 → A2 → C1 → C2 → C3 → B1 → B2 → B3 → C1 → C2 → C3 → None
        pointerB = B1 → B2 → B3 → C1 → C2 → C3 → A1 → A2 → C1 → C2 → C3 → None

        Notice the lenght of the lists are the same, and they meet exactly at the start of the intersection.

        The closing condition - if there is no intersection -> they will meet at None.


        TC = O(n+m)
        SC = O(1)
        :type headA, headB: ListNode
        :rtype: ListNode
        """

        pointerA, pointerB = headA, headB

        while pointerA is not pointerB:
            pointerA = pointerA.next if pointerA else headB
            pointerB = pointerB.next if pointerB else headA

        return pointerA

if __name__ == "__main__":
    intersect_node = ListNode(8,
                              ListNode(4,
                                       ListNode(5)))
    headA = ListNode(4, ListNode(1,
                                 intersect_node))

    headB = ListNode(5, ListNode(6,
                                 ListNode(1,
                                          intersect_node)
                                 ))

    sol = Solution()
    result = sol.getIntersectionNode(headA, headB)
    print(result.val)
    print("Expected", intersect_node.val)
    # temp = headA
    # while temp:
    #     print(temp.val)
    #     temp=temp.next
