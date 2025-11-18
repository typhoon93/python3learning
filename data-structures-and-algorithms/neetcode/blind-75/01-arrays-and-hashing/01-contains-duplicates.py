"""
Contains Duplicate
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
Example 1:
Input: nums = [1, 2, 3, 3]
Output: true
Example 2:
Input: nums = [1, 2, 3, 4]
Output: false

Recommended Time & Space Complexity

You should aim for a solution with O(n) time and O(n) space, where n is the size of the input array.

# https://www.youtube.com/watch?v=3OamzN90kPg&t=15s
https://leetcode.com/problems/contains-duplicate/

# Approaches discussed:
- brute force, check each number against each, TC: (O n**2), SC: O(1)
- sorting, then go through the whole array and check adjacent items, O (n log n + n) + space = O(1)
- hash set, TC: SC and TC both O(n)
"""


def contains_duplicate(nums):
    """
    Write the hash set approach
    # Approaches discussed:
    - brute force, check each number against each, TC: (O n**2), SC: O(1)
    - sorting, then go through the whole array and check adjacent items, O (n log n + n) + space = O(1)
    - hash set, TC: SC and TC both O(n)
    what is optimal? depends on your needs!
    """
    hashset = set()
    for n in nums:
        if n in hashset:
            return False
        hashset.add(n)
    return True



def run_contains_duplicate_tests():
    GREEN = "\033[92m"
    RED = "\033[91m"
    RESET = "\033[0m"

    test_cases = [
        ([1, 2, 3, 4], True),
        ([1, 2, 3, 1], False),
        ([], True),
        ([5], True),
        ([7, 7, 7, 7], False),
        ([1, 2, 3, 4, 5, 6, 2], False),
        (list(range(10000)), True),
        ([0, -1, -2, -3, -1], False),
        ([10, 20, 30, 40], True),
    ]

    print("Testing contains_duplicate:\n")

    for i, (nums, expected) in enumerate(test_cases, 1):
        result = contains_duplicate(nums)
        if result == expected:
            print(f"{GREEN}✅ Test {i}: nums={nums[:10]}... → {result} (expected: {expected}){RESET}")
        else:
            print(f"{RED}❌ Test {i}: nums={nums[:10]}... → {result} (expected: {expected}){RESET}")


if __name__ == "__main__":
    run_contains_duplicate_tests()