"""
https://youtu.be/bNvIQI2wAjk

Description
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].
Each product is guaranteed to fit in a 32-bit integer.
Follow-up: Could you solve it in O(n)O(n) time without using the division operation?

Example 1:
Input: nums = [1,2,4,6]
Output: [48,24,12,8]

Example 2:
Input: nums = [-1,0,1,2,3]
Output: [0,-6,0,0,0]

Constraints:
    2 <= nums.length <= 1000
    -20 <= nums[i] <= 20



Recommended Time & Space Complexity
You should aim for a solution as good or better than O(n) time and O(n) space, where n is the size of the input array.

"""
from typing import List


def product_except_self_brute(nums: List[int]) -> List[int]:
    """TC n**2, Space O(1) (output array n does not count) brute force approach"""
    n = len(nums)
    res = [0] * n
    for i in range(n):
        prod = 1
        for j in range(n):
            if i == j:
                continue
            prod *= nums[j]
        res[i] = prod
    return res


def product_except_self_prefix_sufix(nums: List[int]) -> List[int]:
    """
    TC / SC O(n)

    """
    n = len(nums)
    res = [0] * n
    pref = [0] * n
    suff = [0] * n

    pref[0] = suff[n - 1] = 1
    for i in range(1, n):
        pref[i] = nums[i - 1] * pref[i - 1]
    for i in range(n - 2, -1, -1):
        suff[i] = nums[i + 1] * suff[i + 1]
    for i in range(n):
        res[i] = pref[i] * suff[i]
    return res




def product_except_self_prefix_suffix_optimal(nums: List[int]) -> List[int]:
    """
    TC O(n) sc O(1) (not counting the output array)
    """
    res = [1] * len(nums)
    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]
    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]

    return res





def run_prefix_suffix_tests():
    GREEN = "\033[92m"
    RED   = "\033[91m"
    RESET = "\033[0m"

    test_cases = [
        ([1,2,3,4], [24,12,8,6]),
        ([0,1,2,3], [6,0,0,0]),
        ([0,0,1,2], [0,0,0,0]),
        ([5], [1]),
        ([2,3], [3,2]),
        ([1,-1,1,-1], [1,-1,1,-1]),
        ([10,3,5,6,2], [180,600,360,300,900]),
        ([4,0,5], [0,20,0]),
    ]

    print("Testing product_except_self_prefix_sufix:\n")

    for i, (nums, expected) in enumerate(test_cases, 1):
        result = product_except_self_prefix_sufix(nums)
        if result == expected:
            print(f"{GREEN}✅ Test {i}: nums={nums} → {result}{RESET}")
        else:
            print(f"{RED}❌ Test {i}: nums={nums} → {result} (expected {expected}){RESET}")


def run_optimal_tests():
    GREEN = "\033[92m"
    RED   = "\033[91m"
    RESET = "\033[0m"

    test_cases = [
        ([1,2,3,4], [24,12,8,6]),
        ([0,1,2,3], [6,0,0,0]),
        ([0,0,1,2], [0,0,0,0]),
        ([5], [1]),
        ([2,3], [3,2]),
        ([1,-1,1,-1], [1,-1,1,-1]),
        ([10,3,5,6,2], [180,600,360,300,900]),
        ([4,0,5], [0,20,0]),
    ]

    print("Testing product_except_self_prefix_suffix_optimal:\n")

    for i, (nums, expected) in enumerate(test_cases, 1):
        result = product_except_self_prefix_suffix_optimal(nums)
        if result == expected:
            print(f"{GREEN}✅ Test {i}: nums={nums} → {result}{RESET}")
        else:
            print(f"{RED}❌ Test {i}: nums={nums} → {result} (expected {expected}){RESET}")


if __name__ == "__main__":
    run_prefix_suffix_tests()
    run_optimal_tests()