"""
Queue principle is FIFO = which means First In First Out

Adding people to the queue, we use the term ENQUEUE.
When we remove people from the queue, we use the term DEQUEUE;

For something to be a QUEUE, we add on one end, and remove on the other end.

Data Structures to create a QUEUE:
List - add (append) is O(1); removing is O(n); basically one process is O(n), the other is O(1
Linked List - Adding/Removing from HEAD is O(1); Adding from tail is O(1), but removing is O(n)
THe best flow is to Add from the TAIL and remove from the HEAD -both will be O(1);
For queues, we change the node HEAD to be called FIRST (dequeue from this end), and the TAIL is called LAST (enqueue from this end)
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def enqueue(self, value):  # mine
        new_node = Node(value)
        if not self.first:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None

        dequeued_node = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            dequeued_node.next = None
        self.length -= 1
        return dequeued_node


my_queue = Queue(0)
my_queue.enqueue(1)
my_queue.enqueue(2)

# my_queue.enqueue(1)
my_queue.dequeue()
my_queue.dequeue()
my_queue.dequeue()

# my_queue.dequeue()
my_queue.print_queue()
