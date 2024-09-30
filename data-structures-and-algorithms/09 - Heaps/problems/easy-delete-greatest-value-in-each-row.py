"""
https://leetcode.com/problems/delete-greatest-value-in-each-row


You are given an m x n matrix grid consisting of positive integers.

Perform the following operation until grid becomes empty:

Delete the element with the greatest value from each row. If multiple such elements exist, delete any of them.
Add the maximum of deleted elements to the answer.
Note that the number of columns decreases by one after each operation.

Return the answer after performing the operations described above.



Example 1:


Input: grid = [[1,2,4],[3,3,1]]
Output: 8
Explanation: The diagram above shows the removed values in each step.
- In the first operation, we remove 4 from the first row and 3 from the second row (notice that, there are two cells with value 3 and we can remove any of them). We add 4 to the answer.
- In the second operation, we remove 2 from the first row and 3 from the second row. We add 3 to the answer.
- In the third operation, we remove 1 from the first row and 1 from the second row. We add 1 to the answer.
The final answer = 4 + 3 + 1 = 8.
Example 2:


Input: grid = [[10]]
Output: 10
Explanation: The diagram above shows the removed values in each step.
- In the first operation, we remove 10 from the first row. We add 10 to the answer.
The final answer = 10.


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
1 <= grid[i][j] <= 100

"""
import heapq


class Solution(object):
    def deleteGreatestValue(self, grid):
        """
        m == grid.length
        n == grid[i].length
        My Solution
        SC = O(m)
        TC = O(m * n log n)
        :type grid: List[List[int]]
        :rtype: int
        """
        total = 0
        for row in grid:  # TC = m * n # heapifying rows. it doesn't matter if we do min or max heap here,
            # since the items we pop from each row be matched with the same items from other rows regardless of the heap type
            heapq.heapify(row)

        while grid[0]: # O(m)
            popped_nums = []  # SC = O(m);
            for row in grid:  # TC O(n * log n)
                popped_nums.append(heapq.heappop(row))
            total += max(popped_nums)
        return total

    def deleteGreatestValue(self, grid):
        """
        GPT Solution Very clean and understandable code, uses generator
        SC = O(1)
        TC = O( m * n log n)

        """
        for row in grid:
            row.sort(reverse=True)

        answer = 0
        n = len(grid[0]) # number of cols for each row

        for i in range(n):
            max_in_column = max(row[i] for row in grid)
            answer += max_in_column

        return answer


nums = [[1, 2, 4], [3, 3, 1]]

expected = 8
sol = Solution()
print(sol.deleteGreatestValue(nums))
print(f'{expected=}')
