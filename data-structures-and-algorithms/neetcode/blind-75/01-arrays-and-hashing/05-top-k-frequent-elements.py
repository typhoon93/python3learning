"""
https://neetcode.io/solutions/top-k-frequent-elements
https://www.youtube.com/watch?v=YPTqKIgVk-k

Description

Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

Example 1:

Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]

Example 2:

Input: nums = [7,7], k = 1

Output: [7]

Constraints:

    1 <= nums.length <= 10^4.
    -1000 <= nums[i] <= 1000
    1 <= k <= number of distinct elements in nums.

 You should aim for a solution with O(n) time and O(n) space, where n is the size of the input array.

"""

# heapify is o(n)
import heapq


def top_k_frequencies_sorting(nums: list, k: int) -> list:
    """
    TC n log n
    SC O(n)
    """
    count = {}
    for num in nums:
        count[num] = 1 + count.get(num, 0)
    arr = []
    for num, cnt in count.items():
        arr.append([cnt, num])
    arr.sort()

    res = []
    while len(res) < k:
        res.append(arr.pop()[1])
    return res


def top_k_frequencies_min_heap(nums: list, k: int) -> list:
    """
    TC n log k
    SC O(n + k)

    Where n is the length of the array and k is the number of top frequent elements.
    """
    count = {}
    for num in nums:
        count[num] = 1 + count.get(num, 0)
    heap = []
    for num in count.keys():
        heapq.heappush(heap, (count[num], num))
        if len(heap) > k:
            heapq.heappop(heap)

    res = []
    while len(res) < k:
        res.append(heap.pop()[1])
    return res


def top_k_frequencies(nums: list, k: int) -> list:
    """
    We use buckets; the buckets array is "freq" -> bounded by the len of nums
    Intution: the biggest frequency can be len(nums) -> case where one number is repeated throughout the whole array

    """
    count = {}
    freq = [[] for _ in range(len(nums) + 1)]
    # get counts of items
    for n in nums:
        count[n] = 1 + count.get(n, 0)

    # set counts to numbers; index is the count of the number
    for n, c in count.items():
        freq[c].append(n)

    res = []
    # go backwards, as we are looking for the most frequent k
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res
    return res


def run_top_k_frequencies_tests():
    GREEN = "\033[92m"
    RED = "\033[91m"
    RESET = "\033[0m"

    test_cases = [
        ([1,1,1,2,2,3], 2, [[1,2]]),
        ([1], 1, [[1]]),
        ([4,4,4,4], 1, [[4]]),
        ([1,2,3,4], 2, [[1,2,3,4]]),
        ([5,5,6,6,6,7], 2, [[6,5]]),
        ([10,10,20,20,20,30], 1, [[20]]),
        ([1,2,2,3,3,3], 3, [[3,2,1]]),
        ([], 0, [[]]),

        # FIXED: now expects ANY of [9], [8], [7] when k=1
        ([9,9,8,8,7,7], 1, [[9], [8], [7]]),
    ]

    print("Testing top_k_frequencies:\n")

    def normalize(x):
        return sorted(x)

    for i, (nums, k, expected_groups) in enumerate(test_cases, 1):
        result = top_k_frequencies(nums, k)

        ok = any(normalize(result) == normalize(exp)[:k] for exp in expected_groups)

        if ok:
            print(f"{GREEN}✅ Test {i}: nums={nums}, k={k} → {result}{RESET}")
        else:
            print(f"{RED}❌ Test {i}: nums={nums}, k={k} → {result} (expected one of {expected_groups}){RESET}")


if __name__ == "__main__":
    run_top_k_frequencies_tests()