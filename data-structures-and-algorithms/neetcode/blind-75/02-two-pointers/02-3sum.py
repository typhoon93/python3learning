"""
https://neetcode.io/solutions/3sum
https://youtu.be/jzZsG8n2R9A

3 SUM

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]

Output: [[-1,-1,2],[-1,0,1]]

Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].

Example 2:

Input: nums = [0,1,1]

Output: []

Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0]

Output: [[0,0,0]]

Explanation: The only possible triplet sums up to 0.

Constraints:

    3 <= nums.length <= 1000
    -10^5 <= nums[i] <= 10^5



Recommended Time & Space Complexity

You should aim for a solution with O(n^2) time and O(1) space, where n is the size of the input array.

"""
from collections import defaultdict
from typing import List


def three_sum_brute(nums: List[int]) -> List[List[int]]:
    """
    TC = n^3
    sc = O(n)
    """
    res = set()  # ensures uniquenes
    nums.sort()
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    tmp = (nums[i], nums[j], nums[k])
                    res.add(tmp)
    return [list(i) for i in res]


def three_sum_hash_map(nums: List[int]) -> List[List[int]]:
    """
    TC O (n^2)
    SC O(n)
    """
    nums.sort()
    count = defaultdict(int)
    for num in nums:
        count[num] += 1
    res = []
    for i in range(len(nums)):
        count[nums[i]] -= 1
        if i and nums[i] == nums[i - 1]:
            # prev number equal to current one
            continue
        for j in range(i + 1, len(nums)):
            count[nums[j]] -= 1
            if j - 1 > i and nums[j] == nums[j - 1]:
                # skipping same numbers
                continue
            target = -(nums[i] + nums[j])
            if count[target] > 0:
                res.append([nums[i], nums[j], target])

        for j in range(i + 1, len(nums)):  # reset counts
            count[nums[j]] += 1
    return res


def three_sum_two_pointers(nums: List[int]) -> List[List[int]]:
    """
    TC = O(n^2)
    SC = O(1)
    Sort → O(n log n)
    Fix one number (anchor) and move two pointers → O(n²)
    """
    res = []
    nums.sort()

    for i, anchor in enumerate(nums):
        if anchor > 0:  # if the smallest number is > 0 we can never get a sum == 0, so early return
            break
        if i > 0 and anchor == nums[i - 1]:
            # skip to next num if curr and prev are the same (means already checked in this position)
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            three_sum = anchor + nums[left] + nums[right]
            if three_sum > 0:  # we need to decrease the sum!
                right -= 1
            elif three_sum < 0:  # we need to increase the sum
                left += 1
            else:
                res.append([anchor, nums[left], nums[right]])
                left += 1
                right -= 1
                while nums[left] == nums[left - 1] and left < right:
                    left += 1

    return res



def run_three_sum_two_pointers_tests():
    GREEN = "\033[92m"
    RED   = "\033[91m"
    RESET = "\033[0m"

    test_cases = [
        ([-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]),
        ([0,1,1], []),
        ([0,0,0], [[0,0,0]]),
        ([], []),
        ([1,2,-2,-1], []),
        ([-2,0,1,1,2], [[-2,0,2],[-2,1,1]]),
        ([-4,-2,-2,-2,0,1,2,2,2,3,4], [[-4,0,4],[-4,1,3],[-4,2,2],[-2,-2,4],[-2,0,2]]),
    ]

    # normalize for comparison (sort lists + internal triplets)
    def normalize(result):
        return sorted([sorted(t) for t in result])

    print("Testing three_sum_two_pointers:\n")

    for i, (nums, expected) in enumerate(test_cases, 1):
        result = three_sum_two_pointers(nums)
        if normalize(result) == normalize(expected):
            print(f"{GREEN}✅ Test {i}: nums={nums} → PASS{RESET}")
        else:
            print(f"{RED}❌ Test {i}: nums={nums}\n"
                  f"   result   = {result}\n"
                  f"   expected = {expected}{RESET}")


if __name__ == "__main__":
    run_three_sum_two_pointers_tests()