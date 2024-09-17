"""
https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/


You are given an integer array prices where prices[i] is the price of the ith item in a shop.

There is a special discount for items in the shop. If you buy the ith item, then you will receive a discount equivalent to prices[j] where j is the minimum index such that j > i and prices[j] <= prices[i]. Otherwise, you will not receive any discount at all.

Return an integer array answer where answer[i] is the final price you will pay for the ith item of the shop, considering the special discount.



Example 1:

Input: prices = [8,4,6,2,3]
Output: [4,2,4,2,3]
Explanation:
For item 0 with price[0]=8 you will receive a discount equivalent to prices[1]=4, therefore, the final price you will pay is 8 - 4 = 4.
For item 1 with price[1]=4 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 4 - 2 = 2.
For item 2 with price[2]=6 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 6 - 2 = 4.
For items 3 and 4 you will not receive any discount at all.
Example 2:

Input: prices = [1,2,3,4,5]
Output: [1,2,3,4,5]
Explanation: In this case, for all items, you will not receive any discount at all.
Example 3:

Input: prices = [10,1,1,6]
Output: [9,0,1,6]


Constraints:

1 <= prices.length <= 500
1 <= prices[i] <= 1000

"""
import collections


class Solution(object):
    def finalPrices(self, prices):
        """
        My solution - using multiple data structures, stacks and queues;
        This is similar to aprevious problem i solved nextGreaterElement, but has some differences that make the use of
        a queue imporatnt to keep complexity down.
        TC = O(n)
        SC = O(n)

        :type prices: List[int]
        :rtype: List[int]
        """
        # discount calculation for i th item:
        # discounted i = prices[i] - prices[j]
        # where i < j (indexes
        # where prices[i] >= prices[j]
        # if no suck item j -> then no discount

        discounted_prices = collections.defaultdict(collections.deque)
        stack = []

        for num in prices:
            while stack and stack[-1] >= num:
                discounted_prices[stack[-1]].append(stack[-1] - num)
                stack.pop()
            stack.append(num)

        while stack:
            discounted_prices[stack[-1]].append(stack[-1])
            stack.pop()

        result = []
        for price in prices:
            result.append(discounted_prices[price].popleft())

        return result

    def finalPrices(self, prices):
        """
        An improves SC solution.
        SC here is O(1), we avoid using deque and the solution is overall simpler, as we do an in place modification of prices.
        Takeaway for me: always look at the DS that I am using, if it is mutable, i may be able to save space complexity greatly,
        if the problem doesn't require me to keep the input immutable.
        """
        stack = []
        for i in range(len(prices)):
            # While the current price is less than or equal to the price at the index stored in the stack
            while stack and prices[stack[-1]] >= prices[i]:
                idx = stack.pop()
                prices[idx] = prices[idx] - prices[i]
            stack.append(i)
        return prices

sol = Solution()
prices = [10, 1, 1, 6]

print(sol.finalPrices(prices))
expected = [9, 0, 1, 6]
print(f"{expected=}")
