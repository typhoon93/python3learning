"""
https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/

You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians). The soldiers are positioned in front of the civilians. That is, all the 1's will appear to the left of all the 0's in each row.

A row i is weaker than a row j if one of the following is true:

The number of soldiers in row i is less than the number of soldiers in row j.
Both rows have the same number of soldiers and i < j.
Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.



Example 1:

Input: mat =
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]],
k = 3
Output: [2,0,3]
Explanation:
The number of soldiers in each row is:
- Row 0: 2
- Row 1: 4
- Row 2: 1
- Row 3: 2
- Row 4: 5
The rows ordered from weakest to strongest are [2,0,3,1,4].
Example 2:

Input: mat =
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]],
k = 2
Output: [0,2]
Explanation:
The number of soldiers in each row is:
- Row 0: 1
- Row 1: 4
- Row 2: 1
- Row 3: 1
The rows ordered from weakest to strongest are [0,2,3,1].


"""
import heapq


class Solution(object):

    def kWeakestRows(self, mat, k):
        """
        My solution 1:
        SC = O(n + k)
        TC = O( m x n + n log n)
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        min_heap = []
        for i in range(len(mat)):
            strength = sum(mat[i])
            heapq.heappush(min_heap, (strength, i))

        result = []

        for i in range(k):
            result.append(heapq.heappop(min_heap)[1])

        return result

    def kWeakestRows(self, mat, k):
        """
        Solution 2 with better SC
        tc = (mn + n log k)
        sc = k
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        min_heap = []
        for i in range(len(mat)):
            strength = sum(mat[i])
            heapq.heappush(min_heap, (-strength, -i))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        result = []

        for i in range(k):
            result.append(-heapq.heappop(min_heap)[1])
        result.reverse()

        return result

    def kWeakestRows(self, mat, k):
        """
        Solution 2 with better SC
        tc = (n log m + n log k) m is the len of the arrays
        sc = k
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """

        def count_soldiers(row):
            """Binary search algo to count the soldiers. Using the fact that soldiers are 1 and will always be in front of civs"""
            low, high = 0, len(row) - 1
            while low <= high:
                mid = (low + high) // 2
                if row[mid] == 1:
                    low = mid + 1
                else:
                    high = mid - 1
            return low

        min_heap = []
        for i in range(len(mat)):
            strength = count_soldiers(mat[i])
            heapq.heappush(min_heap, (-strength, -i))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        result = []

        for i in range(k):
            result.append(-heapq.heappop(min_heap)[1])
        result.reverse()

        return result


mat = [[1, 1, 0, 0, 0],
       [1, 1, 1, 1, 0],
       [1, 0, 0, 0, 0],
       [1, 1, 0, 0, 0],
       [1, 1, 1, 1, 1]];
k = 3
expected = [2, 0, 3]
sol = Solution()
res = sol.kWeakestRows(mat, k)
print(res)
print(f"{expected=}")
