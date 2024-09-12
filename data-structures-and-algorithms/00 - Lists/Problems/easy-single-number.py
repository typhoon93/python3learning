"""
https://leetcode.com/problems/single-number

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.



Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1


Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.

"""
import collections


class Solution(object):
    def singleNumber(self, nums):
        """
        TC = O(n)
        SC = O(n)

        :type nums: List[int]
        :rtype: int
        """
        counter = collections.defaultdict(int)
        for num in nums:
            counter[num] += 1
        for number, count in counter.items():
            if count == 1:
                return number

    def singleNumber(self, nums):
        """
        Function is from LC, i did not know about XOR before this so I couldn't solve it with O(1) SC.

        TC = O(n), where n is the number of elements in the list.
        SC = O(1), as no extra space is used other than the variable 'result'.

        This function uses the XOR (^) bitwise operator to find the unique number in a list where
        every other number appears exactly twice. The XOR operator works on bits and has several
        key properties that make it suitable for this problem:

        Properties of XOR:
        1. Commutativity: a ^ b = b ^ a
        2. Associativity: a ^ (b ^ c) = (a ^ b) ^ c
        3. Identity: a ^ 0 = a
        4. Self-inverse: a ^ a = 0

        How XOR works in this context:
        - Each number is XORed with a running result initialized to 0.
        - XORing with 0 leaves the number unchanged (Identity property).
        - XORing a number with itself results in 0 (Self-inverse property).
        - Due to the commutative and associative properties, the order of operations doesn't matter,
          and pairs of identical numbers will cancel out, leaving only the unique number.

        Example:
        Consider nums = [2, 3, 2, 4, 4]
        - Start with result = 0
        - After first operation, result = 0 ^ 2 = 2
        - Then result = 2 ^ 3 = 1 (intermediate XOR result)
        - Then result = 1 ^ 2 = 3 (3 is from XORing the previous result with 2)
        - Then result = 3 ^ 4 = 7 (intermediate XOR result)
        - Finally, result = 7 ^ 4 = 3 (3 is the number that appears once as all pairs cancel out)
        - NB this is as if we just did 2 ^ 3 ^ 2 ^ 4 ^ 4 = 3;
        - XOR has a lot of applications,
            -masking stuff (having a salt and then using the same salt to unmask it for example:
            -simple encryption
            -Memory-efficient Data Structures (doubly linked list that stores data only as a linked list - this is from GPT so if you are interested dive in it when have time).

        The only number that does not find a pair and hence is not canceled out is the unique number.
        TC = O(n), where n is the number of elements in the list.
        SC = O(1), as no extra space is used other than the variable 'result'.

        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for num in nums:
            result ^= num  # Apply XOR between result and each number - this is really one big associative XOR
        return result
if __name__ == "__main__":
    sol = Solution()
    nums = [1,0,1]
    expected = 0
    res = sol.singleNumber(nums)
    print(res)
    print("Expected: ", expected)
