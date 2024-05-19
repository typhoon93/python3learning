"""
Analogy for stacks is a can of tennis balls.
Adding a tennis ball is pushing an item onto the stack.
The thing that makes a stack, a stack, is you can only get to the _last item_ you pushed onto the stack directly.
To get to previous ones, you need to remove tennis balls from the top.
The only item you can get to, is the one that is on top. This is coalled: LIFO.
LIFO definition: Last In, First Out

Example of stack usage:  
A web browser, where you visit Facebook, then Youtube, then Instagram, then Gmail. When you hit the back button, you pop items from the stack,
and you can only get to the previous one you went to. In order to get back to Facebook, you need to go through IG and YT first.

Common ways of implementing a stack:
1. Use a list -> for something to be a stack, you must only add and remove from one end. 
    Only pop and append (terminalogy is PUSH in the case of stack), or only prepend and popfirst; Pop and append (PUSH) are the most efficient, as their time complexity is O(1); 
    Prepend and popfirst require reindexing, so time complexity there is O(n) 

2. Use a linked list -> we will implement it using a LL so it is a bit more challenging; We will be popping and pushing from the HEAD of the stack,
as the complexity in this case is O(1) for popping and pushing; If we do it from the tail, the push is O(1), but the pop is O(n).
Additionally, the Stack has a TOP and BOTTOM instead of HEAD and TAIL respectively; since we do not use the bottom at all, it is not used.
So a STACK only has a TOP.

"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1
        # self.bottom = new_node

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self, value):  # mine
        new_node = Node(value)
        if not self.top:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        return True

    def push_2(self, value):  # mine
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1

    def pop(self):  # mine
        if not self.top:
            return None
        popped_item = self.top
        self.top = self.top.next
        popped_item.next = None
        self.height -= 1
        return popped_item

    def pop_2(self):  # cc
        if self.height == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp


my_stack = Stack(0)
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)

print(my_stack.pop())
my_stack.print_stack()
