"""
#(Task 1) Find the second largest number in a list of integers?

Implement a version that handles duplicates and negative values efficiently using sorting and set operations for O(n log n) complexity.
"""
from typing import List

"""
Answer: I have written a solution that is more optimized than the required complexity. Space is O(1), time is O(n).
This is as optimized as this exercise can get.

More Optimized Solution is here: get_second_largest
Required Solution is here: get_second_largest_alternate

Both were written by me; I have only double checked the code with an LLM to ensure my complexity calculations are correct.
"""


def get_second_largest(nums: List):
    """
    Space Complexity = O(1)
    Time Complexity = O(n)
    this is more efficient than the required version, we do not have to worry about duplicates or negative values in the list.
    """

    if len(nums) < 2:
        return None
    first = float("-inf")  # setting lower bound of -inf so we can easily start comparing.
    second = float("-inf")

    for num in nums:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num

    if second == float("-inf"):
        return None
    return second


def get_second_largest_alternate(nums):
    """
    This is a SET based approach to the solution, I am purposefully trying to get TC of O(n log n) as required.
    Space complexity becomes O(n)
    Time complexity is O(n log n); due to sorted having this complexity.
    """
    if len(nums) < 2:
        return None
    set_nums = set(nums)
    sorted_nums = sorted(set_nums, reverse=True)
    if len(sorted_nums) < 2:
        return None
    return sorted_nums[1]


if __name__ == "__main__":
    nums = [-1, -1, 5, 5]
    expected = -1
    print(get_second_largest_alternate(nums))
    print(f"{expected=}")
