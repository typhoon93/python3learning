"""
https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity/

You are given a positive integer num. You may swap any two digits of num that have the same parity (i.e. both odd digits or both even digits).

Return the largest possible value of num after any number of swaps.



Example 1:

Input: num = 1234
Output: 3412
Explanation: Swap the digit 3 with the digit 1, this results in the number 3214.
Swap the digit 2 with the digit 4, this results in the number 3412.
Note that there may be other sequences of swaps but it can be shown that 3412 is the largest possible number.
Also note that we may not swap the digit 4 with the digit 1 since they are of different parities.
Example 2:

Input: num = 65875
Output: 87655
Explanation: Swap the digit 8 with the digit 6, this results in the number 85675.
Swap the first digit 5 with the digit 7, this results in the number 87655.
Note that there may be other sequences of swaps but it can be shown that 87655 is the largest possible number.


Constraints:

1 <= num <= 10**9

"""
import heapq


class Solution(object):
    def largestInteger(self, num):
        """
        My solution, using selection sort
        SC = O(n) -> number of digits in nums
        TC = O(n**2) -> n = number of digits in num
        :type num: int
        :rtype: int
        """
        num_lst = [int(d) for d in str(num)]
        for i in range(len(num_lst)):
            parity = num_lst[i] % 2
            max_index = i
            for j in range(i + 1, len(num_lst)):
                if num_lst[j] % 2 == parity and num_lst[j] > num_lst[max_index]:
                    max_index = j
            num_lst[i], num_lst[max_index] = num_lst[max_index], num_lst[i]
        return int("".join(str(d) for d in num_lst))


    def largestInteger(self, num):
        """
        Using sorting, GPT solution
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        :type num: int
        :rtype: int
        """
        num_lst = [int(d) for d in str(num)]
        even_digits = sorted([d for d in num_lst if d % 2 == 0], reverse=True)
        odd_digits = sorted([d for d in num_lst if d % 2 == 1], reverse=True)

        result = []
        even_idx = odd_idx = 0
        for d in num_lst:
            if d % 2 == 0:
                result.append(even_digits[even_idx])
                even_idx += 1
            else:
                result.append(odd_digits[odd_idx])
                odd_idx += 1

        return int(''.join(map(str, result)))

    def largestInteger(self, num):
        """
        Using HEAPs(max); we put numbers into odd / even max heaps, and then pop them at the appropriate time to construct
        the largest Integer
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        :type num: int
        :rtype: int
        """
        num_lst = [int(d) for d in str(num)]
        even_heap = []
        odd_heap = []
        for d in num_lst:
            if d%2 == 0:
                heapq.heappush(even_heap, -d) # using minus to simulate max heap
            else:
                heapq.heappush(odd_heap, -d)

        result = []
        for d in num_lst:
            if d % 2 == 0:
                max_even = -heapq.heappop(even_heap)
                result.append(str(max_even))
            else:
                max_odd = -heapq.heappop(odd_heap)
                result.append(str(max_odd))
        return int("".join(result))

num = 1234
expected = 3412
sol = Solution()
print(sol.largestInteger(num))
print(f'{expected=}')
