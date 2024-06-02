"""
#Hash Tables 

Build in hash tables: dictionaries - made out of key value pairs.
Hash tables need a hash function, and we perform a hash on the key; In addition to getting our key back, we also get an address back.
That address is where we store our key / value pair.

Hash charecteristics: 
1. It is one way. - we cannot reverse it.
2. It is deterministic - every time we put a specific input, we get the same output for that specific input.

{
    "nails": 1000
}

We will create our own address space by creating a list, and we will create methods for setting items (key value pairs) etc.
The hash will return our key value pair, and a specific address on the list; then we will save our original key value pair inside that list.

Collision - if we have key/value pairs that map to the same address, we have multiple options:
1. Seperate chaining - we just put them on the same address (list within a list)
2. Linear Probing (a form of open addressing) - We go down until we find an empty address and put the K/V pair there; we keep going down until we find an empty address.
3. Instead of having lists stored at those hash returned addresses, we have linked lists and have a next value for each.

Constructor:

1. We should always have a PRIME number of TOTAL addresses (the last address is only devisable by itself and 1). Why?
Because it increases the amount of randomnes of how the K/V pairs will be distributed through the hash table, so it reduces COLLISIONS; there is more
even distribution;
2. Constructor is basically going to build the address space of the hash table, so we only need SIZE as an argument

class HashTable:
    def __init__(self, size=7) -> None:
        self.data_map = [None] * size

## Hash Table Big O
1. __hash - O(1) - because we will always have a set number of letters in a key, which means a set number of operations calculating the hash.
2. set_item - O(1)
3. get_item - O(1) - worst case scenario might be O(n) (if all keys collide) -> but the assumption with hash tables is that the distribution will be even and random

## Interview Question

We have a list of l1 = [1, 3, 4] and l2 = [2, 4, 5]; find if they have a common item (return True or False);

Approach 1 (interviewer won't like it, because we have O(n*2)) - 2 for loops, or using "in" to compare all items with each other;

Approach 2 (The answer you should give is one that has O(n) (really O(2n) but we drop constants)): use a dictionary as in this method:


def has_same_item(l1, l2):
    all_items_dict = {}
    for item in l1:
        all_items_dict[item] = True

    for item in l2:
        if item in all_items_dict:
            return True
    return False


"""


class HashTable:
    def __init__(self, size=7) -> None:
        self.data_map = [None] * size

    def __hash(self, key):
        """
        ord(letter) gets the asci number for each letter as we are looping through it;
        multiplying by 23 - because 23 is a prime number; we can put any prime number here; again helps with randomness and less collisions.
        % - modulo, so it gives us the REMAINDER after the division;
        """
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):  # mine
        index = self.__hash(key)
        if self.data_map[index] == None:
            return None
        for pair in self.data_map[index]:
            if pair[0] == key:
                return pair
        return None

    def get_item_2(self, key):  # from course
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i]

        return None

    def keys(self):  # mine
        keys = []
        for pairs in self.data_map:
            if pairs:
                for pair in pairs:
                    keys.append(pair[0])
        return keys

    def keys_2(self):  # course code
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])

        return all_keys

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)


my_hash_table = HashTable()

my_hash_table.set_item("bolts", 1400)
my_hash_table.set_item("washers", 50)
my_hash_table.set_item("lumber", 70)
print(my_hash_table.keys_2())


l1 = [1, 3, 7]
l2 = [2, 4, 5]


def has_same_item(l1, l2):
    all_items_dict = {}
    for item in l1:
        all_items_dict[item] = True

    for item in l2:
        if item in all_items_dict:
            return True
    return False


print(has_same_item(l1, l2))
