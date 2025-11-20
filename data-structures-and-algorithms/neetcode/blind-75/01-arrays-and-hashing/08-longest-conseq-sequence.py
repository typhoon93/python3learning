"""
https://neetcode.io/solutions/longest-consecutive-sequence
https://youtu.be/P6RZZMu_maU

Longest Consecutive Sequence

Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [2,20,4,10,3,4,5]

Output: 4

Explanation: The longest consecutive sequence is [2, 3, 4, 5].

Example 2:

Input: nums = [0,3,2,5,4,6,1,1]

Output: 7

Constraints:

    0 <= nums.length <= 1000
    -10^9 <= nums[i] <= 10^9



Recommended Time & Space Complexity

You should aim for a solution as good or better than O(n) time and O(n) space, where n is the size of the input array.

"""
from typing import List


def longestConsecutive_brute(nums: List[int]) -> int:
    """
    O(n*2), sc O(n)
    """
    res = 0
    store = set(nums)
    for num in nums:
        streak, curr = 0, num
        while curr in store:
            streak += 1
            curr += 1
        res = max(res, streak)
    return res


def longestConsecutive_sorting(nums: List[int]) -> int:
    """
    TC = O n log n
    SC = O(1)
    """
    if not nums:
        return 0
    res = 0
    nums.sort()  # in place

    curr, streak = nums[0], 0
    i = 0
    while i < len(nums):
        if curr != nums[i]:
            # reset
            curr = nums[i]
            streak = 0
        while i < len(nums) and nums[i] == curr:
            # go to next num
            i += 1
        streak += 1
        curr += 1
        res = max(res, streak)
    return res

from typing import List

def longestConsecutive_hashmap(nums: List[int]) -> int:
    """
    O(n) time and space.
    """
    num_set = set(nums)
    longest = 0
    for num in num_set:
        if (num - 1) not in num_set:  # only start counting at sequence start
            length = 1
            while (num + length) in num_set:
                length += 1
            longest = max(length, longest)
    return longest


def run_longest_consecutive_tests():
    GREEN = "\033[92m"
    RED = "\033[91m"
    RESET = "\033[0m"

    test_cases = [
        ([100, 4, 200, 1, 3, 2], 4),                 # 1,2,3,4
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),         # 0..8
        ([], 0),
        ([1], 1),
        ([1,2,0,1], 3),                              # 0,1,2
        ([9,1,-3,2,4,8,3,-1,6,-2,-4,7], 4),          # -4..2
        ([5,5,5,5], 1),                              # duplicates
        ([10,30,20], 1),                             # no consecutive chains
        ([2,1,4,3,6,5,7], 7),                        # 1..7
    ]

    print("Testing longestConsecutive_hashmap:\n")

    for i, (nums, expected) in enumerate(test_cases, 1):
        result = longestConsecutive_hashmap(nums)
        if result == expected:
            print(f"{GREEN}✅ Test {i}: nums={nums} → {result}{RESET}")
        else:
            print(f"{RED}❌ Test {i}: nums={nums} → {result} (expected {expected}){RESET}")


if __name__ == "__main__":
    run_longest_consecutive_tests()
