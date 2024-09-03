"""
https://leetcode.com/problems/find-the-town-judge

In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.



Example 1:

Input: n = 2, trust = [[1,2]]
Output: 2
Example 2:

Input: n = 3, trust = [[1,3],[2,3]]
Output: 3
Example 3:

Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1


Constraints:

1 <= n <= 1000
0 <= trust.length <= 104
trust[i].length == 2
All the pairs of trust are unique.
ai != bi
1 <= ai, bi <= n

"""
import collections
from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        """
        an indicator of a someone being a town judge - n-1 people trust one person;
        for someone to be a town judge, they must not trust anybody
        n - number of people in town
        trust - a list of lists, showing a person and the person they trust.
        TC = O(n**2)
        SC = O(n + T) - T entries across all sets
        """
        if n == 1:
            return n

        relationships = collections.defaultdict(set)

        for trustor, trustee in trust:
            relationships[trustee].add(trustor)

        for trustee in relationships:
            if len(relationships[trustee]) >= n - 1:
                can_be_judge = True
                for trustor_list in relationships.values():
                    if trustee in trustor_list:
                        can_be_judge = False
                if can_be_judge:
                    return trustee
        return -1

    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        """
        GPT solution:
        we keep track of how many people each person trusts + how many they are trusted by using Counter.
        Simple approahc, you can do it using some other form of keeping track of the trusts count of each person (how many people they trust).
        very simple and the complexities become better:
        note that my approach above seems to beat this code when it comes to runtime and memory usage in LC.
        SC O(n)
        TC O(T+n) , where T is the len(trusts) list
        """
        if n == 1 and not trust:
            return 1

        trusts = collections.Counter()
        trusted_by = collections.Counter()

        for a, b in trust:
            trusts[a] += 1
            trusted_by[b] += 1

        for i in range(1, n+1):
            if trusts[i] == 0 and trusted_by[i] == n-1:
                return i
        return -1



if __name__ == "__main__":
    sol = Solution()
    trust = [[1,3],[2,3],[3,1]]
    print(sol.findJudge(3, trust))
