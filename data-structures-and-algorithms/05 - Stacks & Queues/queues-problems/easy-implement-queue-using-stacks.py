"""
https://leetcode.com/problems/implement-queue-using-stacks

Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.
Notes:

You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.
 

Example 1:

Input
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 1, 1, false]

Explanation
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false
 

Constraints:

1 <= x <= 9
At most 100 calls will be made to push, pop, peek, and empty.
All the calls to pop and peek are valid.
 

Follow-up: Can you implement the queue such that each operation is amortized O(1) time complexity? In other words, performing n operations will take overall O(n) time even if one of those operations may take longer.


"""


class MyQueue:
    """
    My implementation
    TC:Pop is O(n), everything else is O(1);
    SC:  O(n)
    """

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s2.append(x)
        while self.s2:
            self.s1.append(self.s2.pop())

    def pop(self) -> int:
        return self.s1.pop()

    def peek(self) -> int:
        return self.s1[-1]

    def empty(self) -> bool:
        return not self.s1


"""
amortized analysis explanation (link): https://stackoverflow.com/questions/15079327/amortized-complexity-in-laymans-terms 
In an amortized analysis, the time required to perform a sequence of data-structure operations is averaged over all the operations performed... Amortized analysis differs from average-case analysis in that probability is not involved; an amortized analysis guarantees the average performance of each operation in the worst case.

(from Cormen et al., "Introduction to Algorithms")

That might be a bit confusing since it says both that the time is averaged, and that it's not an average-case analysis. So let me try to explain this with a financial analogy (indeed, "amortized" is a word most commonly associated with banking and accounting.)

Suppose that you are operating a lottery. (Not buying a lottery ticket, which we'll get to in a moment, but operating the lottery itself.) You print 100,000 tickets, which you will sell for 1 currency unit each. One of those tickets will entitle the purchaser to 40,000 currency units.

Now, assuming you can sell all the tickets, you stand to earn 60,000 currency units: 100,000 currency units in sales, minus the 40,000 currency unit prize. For you, the value of each ticket is 0.60 currency units, amortized over all the tickets. This is a reliable value; you can bank on it. If you get tired of selling the tickets yourself, and someone comes along and offers to sell them for 0.30 currency units each, you know exactly where you stand.

For the lottery purchaser, the situation is different. The purchaser has an expected loss of 0.60 currency units when they purchase a lottery ticket. But that's probabilistic: the purchaser might buy ten lottery tickets every day for 30 years (a bit more than 100,000 tickets) without ever winning. Or they might spontaneously buy a single ticket one day, and win 39,999 currency units.

Applied to datastructure analysis, we're talking about the first case, where we amortize the cost of some datastructure operation (say, insert) over all the operations of that kind. Average-case analysis deals with the expected value of a stochastic operation (say, search), where we cannot compute the total cost of all the operations, but we can provide a probabilistic analysis of the expected cost of a single one.

It's often stated that amortized analysis applies to the situation where a high-cost operation is rare, and that's often the case. But not always. Consider, for example, the so-called "banker's queue", which is a first-in-first-out (FIFO) queue, made out of two stacks. (It's a classic functional data-structure; you can build cheap LIFO stacks out of immutable single-linked nodes, but cheap FIFOs are not so obvious). The operations are implemented as follows:

put(x):  Push x on the right-hand stack.
y=get(): If the left-hand stack is empty:
           Pop each element off the right-hand stack and
             push it onto the left-hand stack. This effectively
             reverses the right-hand stack onto the left-hand stack.
         Pop and return the top element of the left-hand stack.
Now, I claim that the amortized cost of put and get is O(1), assuming that I start and end with an empty queue. The analysis is simple: I always put onto the right-hand stack, and get from the left-hand stack. So aside from the If clause, each put is a push, and each get is a pop, both of which are O(1). I don't know how many times I will execute the If clause -- it depends on the pattern of puts and gets -- but I know that every element moves exactly once from the right-hand stack to the left-hand stack. So the total cost over the entire sequence of n puts and n gets is: n pushes, n pops, and n moves, where a move is a pop followed by a push: in other words, the 2n operations (n puts and n gets) result in 2n pushes and 2n pops. So the amortized cost of a single put or get is one push and one pop.

Note that banker's queues are called that precisely because of the amortized complexity analysis (and the association of the word "amortized" with finance). Banker's queues are the answer to what used to be a common interview question, although I think it's now considered too well-known: Come up with a queue which implements the following three operations in amortized O(1) time:

1) Get and remove the oldest element of the queue,

2) Put a new element onto the queue,

3) Find the value of the current maximum element."""


class MyQueue:
    """
    TC: Amortized Analysis: O(1) for all.
    How this words:
        push - O(1), obvious.
        pop -  we check if we have an out_stack:
                in the out_stack, the items are aranged correctly so we use pop but get the oldest pushed element overall.
                if we do not have an out_stack, we move all in_stack elements to the out_stack. This will happen exactly once overall,
                until we have popped all the out_stack elements.
                Imagine if we had  [1, 2, 3] in the in stack, out stack is []. We want to pop from the queue now.
                out stack will become [3, 2, 1], and we will pop 1 from it, leaving it as [3, 2]; in stack is [].
                Overall, in this case the TC of pop was O(n).
                However, for the next 2 pops (as long as we have elements in the out stack), the pop will be O(1).
                That is the idea of the amortized O(1):
                    if we add 100 elements, we will only performed 100 operations in total. 100/100 = O(1)
                    If we then pop those elements, we will perform 200 operations in total (for the pop). 200/100 = O(2) -> O(1)
                    Some operations may have a very high cost, but on average it will come down O(1):
                        Imagine we add 100 elements first. Each operation for adding them costs 1.
                        If we do a pop after that, pop will cost 100 operations (that's the first pop).
                        But then, any other pop will cost only O(1).
                The key point for the amortized O(1) is this line:
                    if not self.out_stack;
        peek - same as pop
        empty - O(1)



    SC:  O(n)
    """

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()

    def peek(self) -> int:
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack


if __name__ == "__main__":
    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    obj.push(3)
    print(obj.in_stack)
    print(obj.peek())
    print(obj.pop())
    print(obj.in_stack)

    print(obj.empty())
