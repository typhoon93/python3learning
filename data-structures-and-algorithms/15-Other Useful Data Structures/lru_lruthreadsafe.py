"""
Design and implement a Least Recently Used (LRU) Cache data structure that supports the following operations in O(1) time complexity:
"""
import threading

class ListNode:
    def __init__(self, key: int, value: int):
        """
        Node of a doubly linked list, storing a key-value pair.
        """
        self.key = key
        self.value = value
        self.previous = None
        self.next = None

class LRUCacheThreadSafe:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache_map = {}  # Maps key -> ListNode
        self.current_size = 0
        self.lock = threading.Lock()

        # Create dummy head and tail to avoid edge checks
        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)
        self.head.next = self.tail
        self.tail.previous = self.head

    def get(self, key: int) -> int:
        with self.lock:
            if key not in self.cache_map:
                return -1

            node = self.cache_map[key]
            self._move_to_head(node)
            return node.value

    def put(self, key: int, value: int) -> None:
        with self.lock:
            if key in self.cache_map:
                # Update existing node and mark as recently used
                node = self.cache_map[key]
                node.value = value
                self._move_to_head(node)
            else:
                # Create new node and add to head
                new_node = ListNode(key, value)
                self.cache_map[key] = new_node
                self._add_to_head(new_node)
                self.current_size += 1

                # Evict if over capacity
                if self.current_size > self.capacity:
                    lru_node = self._pop_tail()
                    del self.cache_map[lru_node.key]
                    self.current_size -= 1

    def _add_to_head(self, node: ListNode):
        node.previous = self.head
        node.next = self.head.next
        self.head.next.previous = node
        self.head.next = node

    def _remove_node(self, node: ListNode):
        prev_node = node.previous
        next_node = node.next
        prev_node.next = next_node
        next_node.previous = prev_node

    def _move_to_head(self, node: ListNode):
        self._remove_node(node)
        self._add_to_head(node)

    def _pop_tail(self) -> ListNode:
        lru_candidate = self.tail.previous
        self._remove_node(lru_candidate)
        return lru_candidate


class LRUCache:
    def __init__(self, capacity: int):
        """
        Initialize the LRU cache with given positive capacity.
        """
        self.capacity = capacity
        self.cache_map = {}  # Maps key -> ListNode

        # Create dummy head and tail to avoid edge checks
        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)
        self.head.next = self.tail
        self.tail.previous = self.head

        self.current_size = 0

    def get(self, key: int) -> int:
        """
        Return the value if key exists; otherwise return -1.
        Also move the accessed node to the head (most recent).
        get(key)

        Returns the value associated with key if it exists in the cache; otherwise returns -1.

        Marks the accessed key as most recently used.

        """
        if key not in self.cache_map:
            return -1

        node = self.cache_map[key]
        self._move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        """
        Insert or update the key-value pair.
        If insertion causes capacity overflow, evict the least recently used node.
        put(key, value)

        Inserts a new key-value pair into the cache.

        If key already exists, updates its value and marks it as most recently used.

        If the cache is at full capacity, evicts the least recently used key before inserting
        """
        if key in self.cache_map:
            # Update existing node and mark as recently used
            node = self.cache_map[key]
            node.value = value
            self._move_to_head(node)
        else:
            # Create new node
            new_node = ListNode(key, value)
            self.cache_map[key] = new_node
            self._add_to_head(new_node)
            self.current_size += 1

            # Evict if over capacity
            if self.current_size > self.capacity:
                lru_node = self._pop_tail()
                del self.cache_map[lru_node.key]
                self.current_size -= 1

    def _add_to_head(self, node: ListNode):
        """
        Insert node right after dummy head.
        """
        node.previous = self.head
        node.next = self.head.next
        self.head.next.previous = node
        self.head.next = node

    def _remove_node(self, node: ListNode):
        """
        Unlink node from its current position.
        """
        prev_node = node.previous
        next_node = node.next
        prev_node.next = next_node
        next_node.previous = prev_node

    def _move_to_head(self, node: ListNode):
        """
        Move an existing node to the head (marking as most recent).
        """
        self._remove_node(node)
        self._add_to_head(node)

    def _pop_tail(self) -> ListNode:
        """
        Remove and return the node just before dummy tail
        (the least recently used).
        """
        lru_candidate = self.tail.previous
        self._remove_node(lru_candidate)
        return lru_candidate





def run_test_cases():
    test_cases = [
        # Example 1
        (
            ["LRUCache","put","put","get","put","get","get"],
            [[2],[1,1],[2,2],[1],[3,3],[2],[3]],
            [None, None, None, 1,    None,  -1, 3]
        ),
        # Eviction and overwrite behavior
        (
            ["LRUCache","put","put","put","put","get","get"],
            [[2],[2,1],[2,2],[1,1],[4,1],[1],[2]],
            [None, None, None, None, None, 1, -1]
        ),
        # Single-capacity edge cases
        (
            ["LRUCache","put","get","put","get","get"],
            [[1],[2,1],[2],[3,2],[2],[3]],
            [None, None,   1,    None,  -1,   2]
        ),
    ]

    for operations, arguments, expected_outputs in test_cases:
        cache = None
        actual_outputs = []
        for op, args in zip(operations, arguments):
            if op == "LRUCache":
                cache = LRUCache(*args)
                actual_outputs.append(None)
            elif op == "put":
                cache.put(*args)
                actual_outputs.append(None)
            elif op == "get":
                actual_outputs.append(cache.get(*args))

        if actual_outputs == expected_outputs:
            print(f"Correct! operations={operations}, arguments={arguments} → got {actual_outputs}, expected {expected_outputs}")
        else:
            print(f"\033[91mWRONG RESULT!!! operations={operations}, arguments={arguments} → got {actual_outputs}, expected {expected_outputs}\033[0m")

if __name__ == "__main__":
    run_test_cases()



def run_test_cases():
    test_cases = [
        # Example 1
        (
            ["LRUCache","put","put","get","put","get","get"],
            [[2],[1,1],[2,2],[1],[3,3],[2],[3]],
            [None, None, None, 1,    None,  -1, 3]
        ),
        # Eviction and overwrite behavior (corrected expected outputs)
        (
            ["LRUCache","put","put","put","put","get","get"],
            [[2],[2,1],[2,2],[1,1],[4,1],[1],[2]],
            [None, None, None, None, None, 1, -1]
        ),
        # Single-capacity edge cases
        (
            ["LRUCache","put","get","put","get","get"],
            [[1],[2,1],[2],[3,2],[2],[3]],
            [None, None,   1,    None,  -1,   2]
        ),
    ]

    for operations, arguments, expected_outputs in test_cases:
        cache = None
        actual_outputs = []
        for op, args in zip(operations, arguments):
            if op == "LRUCache":
                cache = LRUCache(*args)
                actual_outputs.append(None)
            elif op == "put":
                cache.put(*args)
                actual_outputs.append(None)
            elif op == "get":
                actual_outputs.append(cache.get(*args))

        if actual_outputs == expected_outputs:
            print(f"Correct! operations={operations}, arguments={arguments} → got {actual_outputs}, expected {expected_outputs}")
        else:
            print(f"\033[91mWRONG RESULT!!! operations={operations}, arguments={arguments} → got {actual_outputs}, expected {expected_outputs}\033[0m")

if __name__ == "__main__":
    run_test_cases()
