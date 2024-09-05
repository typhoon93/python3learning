"""
https://leetcode.com/problems/relative-ranks/

You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.

The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:

The 1st place athlete's rank is "Gold Medal".
The 2nd place athlete's rank is "Silver Medal".
The 3rd place athlete's rank is "Bronze Medal".
For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").
Return an array answer of size n where answer[i] is the rank of the ith athlete.



Example 1:

Input: score = [5,4,3,2,1]
Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
Explanation: The placements are [1st, 2nd, 3rd, 4th, 5th].
Example 2:

Input: score = [10,3,8,9,4]
Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
Explanation: The placements are [1st, 5th, 3rd, 2nd, 4th].



Constraints:

n == score.length
1 <= n <= 104
0 <= score[i] <= 106
All the values in score are unique.

"""
import heapq
from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        """
        My solution

        SC: O(n)
        TC: O(n log n) (due to sorting, evertthing else is O(n)

        """
        sorted_score = sorted(score, reverse=True)
        mapping = {
            0: "Gold Medal",
            1: "Silver Medal",
            2: "Bronze Medal",
        }
        score_rank = {score: str(rank + 1) if rank not in mapping else mapping[rank] for rank, score in
                      enumerate(sorted_score)}
        return [score_rank[player_score] for player_score in score]

    def findRelativeRanks(self, score: List[int]) -> List[str]:
        """
        https://leetcode.com/problems/relative-ranks/
        return a result with the ranking of the player, instead of their score;
        score[i] is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.
        First three should be "Gold Medal", "Silver Medal", "Bronze Medal" respectively, and the others just str(place)

        Input: score = [5,4,3,2,1]
        Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
        Explanation: The placements are [1st, 2nd, 3rd, 4th, 5th].

        Solution using heap;
        TC: O(n log n)
        SC: O(n)
        """
        N = len(score)
        heap = []  # heapq works on a list in place.
        for index, score in enumerate(score):
            heapq.heappush(heap, (
                -score, index))  # we use the first element of the tuple to compare, if equal -> then comare the second.
            # check tuple comparison if you need understading.
            # we use nagative score because we want max-heap type;, so it is a hack.

        # Assign ranks to the athletes
        result = [None] * N
        medals = ("Gold Medal", "Silver Medal", "Bronze Medal")
        rank = 0
        while heap:
            neg_score, idx = heapq.heappop(heap)
            if rank < 3:
                result[idx] = medals[rank]
            else:
                result[idx] = str(rank + 1)
            rank += 1

        return result

    def findRelativeRanks(self, score: List[int]) -> List[str]:
        """
        A solution i found on leet code, which manages to solve it with Linear time time complexity:
        This approach is efficient if m (the maximum score) is not significantly larger than n (the number of scores).
        It's particularly space-efficient when the range of scores is close to the number of scores, making it almost an application of counting sort.
        TC: O(m + n)
        SC: O(m)
        m is max(score), n is len(score)

        Clever approach, a takeaway here is to look at the constraints of the exercise carefully, and a simple hack like this may emerge from the data we have.
        """
        max_score = max(score)  # O(n)
        index_lst = [None] * (max_score + 1)  # zero based indexing, that's why we have +1
        print(index_lst)
        for i, s in enumerate(
                score):  # here we create a clever mapping: we set the score position in this index_lst to the index of player
            index_lst[s] = i
        print(index_lst)
        rank = 0
        res = [None] * len(score)
        for i in range(max_score, -1, -1):
            if index_lst[i] == None:
                continue
            print(i, rank)  # we map the result
            rank += 1
            if rank == 1:
                res[index_lst[i]] = 'Gold Medal'
            elif rank == 2:
                res[index_lst[i]] = 'Silver Medal'
            elif rank == 3:
                res[index_lst[i]] = 'Bronze Medal'
            else:
                res[index_lst[i]] = str(rank)

        return res


if __name__ == "__main__":
    sol = Solution()
    score = [50, 4, 3, 2, 1]
    print(sol.findRelativeRanks(score))
