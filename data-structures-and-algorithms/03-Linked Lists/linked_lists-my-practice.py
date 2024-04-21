"""
Comparing it with a list - LL doesn't have an index;
A linked list is has nodes spread in memory, compared LIST where they are in contiguous memory (Consecutive blocks of memory allocated to user processes)
Linked list has a HEAD and TAIL, and each node points to the next, and the TAIL / LAST one points to NONE


Linked List BIG O:
append - O(1)
pop - remove from end - O(n)
prepend - add to start - O(1)
popfirst - remove from start - O(1)
insert- O(n)
remove = O(n)
lookup (value or index) - O(n)



POP and Lookup by index is better in lists
Pop or Prepend -> linked list is better


A linked list node is VALUE + Pointer;

it's essentially a dictionary (at least you can think about them that way), where
{
    "value":4,
    "next":None,
}
"""

###VIsual example of how linked lists work, using DICTIONARIES

# head = {
#     "value":4,
#     "next": {
#         "value":7,
#             "next": {
#                 #...
#                 }
#         }, 
# }

# print(head['next']['value']) 


###LInkedLIst

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
          
    
    def print_list(self):
        
        print("Current list is: [ ", end="")
        temp = self.head
        while temp is not None:
            print(temp.value, end=", ")
            temp = temp.next
        print("]", end="")
        print()
    
    def append(self, value):
        """adds an item to the end of the list"""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            
        self.length +=1
        return True
    
    def pop(self): #my own version, before video guide
        """removes an item from the end of the list"""
        if self.head is None:
            return None
        
        
        popped_value = self.tail
        if self.head == self.tail:
            self.head = None
            self.tail = None
            self.length -=1
            return popped_value
        
        current_value = self.head
        while current_value is not None:
            if current_value.next == popped_value:
                self.tail = current_value
                self.tail.next = None
                break
            current_value = current_value.next
        self.length -=1
        return popped_value
    
    def pop_2(self): #video guide code
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head

        while(temp.next):
            pre = temp
            temp = temp.next
        
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
            self.head = None
        return temp
            
    def prepend(self, value): #my own
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            return new_node
        new_node.next = self.head
        self.head = new_node
        return True
    
    def prepend_2(self, value): #video guide code
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length +=1
        return True
    
    def pop_first(self): #my own
        if self.head is None:
            return None
        
        popped_item = self.head
        if popped_item == self.tail:
            self.head == None
            self.tail == None

        self.head = popped_item.next
        popped_item.next = None
        self.length -=1
        return popped_item
    
    def pop_first_2(self): #video course code
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp
    
    def get(self, index):#mine
        if index >= self.length or index < 0:
            return None 
        current_index = 0
        temp = self.head
        while(temp.next):
            if current_index == index:
                return temp
            current_index += 1
            temp = temp.next
        return temp
    
    def get_2(self, index):#vid course
        if index >= self.length or index < 0:
            return None 
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self, index, value): #mine
        if index >= self.length or index < 0:
            return False
        temp = self.head
        for _ in range(index):
            temp = temp.next
        temp.value = value
        return True
        
    def set_value_2(self, index, value): #vid course
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):#mine
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        
        current_node_at_index = self.get(index)
        if current_node_at_index:
            temp = Node(current_node_at_index.value)
            temp.next = current_node_at_index.next
            current_node_at_index.value = value
            current_node_at_index.next = temp
            return True
        return False
    
    def insert_2(self, index, value): #vide course
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value) 
        new_node = Node(value)
        temp = self.get(index-1)
        new_node.next = temp.next
        temp.next = new_node
        self.length +=1
        return True
    
    def remove(self, index):#mine
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        temp = self.get(index-1)
        node_at_index = temp.next
        temp.next = node_at_index.next
        temp.next = None
        return node_at_index
    
    def remove_2(self, index):#vid course
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        prev = self.get(index-1)
        temp = temp.next
        prev.next = temp.next
        temp.next = None
        return temp
        
    def reverse(self): #mine
        if self.length == 0:
            return False
        new_list = LinkedList(self.pop().value)
        while self.length > 0:
            new_list.append(self.pop().value)
        self.head = new_list.head
        self.tail = new_list.tail
        return True
    
    def reverse_2(self): #video course
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
    
my_linked_list = LinkedList(1)
# my_linked_list.head = None
# my_linked_list.tail = None
# my_linked_list.length = 0
my_linked_list.append(2)
# my_linked_list.append(3)
# print(my_linked_list.remove(0))
result = my_linked_list.reverse_2()
my_linked_list.print_list()
