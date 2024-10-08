"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.



Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.


Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        O(n) - tc
        O(1) - sc
        :type prices: List[int]
        :rtype: int
        """
        lowest_buy = prices[0]
        max_profit = 0
        for price in prices:
            if lowest_buy is None:
                lowest_buy = price
            if lowest_buy > price:
                lowest_buy = price
            current_profit = price - lowest_buy
            if current_profit > max_profit:
                max_profit = current_profit
        return max_profit

    def maxProfit(self, prices):
        """
        Streamlined version, GPT - just a bit better one, has good assumptions / tc and sc is the same
        O(n) - time complexity
        O(1) - space complexity
        :type prices: List[int]
        :rtype: int
        """
        if not prices:  # Handle an empty list case
            return 0

        max_profit = 0
        lowest_buy = prices[0]

        for price in prices:
            if price < lowest_buy:
                lowest_buy = price
            elif price - lowest_buy > max_profit:
                max_profit = price - lowest_buy

        return max_profit

if __name__ == "__main__":
    sol = Solution()
    prices = [2,1,2,1,0,1,2]
    expected = 2
    res = sol.maxProfit(prices)
    print(res)
    print("Expected: ", expected)