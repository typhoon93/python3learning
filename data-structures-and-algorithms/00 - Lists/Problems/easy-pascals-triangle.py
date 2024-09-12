"""
https://leetcode.com/problems/pascals-triangle/

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:




Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]


Constraints:

1 <= numRows <= 30


"""


class Solution(object):
    def generate(self, numRows):
        """
        my solution
        SC = n*2
        TC = n*2
        :type numRows: int
        :rtype: List[List[int]]
        """
        start = 1
        pascal_triangle = []
        for i in range(numRows):
            line = (i + 1) * [start]
            if i != 0:
                for j in range(len(line)):
                    if j == 0 or j == len(line) - 1:
                        continue
                    line[j] = pascal_triangle[i - 1][j - 1] + pascal_triangle[i - 1][j]
            pascal_triangle.append(line)

        return pascal_triangle

    def generate(self, numRows):
        """
        Improved GPT solution - slightly more python code.
        """
        pascal_triangle = []
        for i in range(numRows):
            row = [1] * (i + 1)
            for j in range(1, i):  # this loop makes sure that we do not touch j == 0 and j == len - 1 (last index),
                # so it remains zero. Basically uses pythons range and how it works to avoid some lines of code.
                row[j] = pascal_triangle[i - 1][j - 1] + pascal_triangle[i - 1][j]
            pascal_triangle.append(row)
        return pascal_triangle


if __name__ == "__main__":
    sol = Solution()
    numRows = 5
    res = sol.generate(numRows)
    for line in res:
        print(line)
