"""

### INTRO
Linked list is just a Tree that doesn't fork (the node in a Tree is different, it has left and right pointers.)

A Tree with nodes that have left and right pointers, is called a BINARY tree
Trees do not have to be BINARY, each node can point to any number of nodes depending on our design.
We will build a binary tree.

Tree types (binary specific examples, but concepts transfer to trees with more pointers):

Full - every node either points to ZERO nodes or TWO
Perfect - a full tree, any level on the tree that has any nodes, it is completely filled all the way across
Complete - a tree that is filled from left to right with no gaps; 


Subnodes are children; the one they originate from are called parents
Child nodes that share the same parent are SIBLINGS:
Every node can have one parent, if a node has multiple parents, it is not a tree.
A node without children is a LEAF

#### BINARY SEARCH TREE

With a binary search tree, if a number is greater than the parent, it goes to the RIGHT of that node, if it's less than the parent node, it goes on the LEFT of that node.
If there's already a node on the LEFT on the right, we compare the new number to that node; we do this repeatedly, until we can place the new node correctly

In a binary search tree, if you take ANY node, all nodes below it to the RIGHT, are going to be GREATER than that node;
In a binary search tree, if you take ANY node, all nodes below it to the LEFT, are going to be LESS than that node;


#### Binary Search TREE Big O
Search, remove and add - all are O(log n) - very efficient; divide and conquer;
Compared to a linked list:
    search is O(n)
    remove by value is O(n)
    insert (append) -> O(1) 
    
In a binary search tree class constructor, the only thing that we have is a ROOT (equivalent of Linked Lists HEAD)

"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value):  # mine
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:  # case of equal nodes
                return False
            if new_node.value > temp.value:  # case when node a bigger num
                if temp.right == None:
                    temp.right = new_node
                    return True
                temp = temp.right
                continue
            if temp.left == None:  # case when node a smaller num
                temp.left = new_node
                return True
            temp = temp.left

    def contains(self, value):  # mine
        if self.root == None:
            return False
        temp = self.root
        while True:
            if value == temp.value:
                return True
            if value > temp.value:  # bigger than case
                if temp.right == None:
                    return False
                temp = temp.right
                continue
            if temp.left == None:  # smaller than case
                return False
            temp = temp.left


my_tree = BinarySearchTree()
my_tree.insert(2)
my_tree.insert(1)
my_tree.insert(3)
print(my_tree.root.value)
# print(my_tree.root.left.value)
print(my_tree.root.right.value)
print(my_tree.contains(3))
