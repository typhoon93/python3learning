"""
double linked list vs linked list -> dll same as linked list, but also has prev pointer
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        
        
class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
            
    def append(self, value): #my code
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    def append_2(self, value): #course code
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self): #mine
        if self.length == 0:
            return None
        popped_item = self.tail
        self.tail = self.tail.prev
        if not self.tail: # only 1 object
            self.head = None 
        else:
            self.tail.next = None
        self.length -= 1
        popped_item.prev = None
        return popped_item
    def pop_2(self): #course code
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp
            
    
    
my_doubly_linked_list = DoublyLinkedList(7)
my_doubly_linked_list.append(3)
print(my_doubly_linked_list.pop_2())
print(my_doubly_linked_list.pop_2())
print(my_doubly_linked_list.pop_2())
my_doubly_linked_list.print_list()