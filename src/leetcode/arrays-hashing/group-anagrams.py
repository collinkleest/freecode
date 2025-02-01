# https://leetcode.com/problems/group-anagrams/

from typing import List

"""
first attempt brute force solution
time complexity O(n log(n))
space complexity O(n)
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = []
        anaMap = {}
        for s in strs:
            ss = sorted(s)
            ss = "".join(ss)
            if ss in anaMap:
                anaMap[ss].append(s)
            else:
                anaMap[ss] = [s]
        for key in anaMap:
            grouped.append(anaMap[key])
        return grouped