"""
https://leetcode.com/problems/kth-largest-element-in-a-stream

You are part of a university admissions office and need to keep track of the kth highest test score from applicants in real-time. This helps to determine cut-off marks for interviews and admissions dynamically as new applicants submit their scores.

You are tasked to implement a class which, for a given integer k, maintains a stream of test scores and continuously returns the kth highest test score after a new score has been submitted. More specifically, we are looking for the kth highest score in the sorted list of all scores.

Implement the KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of test scores nums.
int add(int val) Adds a new test score val to the stream and returns the element representing the kth largest element in the pool of test scores so far.


Example 1:

Input:
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]

Output: [null, 4, 5, 5, 8, 8]

Explanation:

KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3); // return 4
kthLargest.add(5); // return 5
kthLargest.add(10); // return 5
kthLargest.add(9); // return 8
kthLargest.add(4); // return 8

Example 2:

Input:
["KthLargest", "add", "add", "add", "add"]
[[4, [7, 7, 7, 7, 8, 3]], [2], [10], [9], [9]]

Output: [null, 7, 7, 7, 8]

Explanation:

KthLargest kthLargest = new KthLargest(4, [7, 7, 7, 7, 8, 3]);
kthLargest.add(2); // return 7
kthLargest.add(10); // return 7
kthLargest.add(9); // return 7
kthLargest.add(9); // return 8


Constraints:

0 <= nums.length <= 104
1 <= k <= nums.length + 1
-104 <= nums[i] <= 104
-104 <= val <= 104
At most 104 calls will be made to add.


"""
from typing import List
import heapq


class KthLargest:
    """My initial solution, not very efficient"""

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = [-num for num in nums]  # switching signs so heapq behaves as a max_heap
        heapq.heapify(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, -val)
        extracted = []
        for i in range(self.k - 1):
            extracted.append(heapq.heappop(self.nums))
        k_th = -self.nums[0]
        while extracted:
            heapq.heappush(self.nums, extracted.pop())
        return k_th


class KthLargest:
    """
    https://leetcode.com/problems/kth-largest-element-in-a-stream
    GPT Solution 0 very efficient, miles ahead of my own solution;
    Implement the KthLargest class:
        KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of test scores nums.
        int add(int val) Adds a new test score val to the stream and returns the element representing the kth
        largest element in the pool of test scores so far.
    This not the most efficient way but it is a good clear demo of using heaps
    TC: O(log k) - add
    SC: O(k)
    """

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        for num in nums:
            heapq.heappush(self.heap, num)
            if len(self.heap) > k:
                # If the heap is larger than k, remove the smallest element (root) until it has exactly k elements
                heapq.heappop(self.heap)
        # since this is a min heap, this will leave only K elements,
        # and they are going to be the K largest of all elements added. Why? These are the only ones the problem is interested in.
        # as such, the 0th element of the array (the smallest) is always the one we are looking for

    def add(self, val: int) -> int:
        """
        Adds a value to the heap and maintains its size at k, returning the k-th largest element.
        """
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
            # since this is a min heap, this will leave only K elements,
            # and they are going to be the K largest of all elements added. Why? These are the only ones the problem is interested in.
            # as such, the 0th element of the array (the smallest) is always the one we are looking for
        return self.heap[0]


class KthLargest:
    """
    This is the most efficient way for doing the algo.
    Time complexity for add operation: O(log k)
    Space complexity: O(k)
    """

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = []
        for num in nums:
            self.add(num)  # Use the add method to maintain the heap with only k elements

    def add(self, val: int) -> int:
        """
        Adds a value to the heap, keeping the heap size at most k, and returns the k-th largest element.
        """
        # Add the new value to the heap
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
        elif val > self.min_heap[0]:
            # Only push the new value if it's larger than the smallest in the heap
            heapq.heappushpop(self.min_heap, val)

        # The root of the heap is the k-th largest element
        return self.min_heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


if __name__ == "__main__":
    k = 4
    nums = [7, 7, 7, 7, 8, 3]
    new_nums = [2, 10, 9, 9]
    obj = KthLargest(k, nums)
    for num in new_nums:
        print(obj.add(num))
