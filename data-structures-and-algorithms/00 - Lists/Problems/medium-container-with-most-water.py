"""
https://leetcode.com/problems/container-with-most-water

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.



Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1


Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104


"""


class Solution(object):
    def maxArea(self, height):
        """
        my solution, brute force
        sc = O(1)
        tc = O(n**2)
        :type height: List[int]
        :rtype: int
        """
        max_area = float("-inf")
        for i in range(len(height)):
            for j in range(i):
                horizontal = i - j
                vertical = min(height[i], height[j])
                area = horizontal * vertical
                if area > max_area:
                    max_area = area
        return max_area

    def maxArea(self, height):
        """
        my solution, improving on initial brute force approach;
        Two pointer solution; note that i saw the hint for a two pointer solution before writing my answer
        TC = O(n)
        SC = O(1)
        I came up with this solution myself, but here's a chatgpt details I got afterwards for details on why this works:

        The solution you've provided employs a two-pointer technique to efficiently find the maximum area without
        exhaustively checking all possible pairs of lines.
        The key lies in understanding how certain combinations can be safely skipped based on logical reasoning
        about the problem's constraints.

        The goal is to find two lines that, along with the x-axis, form a container that holds the maximum amount of water.
        The area between two lines is determined by the shorter line and the distance (width) between them.
        The brute force solution checks all solutions.
        The two pointer solution (that we have below) makes some assumptions.
            The critical decision in this algorithm is which pointer to move at each step:
                1. Calculate the Current Area:
                2. Update Maximum Area
                3. Move the pointer of the shorter line:
                    The reasoning is based on the observation that the area is limited by the shorter line:
                        - area = width * height
                        - limiting factor is the min(height[i], height[j])
                        - By moving the pointer of the shorter line inward, you may find a taller line,
                         potentially increasing the
                        - The width decreases by 1 in any case,
                         but the potential increase in height could compensate for this loss,
                         - if we were to move the taller line, the height can only decrease, which is not what we want.
                        The width decreases, and the height remains the same or decreases,
                        leading to an area that has a chance to be bigger than the current one.

            Why All Combinations Aren't Needed
                Not all combinations are needed with this approach, and we skip certain combinations based
                 on logical deducctions:
                    - Eliminating Suboptimal Pairs: By always moving the pointer pointing to the shorter line,
                    the algorithm avoids pairs that cannot possibly yield a larger area than the current maximum.
                    - Mathematical Guarantee: It's mathematically impossible for a pair involving
                    a shorter line (than the one just considered) and a narrower width to produce a larger area.

            Proof by Contradiction
                Assuming Moving the Taller Line Could Help:
                    - Contradicts the Area Formula: The area would either stay the same
                    or decrease because the width decreases and the limiting height does not increase.
                    - No Benefit in Moving Taller Line: Hence,
                    moving the taller line's pointer doesn't help in finding a larger area.


        A demo (by me):
        imagine a list that is something like this:

        [1, 2, 3, 4, 5]
        at the start of the below alg, height will be min(1, 5) == 1-> width will be 4;
        At this point we will save this result, and discard 1, and we will get the height from min(2, 5);
        The reason we are not missing on any potential bigger areas by discarding one is:
        whatever number we pick, the width will decrease (because we already used up the highest width possible).
        whatever number we pick, we also cannot increase the height -> if we have a number bigger than 1,
        since we need to use the MIN of both, we will get 1;
        If it is smaller than 1 - well it is smaller;
        SO the product of height * width will always be smaller than what we comapred it with originally.
        This is how we are able to eliminate a whole meriad of tries.


        Basically, by using this approach, all potential Max Areas are considered:
        By moving the shorter line's pointer, all combinations that could possibly yield a larger area are evaluated.
        Inefficient Combinations are Skipped: Combinations that cannot surpass the current
        maximum area are not explicitly checked, saving time.
        :type height: List[int]
        :rtype: int
        """
        ### The trick here is two fold:
        # Realize that after the i and j pointers meet, the heights will just repeat
        # Decide when to move the pointers to the next number;
        # I decided on moving the pointers left or right based on the side of whichever is the smallest
        # because the bigger pointer has a chance of giving us a bigger area.
        i = 0
        j = len(height) - 1
        max_area = float("-inf")
        while i < j:
            a = height[i]
            b = height[j]
            width = j - i
            h = min(a, b)
            if h == a:
                i += 1
            else:
                j -= 1
            area = width * h
            if area > max_area:
                max_area = area
        return max_area


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
expected = 49
sol = Solution()
print(sol.maxArea(height))
print(f"{expected=}")
