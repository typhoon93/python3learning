"""
https://leetcode.com/problems/design-hashmap/

Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

MyHashMap() initializes the object with an empty map.
void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.


Example 1:

Input
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
Output
[null, null, null, 1, -1, null, 1, null, -1]

Explanation
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // The map is now [[1,1]]
myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]


Constraints:

0 <= key, value <= 106
At most 104 calls will be made to put, get, and remove.


"""


class MyHashMap(object):
    buckets = 2003  # or any prime number
    """
    Worst Case space complexity is O n + m _;  n is buckets, m is the possible inputs.
    """

    def __init__(self):

        self.hash_map = [[] for _ in range(self.buckets)]

    def put(self, key, value):
        """
        Average is O(1) worst is O(n)
        :type key: int
        :type value: int
        :rtype: None
        """
        bucket = key % self.buckets
        for pair in self.hash_map[bucket]:
            if pair[0] == key:
                pair[1] = value
                return
        self.hash_map[bucket].append([key, value])

    def get(self, key):
        """
        Average is O(1) worst is O(n)
        :type key: int
        :rtype: int
        """
        bucket = key % self.buckets
        for k, v in self.hash_map[bucket]:
            if k == key:
                return v
        return -1

    def remove(self, key):
        """
        Average is O(1) worst is O(n)
        :type key: int
        :rtype: None
        """
        bucket = key % self.buckets
        for index, pair in enumerate(self.hash_map[bucket]):
            if pair[0] == key:
                self.hash_map[bucket].pop(index)
                return



class ListNode:
    def __init__(self, key, val, nxt):
        self.key = key
        self.val = val
        self.next = nxt


class MyHashMap:
    """
    LC implementation using Linked List, very cool design of PUT, check it.
    I knew about separate chaining using LL,  this is more elegant than the list method above i believe, so can be used if needed.
    """
    def __init__(self):
        self.size = 19997
        self.mult = 12582917
        self.data = [None for _ in range(self.size)]

    def hash(self, key):
        return key * self.mult % self.size

    def put(self, key, val):
        self.remove(key)
        h = self.hash(key)
        node = ListNode(key, val, self.data[h])
        self.data[h] = node

    def get(self, key):
        h = self.hash(key)
        node = self.data[h]
        while node:
            if node.key == key: return node.val
            node = node.next
        return -1

    def remove(self, key: int):
        h = self.hash(key)
        node = self.data[h]
        if not node: return
        if node.key == key:
            self.data[h] = node.next
            return
        while node.next:
            if node.next.key == key:
                node.next = node.next.next
                return
            node = node.next


# Your MyHashMap object will be instantiated and called as such:
key = 1
value = 1
obj = MyHashMap()
obj.put(key, value)
param_2 = obj.get(key)
print(param_2)
obj.remove(key)
