"""
 Container With Most Water - Explanation

https://neetcode.io/solutions/container-with-most-water
https://youtu.be/UuiTKBwPgAo

You are given an integer array heights where heights[i] represents the height of the ithith bar.

You may choose any two bars to form a container. Return the maximum amount of water a container can store.

Example 1:

Input: height = [1,7,2,5,4,7,3,6]

Output: 36

Example 2:

Input: height = [2,2,2]

Output: 4

Constraints:

    2 <= height.length <= 1000
    0 <= height[i] <= 1000

Recommended Time & Space Complexity

You should aim for a solution with O(n) time and O(1) space, where n is the size of the input array.

"""
from typing import List


def max_area_brute(height: List[int]) -> int:
    """
    SC = O(1)
    TC = O(n^2)
    """
    res = 0
    for l in range(len(height)):
        for r in range(l + 1, len(height)):
            area = (r - l) * min(height[l], height[r])  # width * height
            res = max(res, area)
    return res


def max_area_optimized(height: List[int]) -> int:
    """
    SC = O(1)
    TC = O(n) linear
    """
    res = 0
    l, r = 0, len(height) - 1
    while l < r:
        area = (r - l) * min(height[l], height[r])  # width * height
        res = max(res, area)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return res




def run_max_area_optimized_tests():
    GREEN = "\033[92m"
    RED   = "\033[91m"
    RESET = "\033[0m"

    test_cases = [
        ([1,7,2,5,4,7,3,6], 36),    # from prompt
        ([2,2,2], 4),               # flat bars
        ([1,1], 1),                 # minimum case
        ([1,2,3,4,5], 6),           # increasing heights
        ([5,4,3,2,1], 6),           # decreasing heights
        ([4,3,2,1,4], 16),          # symmetric
        ([1,8,6,2,5,4,8,3,7], 49),  # classic LC example
        ([0,0,0,0], 0),             # all zeros
        ([9,8,7,6,5,4,3,2,1], 20),  # optimal at far ends
    ]

    print("Testing max_area_optimized:\n")

    for i, (height, expected) in enumerate(test_cases, 1):
        result = max_area_optimized(height)
        if result == expected:
            print(f"{GREEN}✅ Test {i}: height={height} → {result}{RESET}")
        else:
            print(f"{RED}❌ Test {i}: height={height} → {result} (expected {expected}){RESET}")


if __name__ == "__main__":
    run_max_area_optimized_tests()


