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

    def append(self, value):  # my code
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

    def append_2(self, value):  # course code
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

    def pop(self):  # mine (O(1))
        if self.length == 0:
            return None
        popped_item = self.tail
        self.tail = self.tail.prev
        if not self.tail:  # only 1 object
            self.head = None
        else:
            self.tail.next = None
        self.length -= 1
        popped_item.prev = None
        return popped_item

    def pop_2(self):  # course code
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

    def prepend(self, value):  # mine
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def prepend_2(self, value):  # cource code
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):  # my code
        # no items
        if self.length == 0:
            return None
        popped_item = self.head
        self.head = self.head.next
        if not self.head:  # only 1 item
            self.tail = None
        else:
            self.head.prev = None
        popped_item.next = None
        self.length -= 1
        return popped_item

    def pop_first_2(self):  # course code
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None

        self.length -= 1
        return temp

    def get(self, index):  # mine
        if index < 0 or index >= self.length:
            return None
        index_from_tail = abs(index - self.length) - 1
        temp = self.head
        direction = "next"
        if index > index_from_tail:  # determining shortest path to index
            temp = self.tail
            index = index_from_tail
            direction = "prev"
        for _ in range(index):
            temp = getattr(temp, direction)
        return temp

    def get_2(self, index):  # course
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length / 2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):  # start, stop, increment
                temp = temp.prev
        return temp

    def set_value(self, index, value):  # mine
        node = self.get(index)
        if node:
            node.value = value
            return True
        return False

    def set_value_2(self, index, value):  # course
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):  # mine
        if index < 0 or index > self.length:
            return False
        if index == 0:
            self.prepend(value)
            return True
        elif index == self.length:
            self.append(value)
            return True
        else:
            new_node = Node(value)
            current_at_index = self.get(index)
            before_current_at_index = current_at_index.prev
            new_node.next = current_at_index
            new_node.prev = before_current_at_index
            current_at_index.prev = new_node
            before_current_at_index.next = new_node
            self.length += 1
            return True

    def insert_2(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next
        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
        self.length += 1
        return True

    def remove(self, index):  # mine
        if index < 0 or index > self.length - 1:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        removed_node = self.get(index)
        removed_node.next.prev = removed_node.prev
        removed_node.prev.next = removed_node.next
        removed_node.next = None
        removed_node.prev = None
        self.length -= 1
        return removed_node

    def remove_2(self, index):  # course code
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()

        temp = self.get(index)
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.next = None
        temp.prev = None
        self.length -= 1
        return temp


my_doubly_linked_list = DoublyLinkedList(0)
my_doubly_linked_list.append(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)
# my_doubly_linked_list.append(5)
my_doubly_linked_list.remove(1)
# print(my_doubly_linked_list.pop_first_2())
# print(my_doubly_linked_list.pop_first_2())
# print(my_doubly_linked_list.pop_first_2())
# print(my_doubly_linked_list.pop_first_2())
# my_doubly_linked_list.set_value(3,1999)
my_doubly_linked_list.print_list()
