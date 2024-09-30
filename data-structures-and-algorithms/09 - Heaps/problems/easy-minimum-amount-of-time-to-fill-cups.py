"""
https://leetcode.com/problems/minimum-amount-of-time-to-fill-cups

You have a water dispenser that can dispense cold, warm, and hot water. Every second, you can either fill up 2 cups with different types of water, or 1 cup of any type of water.

You are given a 0-indexed integer array amount of length 3 where amount[0], amount[1], and amount[2] denote the number of cold, warm, and hot water cups you need to fill respectively. Return the minimum number of seconds needed to fill up all the cups.



Example 1:

Input: amount = [1,4,2]
Output: 4
Explanation: One way to fill up the cups is:
Second 1: Fill up a cold cup and a warm cup.
Second 2: Fill up a warm cup and a hot cup.
Second 3: Fill up a warm cup and a hot cup.
Second 4: Fill up a warm cup.
It can be proven that 4 is the minimum number of seconds needed.
Example 2:

Input: amount = [5,4,4]
Output: 7
Explanation: One way to fill up the cups is:
Second 1: Fill up a cold cup, and a hot cup.
Second 2: Fill up a cold cup, and a warm cup.
Second 3: Fill up a cold cup, and a warm cup.
Second 4: Fill up a warm cup, and a hot cup.
Second 5: Fill up a cold cup, and a hot cup.
Second 6: Fill up a cold cup, and a warm cup.
Second 7: Fill up a hot cup.
Example 3:

Input: amount = [5,0,0]
Output: 5
Explanation: Every second, we fill up a cold cup.

Constraints:

amount.length == 3
0 <= amount[i] <= 100

"""
import heapq


class Solution(object):
    def fillCups(self, amount):
        """
        My initial solution:
        SC = 1
        TC = O((3 log 3) * n) where n = sum(amount);
        3 log 3 is the sorting part, the size is known and doesn't change this regresses to O(1) complexity;
        So the final TC is = O(n)
        Not very optimized.

        :type amount: List[int]
        :rtype: int
        """

        # The algo we need is to reduce each of the biggest 2 amounts by 1, until we have 2 zero amounts.
        # then we add the last reaming amount to the seconds.
        seconds = 0
        while True:
            amount.sort(reverse=True)
            if amount[0] and amount[1]:
                amount[0] -= 1
                amount[1] -= 1
                seconds += 1
            elif amount[0]:
                seconds += amount[0]
                break
            else:
                break
        return seconds

    def fillCups(self, amount):
        """
        HEAP solution (priority queue), mine.
        SC = O(1), i am doing everything in place
        TC = O(n) where n is sum(amount);
        heapify and pop / push all have complexity of constant time, since we have 3 items;
        interestingly this code has much better runtime in LeetCode
        :type amount: List[int]
        :rtype: int
        """

        # The algo we need is to reduce each of the biggest 2 amounts by 1, until we have 2 zero amounts.
        # then we add the last reaming amount to the seconds.
        seconds = 0
        for i in range(len(amount)):
            amount[i] = -amount[i]  # creating a max heap that is why we switch to negative

        heapq.heapify(amount)  # creating a max heap
        while amount[0]:
            biggest = heapq.heappop(amount)
            second_biggest = heapq.heappop(amount)
            if second_biggest == 0:
                seconds += -biggest  # we had a negative num to create a max heap
                return seconds
            else:
                biggest += 1
                second_biggest += 1
                seconds += 1
                heapq.heappush(amount, biggest)
                heapq.heappush(amount, second_biggest)

        return seconds

    def fillCups(self, amount):
        """
        An attempt for a more optimized solution; I wasn't able to come up with this.
        This is a formula based approach, SC == TC == O(1)
        Code is from GPT as I couldn't come up with the formula. Explanation for future reference:
         Calculates the minimum number of seconds required to fill all cups, given the constraints.

        Constraints:
        - There are three types of cups, and each type needs to be filled a certain number of times,
          as specified in the `amount` list (e.g., [a, b, c]).
        - In each second, you can fill up to two cups, but they must be of different types.
        - You cannot fill more than one cup of the same type in a single second.

        Algorithm Overview:
        - This solution uses a formula-based approach rather than simulating each step.
        - The key is to find the maximum of two values:
            1. The largest single amount in `amount`.
            2. Half of the total sum of all amounts, rounded up.

        Formula:
            Minimum Seconds = max(
                max(amount),
                (sum(amount) + 1) // 2
            )

        Explanation:
        1. **Constraint from the Largest Amount (`max(amount)`):**
           - Since you can't fill more than one cup of the same type per second,
             you need at least as many seconds as the largest single amount.
           - Example: If one type needs to be filled 5 times, you need at least 5 seconds.

        2. **Constraint from Total Cups (`(sum(amount) + 1) // 2`):**
           - You can fill up to two cups per second (of different types).
           - Therefore, the minimum number of seconds cannot be less than half of the total cups, rounded up.
           - Example: If the total cups needed are 7, you need at least ceil(7 / 2) = 4 seconds.

        3. **Taking the Maximum:**
           - The minimum number of seconds required is the maximum of the two constraints above.
           - This ensures both individual and total filling constraints are satisfied.

        Step-by-Step Examples:

        **Example 1:**
        - Input: amount = [1, 4, 2]
        - Calculation:
            - total = 1 + 4 + 2 = 7
            - max_amount = max(1, 4, 2) = 4
            - Half of total (rounded up): (7 + 1) // 2 = 4
            - Minimum Seconds = max(4, 4) = 4
        - Explanation:
            - You need at least 4 seconds to fill the type that requires 4 cups.
            - Even though you can fill two cups per second, the largest amount dictates the minimum time.

        **Example 2:**
        - Input: amount = [2, 2, 2]
        - Calculation:
            - total = 2 + 2 + 2 = 6
            - max_amount = max(2, 2, 2) = 2
            - Half of total (rounded up): (6 + 1) // 2 = 3
            - Minimum Seconds = max(2, 3) = 3
        - Explanation:
            - Half of the total cups requires 3 seconds.
            - Although the largest single amount is 2, you need at least 3 seconds to fill all cups.

        **Example 3:**
        - Input: amount = [5, 4, 4]
        - Calculation:
            - total = 5 + 4 + 4 = 13
            - max_amount = max(5, 4, 4) = 5
            - Half of total (rounded up): (13 + 1) // 2 = 7
            - Minimum Seconds = max(5, 7) = 7
        - Explanation:
            - You need at least 7 seconds because, even though the largest amount is 5,
              the total number of cups requires more time when considering you can fill two cups per second.

        **Why the Formula Works:**
        - **Limiting Factors:**
            - The largest single amount is a limiting factor because you can't fill more than one cup of the same type per second.
            - The total amount determines the overall workload, considering the maximum capacity of filling two cups per second.
        - **Ensuring Both Constraints Are Met:**
            - By taking the maximum, you ensure that you're allocating enough time to handle both the largest individual demand and the collective demands.

        Time Complexity:
        - O(1): All operations (sum, max, integer division) are constant time because the list `amount` always has a fixed size of 3.

        Space Complexity:
        - O(1): Only a constant amount of extra space is used for variables like `total` and `max_amount`.

        :type amount: List[int]
        :rtype: int
        """

        # Calculate the total number of cups needed.
        total = sum(amount)
        # Find the largest single amount among the cup types.
        max_amount = max(amount)
        # Calculate half of the total cups, rounded up.
        half_total = (total + 1) // 2
        # The minimum seconds is the maximum of the largest amount and half of the total cups.
        return max(max_amount, half_total)


sol = Solution()
amount = [5, 4, 4]
expected = 7
print(sol.fillCups(amount))
print(f"{expected=}")
