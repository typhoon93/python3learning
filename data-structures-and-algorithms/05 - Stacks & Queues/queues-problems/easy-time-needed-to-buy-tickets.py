"""
https://leetcode.com/problems/time-needed-to-buy-tickets

There are n people in a line queuing to buy tickets, where the 0th person is at the front of the line and the (n - 1)th person is at the back of the line.

You are given a 0-indexed integer array tickets of length n where the number of tickets that the ith person would like to buy is tickets[i].

Each person takes exactly 1 second to buy a ticket. A person can only buy 1 ticket at a time and has to go back to the end of the line (which happens instantaneously) in order to buy more tickets. If a person does not have any tickets left to buy, the person will leave the line.

Return the time taken for the person at position k (0-indexed) to finish buying tickets.



Example 1:

Input: tickets = [2,3,2], k = 2
Output: 6
Explanation:
- In the first pass, everyone in the line buys a ticket and the line becomes [1, 2, 1].
- In the second pass, everyone in the line buys a ticket and the line becomes [0, 1, 0].
The person at position 2 has successfully bought 2 tickets and it took 3 + 3 = 6 seconds.
Example 2:

Input: tickets = [5,1,1,1], k = 0
Output: 8
Explanation:
- In the first pass, everyone in the line buys a ticket and the line becomes [4, 0, 0, 0].
- In the next 4 passes, only the person in position 0 is buying tickets.
The person at position 0 has successfully bought 5 tickets and it took 4 + 1 + 1 + 1 + 1 = 8 seconds.


Constraints:

n == tickets.length
1 <= n <= 100
1 <= tickets[i] <= 100
0 <= k < n

"""
import collections


class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        My solution, simulation based;
        SC = O(n) -> creating the queue.
        TC = O(n×m) (depends on the tickets that people need to buy, but it will be linear in relation to the nums in the tickets queue)
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        seconds = 0
        k_pos = k
        tickets = collections.deque(tickets)
        while True:
            current = tickets.popleft()
            if current != 0:
                current = current - 1
                seconds += 1
            tickets.append(current)
            k_pos -= 1
            if k_pos < 0:
                k_pos = len(tickets) - 1
                if tickets[k_pos] == 0:
                    break
        return seconds


class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        Attempt at new solution that has
        SC = O(1)
        TC = O(n)
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        # tickets = [2, 3, 2], k = 2
        # =>we need to go through the loop 2 times.
        # => we have 3 items before us, so 3 * 2 = 6;
        # edge cases:
        # k is not the end of the list.
        # we go one time len - k
        # then we go n(len)
        # some person becomes 0 while in the loop (aka person < tickets[k])
        # in that case we only calculate it however many times it takes for it to go to 0
        # after it is 0, we reduce the len of the array by it

        # case1: ideal case, tickets[k] >= all in k, and k == len(tickets)-1
        # return (k + 1) * tickets[k]
        # case 2: tickets[k] >= all in k, and k < len(ticket)-1 (below code handles ideal case too)
        # return len(tickets) * (tickets[k]-1) + (k+1)
        # case 3: tickets[k] >= all in k, and k < len(ticket)-1, and tickets[i] may be smaller than tickets[k]
        # this handles all the above cases too:
        total = 0
        for i in range(len(tickets)):
            if i <= k:
                total += tickets[i] if tickets[i] < tickets[k] else tickets[k]
            else:  # these will be looped 1 less time than ticket[k], because they come after it
                total += tickets[i] if tickets[i] < tickets[k] else tickets[k] - 1

        return total


sol = Solution()
tickets = [84, 49, 5, 24, 70, 77, 87, 8];
k = 3;
expected = 154
# tickets =[2,3,2]; k = 2 ; expected = 6
res = sol.timeRequiredToBuy(tickets, k)
print(res)
print(f"{expected}")
