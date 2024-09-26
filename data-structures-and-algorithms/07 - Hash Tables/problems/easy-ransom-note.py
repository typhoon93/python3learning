"""

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.



Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true


Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
"""
import collections


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        My initial code
        SC = O(n) -> len ransomNote
        TC = O( n + m)
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransom_note_char_counts = collections.Counter(ransomNote)
        for char in magazine:
            if char in ransom_note_char_counts:
                ransom_note_char_counts[char] -= 1
        for char_count in ransom_note_char_counts.values():
            if char_count > 0:
                return False
        return True


    def canConstruct(self, ransomNote, magazine):
        """

        My solution, Optmized with early exits; we del all chars that are at 0,
        we check ransom not on each del
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if not ransomNote:
            return True
        if not magazine:
            return False

        ransom_note_char_counts = collections.Counter(ransomNote)
        for char in magazine:
            if char in ransom_note_char_counts:
                ransom_note_char_counts[char] -= 1
                if ransom_note_char_counts[char] == 0:
                    del ransom_note_char_counts[char]
                    if not ransom_note_char_counts:
                        return True
        return False

ransomNote = "a"; magazine = "b"
expected = False
sol = Solution()
res = sol.canConstruct(ransomNote, magazine)
print(res)
print(f"{expected=}")