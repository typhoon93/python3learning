"""
Binary Heap Overview:
---------------------
A binary heap is a complete binary tree which must satisfy the heap property. It is used to implement priority queues and is crucial in various sorting and graph algorithms.

Properties:
- Each node can have at most two children.
- The heap can be categorized as a min-heap or max-heap:
  - Min-Heap: The value of each node is less than or equal to the values of its children. The root, therefore, is the minimum element in the heap.
  - Max-Heap: The value of each node is greater than or equal to the values of its children. The root, therefore, is the maximum element in the heap.
- It is a complete tree; all levels are completely filled except possibly for the last level, which is filled from left to right.

Why Binary Heap?
----------------
- Efficiently find the minimum or maximum element (depending on min-heap or max-heap) in O(log N) time.
- Ensure that insertion and deletion operations take no more than O(log N) time.

Comparison with Other Data Structures:
- Sorted Array:
  - Find Min/Max: O(1)
  - Insertion: O(n) – Not suitable for dynamic data where insertion is frequent.
- Linked List:
  - Find Min/Max: O(n)
  - Insertion: O(1) at beginning, but finding the correct position to maintain sorted order is O(n).

Binary Heap Practical Uses:
----------------------------
- Priority Queues: Managing tasks by priority, where tasks with higher priority are processed first.
- Graph Algorithms: Such as Prim's and Dijkstra's algorithm for finding the shortest path.
- Heap Sort: An efficient sorting algorithm utilizing the heap properties.

Types of Binary Heap:
- Min-Heap: Each parent node is less than or equal to its child nodes.
- Max-Heap: Each parent node is greater than or equal to its child nodes.

Implementation Options:
-----------------------
- Array Implementation: Preferred for binary heaps due to easy index calculation:
  - if we start at index 0:
    -Parent Index: If 'i' is greater than 0, parent(i) = (i - 1) // 2.
    -Left Child Index: left child(i) = 2i + 1.
    -Right Child Index: right child(i) = 2i + 2.
- Pointer/Reference Implementation: Uses nodes and pointers like a binary tree, less common for heaps due to the overhead of handling pointers.
"""

# Creation of Binary Heap
# Initialize fixed size List
# set size of BInary Heap to 0 -> when creating a blank list we create it with user input + 1,
# to make mathematical operations easier, since we will not use the index 0


class Heap:
    def __init__(self, size):
        self.size = size
        self.heap = []

    def parent(self, index):
        return (index - 1) // 2

    def left_child(self, index):
        return 2 * index + 1

    def right_child(self, index):
        return 2 * index + 2

    def has_parent(self, index):
        return self.parent(index) >= 0

    def has_left_child(self, index):
        return self.left_child(index) < len(self.heap)

    def has_right_child(self, index):
        return self.right_child(index) < len(self.heap)

    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, key):
        if len(self.heap) < self.size:
            self.heap.append(key)
            self.heapify_up(len(self.heap) - 1)
        else:
            raise Exception("Heap is full")

    def extract(self):
        if not self.heap:
            return None
        root_item = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapify_down(0)
        return root_item

    def peek(self):
        return self.heap[0] if self.heap else None

    def is_empty(self):
        return not self.heap

    def build_heap(self, elements):
        """
        build a heap from a list
        tc O(n)
        """
        if len(elements) > self.size:
            raise ValueError("More elements than the capacity of the heap.")
        self.heap = elements[:]
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self.heapify_down(i)


    def __str__(self):
        return str(self.heap)

    def heapify_up(self, index):
        raise NotImplementedError("Subclasses should implement this!")

    def heapify_down(self, index):
        raise NotImplementedError("Subclasses should implement this!")

    def __len__(self):
        return len(self.heap)


class MinHeap(Heap):
    def heapify_up(self, index):
        while self.has_parent(index) and self.heap[self.parent(index)] > self.heap[index]:
            self.swap(self.parent(index), index)
            index = self.parent(index)

    def heapify_down(self, index):
        while self.has_left_child(index):
            smaller_child_index = self.left_child(index)
            if self.has_right_child(index) and self.heap[self.right_child(index)] < self.heap[smaller_child_index]:
                smaller_child_index = self.right_child(index)
            if self.heap[index] < self.heap[smaller_child_index]:
                break
            else:
                self.swap(index, smaller_child_index)
                index = smaller_child_index


class MaxHeap(Heap):
    def heapify_up(self, index):
        while self.has_parent(index) and self.heap[self.parent(index)] < self.heap[index]:
            self.swap(self.parent(index), index)
            index = self.parent(index)

    def heapify_down(self, index):
        while self.has_left_child(index):
            larger_child_index = self.left_child(index)
            if self.has_right_child(index) and self.heap[self.right_child(index)] > self.heap[larger_child_index]:
                larger_child_index = self.right_child(index)
            if self.heap[index] > self.heap[larger_child_index]:
                break
            else:
                self.swap(index, larger_child_index)
                index = larger_child_index

heap = MaxHeap(5)
heap.insert(5)
heap.insert(3)
heap.insert(51)
heap.insert(1)
print(heap)
heap.extract()
print(heap)
