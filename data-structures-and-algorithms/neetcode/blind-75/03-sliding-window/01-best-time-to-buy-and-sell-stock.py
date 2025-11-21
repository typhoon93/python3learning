"""
https://neetcode.io/solutions/best-time-to-buy-and-sell-stock
https://youtu.be/1pkOgXD63yU
Best Time to Buy And Sell Stock - Explanation

You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

Example 1:

Input: prices = [10,1,5,6,7,1]

Output: 6

Explanation: Buy prices[1] and sell prices[4], profit = 7 - 1 = 6.

Example 2:

Input: prices = [10,8,7,5,2]

Output: 0

Explanation: No profitable transactions can be made, thus the max profit is 0.

Constraints:

    1 <= prices.length <= 100
    0 <= prices[i] <= 100


Recommended Time & Space Complexity

You should aim for a solution with O(n) time and O(1) space, where n is the size of the input array.

"""
from typing import List


def max_profit_brute(prices: List[int]) -> int:
    """
    SC = O(1)
    TC = n^2
    """
    res = 0
    for i in range(len(prices)):
        buy = prices[i]
        for j in range(i + 1, len(prices)):
            sell = prices[j]
            res = max(res, sell - buy)
    return res


def max_profit_dynamic_p(prices: List[int]) -> int:
    max_p = 0
    min_buy = prices[0]
    for sell in prices:
        max_p = max(max_p, sell - min_buy)
        min_buy = min(min_buy, sell)
    return max_p


def max_profit_pointers(prices: List[int]) -> int:
    """
    SC = O(1)
    TC = O(n)
    """
    l, r = 0, 1  # left = buy, right = sell
    max_profit = 0
    while r < len(prices):
        # profitable ?
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            max_profit = max(max_profit, profit)
        else:
            l = r
        r += 1
    return max_profit




def run_max_profit_pointers_tests():
    GREEN = "\033[92m"
    RED   = "\033[91m"
    RESET = "\033[0m"

    test_cases = [
        ([10,1,5,6,7,1], 6),        # example
        ([10,8,7,5,2], 0),          # descending
        ([1,2,3,4,5], 4),           # all increasing
        ([5,4,3,2,1], 0),           # all decreasing
        ([7,1,5,3,6,4], 5),         # classic LC example
        ([2,4,1], 2),               # simple
        ([3,3,3,3], 0),             # constant prices
        ([1], 0),                   # single element
        ([1,5], 4),                 # minimal profitable pair
        ([7,6,4,3,1,10], 9),        # big jump at end
    ]

    print("Testing max_profit_pointers:\n")

    for i, (prices, expected) in enumerate(test_cases, 1):
        result = max_profit_pointers(prices)
        if result == expected:
            print(f"{GREEN}✅ Test {i}: prices={prices} → {result}{RESET}")
        else:
            print(f"{RED}❌ Test {i}: prices={prices} → {result} (expected {expected}){RESET}")


if __name__ == "__main__":
    run_max_profit_pointers_tests()