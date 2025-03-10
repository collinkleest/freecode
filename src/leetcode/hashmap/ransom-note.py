# https://leetcode.com/problems/ransom-note


"""

time complexity O(N)
space complexity O(N)

"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNoteMap, magazineMap = dict(), dict()

        for char in ransomNote:
            ransomNoteMap[char] = ransomNoteMap.get(char, 0) + 1

        for char in magazine:
            magazineMap[char] = magazineMap.get(char, 0) + 1

        for char, count in ransomNoteMap.items():
            if char not in magazineMap:
                return False
            elif magazineMap[char] < count:
                return False
        return True
