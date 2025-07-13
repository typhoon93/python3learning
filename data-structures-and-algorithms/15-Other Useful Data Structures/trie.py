"""
Why Autocomplete, URL routing, secret-key prefix matches.
Problem Design a Trie with insert/search/startsWith.
Design and implement a Trie (prefix tree) data structure that efficiently stores a dynamic set of strings and supports the following operations:
insert(word)
search(word) → bool
startsWith(prefix) → bool


Use-Case Examples: we built a trie with these inserted words:
["hello", "hell", "heaven", "goodbye"]
search("hell")	True	“hell” was inserted exactly.
startsWith("he")	True	Matches “hell”, “hello”, or “heaven”.
startsWith("goody")	False	No word starts with “goody”.

Time & Space Complexity
Time Complexity
insert(word): O(L)
search(word): O(L)
startsWith(prefix): O(P)
 where L is the length of the word and P is the length of the prefix.


Space Complexity
 In the worst case (no shared prefixes), storing N words of average length L takes O(N × L) memory for the Trie nodes and their child pointers.

"""

class TrieNode:
    """
    A node in the Trie structure.
    Each node maintains:
      - `children`: a dict mapping characters to subsequent TrieNodes
      - `is_end_of_word`: True if the path to this node spells a valid inserted word
    """

    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    """
    Implements a Trie (prefix tree) with the following methods:
      - insert(word):       Insert a word.
      - search(word):       Check if an exact word exists.
      - startsWith(prefix): Check if any word starts with the prefix.
    """

    def __init__(self):
        # The root does not hold any character itself.
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts the string `word` into the Trie.
        Time: O(len(word))
        """
        current_node = self.root
        for character in word:
            # If the character path doesn't exist, create a new node.
            if character not in current_node.children:
                current_node.children[character] = TrieNode()
            current_node = current_node.children[character]
        # Mark the terminal node as representing a complete word.
        current_node.is_end_of_word = True

    def _find_node(self, sequence: str) -> 'TrieNode | None':
        """
        Traverse the Trie following `sequence` character by character.
        Returns the final node if the path exists, else None.
        Time: O(len(sequence))
        """
        current_node = self.root
        for character in sequence:
            if character not in current_node.children:
                return None
            current_node = current_node.children[character]
        return current_node

    def search(self, word: str) -> bool:
        """
        Returns True if `word` was previously inserted into the Trie.
        """
        node = self._find_node(word)
        # Must both reach a node *and* have is_end_of_word == True
        return bool(node and node.is_end_of_word)

    def startsWith(self, prefix: str) -> bool:
        """
        Returns True if there is any inserted word
        that begins with `prefix`.
        """
        return self._find_node(prefix) is not None


test_cases = [
    ("insert", "hello", None),
    ("insert", "hell", None),
    ("insert", "heaven", None),
    ("insert", "goodbye", None),
    ("search", "hell", True),
    ("search", "hello", True),
    ("search", "hel", False),
    ("search", "good", False),
    ("search", "", False),
    ("startsWith", "he", True),
    ("startsWith", "hea", True),
    ("startsWith", "good", True),
    ("startsWith", "goody", False),
    ("startsWith", "", True),
]

trie = Trie()
for operation, argument, expected in test_cases:
    if operation == "insert":
        result = trie.insert(argument)
    elif operation == "search":
        result = trie.search(argument)
    elif operation == "startsWith":
        result = trie.startsWith(argument)
    try:
        assert result == expected
        print(f"Correct! operation={operation}, argument={argument!r} → got {result}, expected {expected}")
    except AssertionError:
        # Print WRONG in red (ANSI escape code \033[91m)
        print(
            f"\033[91mWRONG RESULT!!! operation={operation}, argument={argument!r} → got {result}, expected {expected}\033[0m")
