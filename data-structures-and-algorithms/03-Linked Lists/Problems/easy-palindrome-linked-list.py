"""
https://leetcode.com/problems/palindrome-linked-list/

Given the head of a singly linked list, return true if it is a
palindrome
 or false otherwise.



Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false


Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9


Follow up: Could you do it in O(n) time and O(1) space?


"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def isPalindrome(self, head):
        """
        My solution.
        TC = O(n)
        SC = O(1)
        :type head: ListNode
        :rtype: bool
        """
        # get to middle, reverse it from middle on out
        # then check if it's a palindrome
        lenght = 0
        current = head
        while current:
            lenght += 1
            current = current.next

        if lenght == 1 or lenght == 0:  # not necassary but code is faster with it in these cases.
            return True

        mid, remainder = divmod(lenght, 2)

        mid_head = head  # we get the mid point head
        for _ in range(mid + remainder):
            mid_head = mid_head.next

        back_head = self.reverseList(mid_head)  # we reverse the list from the mid to the end, and get the back head

        temp_back = back_head
        temp_front = head
        while temp_back:
            if temp_back.val != temp_front.val:
                # reverse the back_head list to ensure the list remains unchanged
                self.reverseList(back_head)
                return False
            temp_back = temp_back.next
            temp_front = temp_front.next

        # we reverse the back_head here
        self.reverseList(back_head)
        # this will ensure the linked list remains the same as they gave it to us
        # however, this is not strictly necessary as the exercise doesn't require it
        return True

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

def isPalindrome(self, head):
        """
        CHATGPT  solution using fast and slow pointers; this may be clearer to some devs,
        and we reduce some of the stuff from my code (like keeping track of length.
        TC and SC are same but it is slightly more optimized.
        Personally i find my own code more readable
        TC = O(n)
        SC = O(1)
        """
        if not head or not head.next:
            return True

        # Initialize slow and fast pointers
        slow = head
        fast = head

        # Find the middle of the list
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # If the list has an odd number of elements, move slow one step further
        if fast.next:
            slow = slow.next

        # Reverse the second half
        second_half = self.reverseList(slow)

        # Compare the two halves
        first_half = head
        while second_half:
            if first_half.val != second_half.val:
                # Restore the list before returning
                self.reverseList(slow)
                return False
            first_half = first_half.next
            second_half = second_half.next

        # Restore the list before returning
        self.reverseList(slow)
        return True


if __name__ == "__main__":
    head = ListNode(1,
                    ListNode(2,
                             ListNode(2,
                                      ListNode(1, ))))

    expected = True
    sol = Solution()
    res = sol.isPalindrome(head, )
    print(res)
    print("Expected: ", expected)
    temp = head
    while temp:
        print(temp.val, end=", ")
        temp = temp.next
