"""
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:




Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]


Constraints:

0 <= rowIndex <= 33


Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?


"""


class Solution(object):
    def getRow(self, rowIndex):
        """
        My solution, simple after doing the initial Pascal Triangle Exercise.
        SC = O(rowIndex)
        TC = O(n**2)
        :type rowIndex: int
        :rtype: List[int]
        """
        prev_row = []
        # Iterate over each row up to the given rowIndex.
        for i in range(rowIndex+1):
            # Start the current row with 1's since the first and last elements are always 1.
            row = (i + 1) * [1]
            for j in range(1, i):
                # Each element is the sum of the two elements diagonally above it from the previous row.
                row[j] = prev_row[j-1] + prev_row[j]
            prev_row = row
        # After all iterations, prev_row will be the rowIndex-th row of Pascal's Triangle.
        return prev_row



    def generate(self, numRows):
        """
        my solution
        SC = n*2
        TC = n*2
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        for i in range(numRows):
            row = (i+1) * [1]
            for j in range(1,i):
                row[j] = result[i][j-1] + result[i][j+1]
            result.append(row)
        return result



if __name__ == "__main__":
    sol = Solution()
    numRows = 4
    res = sol.getRow(numRows)
    print(res)
    for line in res:
        print(line)
