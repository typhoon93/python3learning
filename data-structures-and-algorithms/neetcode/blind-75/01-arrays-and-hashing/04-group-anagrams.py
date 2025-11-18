"""
https://neetcode.io/solutions/group-anagrams
https://www.youtube.com/watch?v=vzdNOK2oB2E

https://www.youtube.com/watch?v=vzdNOK2oB2E
Description

Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

Example 2:

Input: strs = ["x"]

Output: [["x"]]

Example 3:

Input: strs = [""]

Output: [[""]]

Recommended Time & Space Complexity
You should aim for a solution with O(m * n) time and O(m) space, where m is the number of strings and n is the length of the longest string.

"""
from collections import defaultdict


def group_anagrams_sort(strs):
    """
    TC: O(m * n log n)
    SC: O(m * n)
    """
    res = defaultdict(list)
    for s in strs:
        sorted_s = "".join(sorted(s))
        res[sorted_s].append(s)

    return list(res.values())


def group_anagrams_optimal(strs):
    """
    TC: O(m * n) (* 26 but it is dropped as we drop constants)
    SC: O(m); O(m * n) extra space for the output list
    Where m is the number of strings and n is the length of the longest string.
    """
    res = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        res[tuple(count)].append(s)
    return list(res.values())



def run_group_anagrams_tests():
    GREEN = "\033[92m"
    RED = "\033[91m"
    RESET = "\033[0m"

    test_cases = [
        (["eat", "tea", "tan", "ate", "nat", "bat"],
         [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]),
        ([""], [[""]]),
        (["a"], [["a"]]),
        (["aa", "bb", "ab", "ba"], [["aa"], ["bb"], ["ab", "ba"]]),
        (["abc", "cab", "bca", "zzz"], [["abc", "cab", "bca"], ["zzz"]]),
        ([], []),
        (["x", "y", "z"], [["x"], ["y"], ["z"]]),
        (["dddd", "dd", "d", "ddd"], [["dddd"], ["dd"], ["d"], ["ddd"]]),
    ]

    print("Testing group_anagrams_optimal:\n")

    for i, (strs, expected) in enumerate(test_cases, 1):
        result = group_anagrams_optimal(strs)

        # Because order of groups and items inside groups may vary,
        # normalize by sorting sublists and the top-level list.
        normalize = lambda lst: sorted([sorted(group) for group in lst])
        if normalize(result) == normalize(expected):
            print(f"{GREEN}✅ Test {i}: strs={strs} → PASS{RESET}")
        else:
            print(f"{RED}❌ Test {i}: strs={strs}\n   result={result}\n   expected={expected}{RESET}")


if __name__ == "__main__":
    run_group_anagrams_tests()
