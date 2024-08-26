"""
https://leetcode.com/problems/implement-stack-using-queues/

Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
Notes:

You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.
 

Example 1:

Input
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 2, 2, false]

Explanation
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False
 

Constraints:

1 <= x <= 9
At most 100 calls will be made to push, pop, top, and empty.
All the calls to pop and top are valid.
 

Follow-up: Can you implement the stack using only one queue?

"""

from collections import deque


class MyStack:
    """My solution
    Push is O(1)
    TOP shouldn't be implemented that way - we should use PEEK type of TOP, where we get element 0 of the queue. If I implement it correctly and leavery elese the same, it would be O(n)
    POP is O(n)
    the solution of GPT is more elegant and simpler, and TOP being O(1) makes it much better
    """

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        main_q, _ = self.get_main_and_secondary_queue()
        main_q.append(x)

    def pop(self) -> int:
        main_q, secondary_q = self.get_main_and_secondary_queue()
        while len(main_q) > 1:
            secondary_q.append(main_q.popleft())
        return main_q.popleft()

    def top(self) -> int:
        main_q, _ = self.get_main_and_secondary_queue()
        return main_q[-1]

    def empty(self) -> bool:
        main_q, _ = self.get_main_and_secondary_queue()
        if len(main_q) == 0:
            return True
        return False

    def get_main_and_secondary_queue(self):
        if len(self.q1) > len(self.q2):
            main_q = self.q1
            secondary_q = self.q2
        else:
            main_q = self.q2
            secondary_q = self.q1
        return main_q, secondary_q


class MyStack:
    """GPT solution
    Push is O(n), everything else O(1)
    """

    def __init__(self):
        self.q1 = deque()  # primary queue
        self.q2 = deque()  # secondary queue used during push operation

    def push(self, x: int) -> None:
        """TC = O(n)"""
        # First, push to the empty secondary queue
        self.q2.append(x)
        # Transfer all elements from q1 to q2
        while self.q1:
            self.q2.append(self.q1.popleft())
        # Swap q1 and q2 to make sure the last added element is always at the front of q1
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        # Pop from the front of q1, which is the last pushed element
        return self.q1.popleft()

    def top(self) -> int:  # == PEEK
        # The front of q1 is the last element pushed, hence the top of the stack. PEEK.
        return self.q1[0]

    def empty(self) -> bool:
        # Check if q1 is empty
        return not self.q1


class MyStack:
    """My solution, 1 queue
    Push is O(n), everything else O(1)"""

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        """TC = O(n)"""

        self.q.append(x)
        """O(n)"""
        for _ in range(
            len(self.q) - 1
        ):  # arrange the queue so last element we added is on top.
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        """O(1)"""
        return self.q.popleft()

    def top(self) -> int:  # == PEEK
        # The front of q1 is the last element pushed, hence the top of the stack. PEEK.
        return self.q[0]

    def empty(self) -> bool:
        # Check if q1 is empty
        return not self.q


# Your MyStack object will be instantiated and called as such:
if __name__ == "__main__":
    obj = MyStack()
    obj.push(1)
    obj.push(2)
    print(obj.top())
    print(obj.pop())
    print(obj.empty())
