"""
https://leetcode.com/problems/design-hashset/


Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:

void add(key) Inserts the value key into the HashSet.
bool contains(key) Returns whether the value key exists in the HashSet or not.
void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.


Example 1:

Input
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
Output
[null, null, null, true, false, null, true, null, false]

Explanation
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // return True
myHashSet.contains(3); // return False, (not found)
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // return True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // return False, (already removed)


Constraints:

0 <= key <= 106
At most 104 calls will be made to add, remove, and contains.

"""


class MyHashSet(object):
    """My solution, not very space efficient, but should generally be faster in doing operations
    All operations are O(1)
    Space complexity is 10**6 + 1
    """
    def __init__(self):
        self.hash_map = [False] * (10 ** 6 + 1)

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.hash_map[key] = True

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.hash_map[key] = False

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        return self.hash_map[key]




class MyHashSet(object):
    """
    Found on LC, using buckets, interesting approachs.
    Space wise it should be more efficient than mine.
    """

    NUM_BUCKETS = 2003  # or any appropriate number

    def __init__(self):
        self.buckets = [[] for _ in range(self.NUM_BUCKETS)]

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        mod = key % self.NUM_BUCKETS
        if key not in self.buckets[mod]:  # Fix potential syntax issues
            self.buckets[mod].append(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        mod = key % self.NUM_BUCKETS
        # Remove if it's present
        try:
            self.buckets[mod].remove(key)
        except ValueError:
            pass  # It's better to catch a specific error like ValueError
    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        mod = key % self.NUM_BUCKETS
        return key in self.buckets[mod]


class MyHashSet:
    """ Extremely efficient for dense sets, from chatgpt
    Uses bits to store that data
    I am not familiar with this type of operations so it may be worth it to learn at some point

        Efficient implementation using bit manipulation (bitset).
        Each bit in an integer represents whether a key is present in the set.
        This is a space-efficient solution for dense sets with a large key range.
    """

    def __init__(self):
        # The key range is 0 to 10^6, so we need a bitset large enough to store this many bits.
        # Each integer in Python holds 32 bits, so to store 10^6 keys, we need at least 10^6 // 32 integers.
        # `size = 10^6 + 1` to account for the upper bound, and we divide by 32 to get the number of integers.
        self.size = 10**6 + 1
        self.bitset = [0] * ((self.size >> 5) + 1)  # size // 32 is the same as size >> 5

    def add(self, key):
        """ Sets the bit corresponding to `key` to 1 (indicating the presence of the key in the set).
            key >> 5 gives the index of the integer in which the bit is stored.
            key & 31 gives the position of the bit within that integer.
        """
        # Calculate the index of the integer in which the bit for `key` is stored.
        # key >> 5 is equivalent to key // 32 (dividing key by 32).
        integer_index = key >> 5

        # Calculate the position of the bit within the integer. key & 31 is the same as key % 32.
        bit_position = key & 31

        # Set the bit at the calculated position using bitwise OR (|=) with the mask 1 << bit_position.
        # This turns the bit for the given key to 1 (indicating that the key is present).
        self.bitset[integer_index] |= (1 << bit_position)

    def remove(self, key):
        """ Clears the bit corresponding to `key` to 0 (indicating the absence of the key in the set).
            key >> 5 gives the index of the integer in which the bit is stored.
            key & 31 gives the position of the bit within that integer.
        """
        # Calculate the index of the integer in which the bit for `key` is stored.
        integer_index = key >> 5

        # Calculate the position of the bit within the integer. key & 31 is the same as key % 32.
        bit_position = key & 31

        # Create a mask by shifting 1 to the left by `bit_position` (1 << bit_position).
        # The bitwise NOT (~) inverts the mask, so all bits are 1 except the one for the given `key`.
        # Apply bitwise AND (&=) to clear the bit for the given key.
        self.bitset[integer_index] &= ~(1 << bit_position)

    def contains(self, key):
        """ Checks whether the bit corresponding to `key` is 1 (i.e., the key is present in the set).
            key >> 5 gives the index of the integer in which the bit is stored.
            key & 31 gives the position of the bit within that integer.
        """
        # Calculate the index of the integer in which the bit for `key` is stored.
        integer_index = key >> 5

        # Calculate the position of the bit within the integer. key & 31 is the same as key % 32.
        bit_position = key & 31

        # Check whether the bit at the calculated position is set to 1.
        # This is done using bitwise AND (&) with the mask 1 << bit_position.
        # If the result is not 0, the bit is set, so the key is present.
        return (self.bitset[integer_index] & (1 << bit_position)) != 0
# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
