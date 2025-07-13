"""
Disjoint Set Union
Disjoint Set Union or DSU.
Often it is also called Union Find because of its two main operations.
function based approach here:
https://cp-algorithms.com/data_structures/disjoint_set_union.html

✅ 1. Time Complexity
Simple DSU (No Path Compression)

    find_root(x):

        Worst-case: O(n) — In a chain-like tree, you may walk all the way up.

    union_sets(a, b):

        Calls find_root twice → O(n) in worst case.

DSU with Path Compression
    find_root(x):
        Nearly constant time: O(α(n)), where α is the inverse Ackermann function — grows extremely slowly.

    union_sets(a, b):
        Two find_root calls + constant work → still O(α(n)).

In practice, even for millions of elements, operations take effectively constant time.



NB! these can be further optimized by determing what is the best root to use, but i have nto implemented it!!

"""


class DisjointSetSimple:
    """
    Simple DSU (No Path Compression)
    Simple Union-Find WITHOUT path compression.
    Each element’s parent pointer is only updated on union;
    find_root always walks all the way up.
    """

    def __init__(self):
        # maps each element to its parent element
        self.parent_map: dict[str, str] = {}

    def find_root(self, element: str) -> str:
        """
        Return the root representative for `element`.
        If `element` is new, initialize its parent to itself.
        """
        # initialize new element
        if element not in self.parent_map:
            self.parent_map[element] = element

        # climb parent pointers until we find a self-parent
        current = element
        while self.parent_map[current] != current:
            current = self.parent_map[current]
        return current

    def union_sets(self, a: str, b: str) -> None:
        """
        Merge the sets containing `a` and `b` by making
        a’s root point to b’s root.
        constant time O(1) + whatever we have for for find_root
        """
        root_a = self.find_root(a)
        root_b = self.find_root(b)
        if root_a != root_b:
            self.parent_map[root_a] = root_b


class DisjointSetSimpleVerbose:
    def __init__(self):
        self.parent_map: dict[str, str] = {}

    def find_root(self, element: str) -> str:

        print(f"\n[find_root] Finding root of '{element}'")
        print(f"parent_map: {self.parent_map}")
        if element not in self.parent_map:
            self.parent_map[element] = element
            print(f"[init] '{element}' is new, setting parent to itself")

        current = element
        steps = []
        while self.parent_map[current] != current:
            steps.append(current)
            current = self.parent_map[current]

        print(f"[walk] Path followed: {' → '.join(steps)}")
        print(f"[result] Root of '{element}' is '{current}'")
        return current

    def union_sets(self, a: str, b: str) -> None:
        print(f"\n[union] Union '{a}' and '{b}'")
        root_a = self.find_root(a)
        root_b = self.find_root(b)

        if root_a != root_b:
            self.parent_map[root_a] = root_b
            print(f"[merge] Root '{root_a}' now points to root '{root_b}'")
        else:
            print(f"[skip] '{a}' and '{b}' are already in the same set")


class DisjointSetCompressed:
    """
    Disjoint Set Union with Path Compression.
    """

    def __init__(self):
        self.parent_map: dict[str, str] = {}

    def find_root(self, element: str) -> str:
        """
        Return the root of `element`, and compress the path:
        Make each node along the way point directly to the root.
        compressed version is O inverse ackerman; less than log n, less than even log log n

        """
        # If new, initialize to self-parent
        if element not in self.parent_map:
            self.parent_map[element] = element

        # Base case: If this element is the root, return it
        if self.parent_map[element] == element:
            return element

        # Recursive case: find root of parent, and assign it directly
        root = self.find_root(self.parent_map[element])  # Recursion
        self.parent_map[element] = root  # Path compression
        return root

    def union_sets(self, a: str, b: str) -> None:
        """
        Merge sets by connecting the root of one to the root of the other.
        constant time O(1) + whatever we have for for find_root
        """
        root_a = self.find_root(a)
        root_b = self.find_root(b)
        if root_a != root_b:
            self.parent_map[root_a] = root_b


class DisjointSetCompressedVerbose:
    def __init__(self):
        self.parent_map: dict[str, str] = {}

    def find_root(self, element: str) -> str:
        print(f"\n[find_root] Finding root of '{element}'")
        print(f"parent_map: {self.parent_map}")
        if element not in self.parent_map:
            self.parent_map[element] = element
            print(f"[init] '{element}' is new, setting parent to itself")

        if self.parent_map[element] == element:
            print(f"[base] '{element}' is its own root")
            return element

        print(f"[recurse] '{element}' points to '{self.parent_map[element]}', recursing...")
        root = self.find_root(self.parent_map[element])
        self.parent_map[element] = root
        print(f"[compress] Path compression: '{element}' now points directly to '{root}'")

        return root

    def union_sets(self, a: str, b: str) -> None:
        print(f"\n[union] Union '{a}' and '{b}'")
        root_a = self.find_root(a)
        root_b = self.find_root(b)

        if root_a != root_b:
            self.parent_map[root_a] = root_b
            print(f"[merge] Root '{root_a}' now points to root '{root_b}'")
        else:
            print(f"[skip] '{a}' and '{b}' are already in the same set")


ds = DisjointSetCompressedVerbose()
ds.union_sets("a", "b")
ds.union_sets("b", "c")
ds.find_root("a")
ds.find_root("b")