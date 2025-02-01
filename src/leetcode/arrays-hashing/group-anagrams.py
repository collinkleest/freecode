# https://leetcode.com/problems/group-anagrams/

from typing import List
from collections import defaultdict

"""
first attempt brute force solution
time complexity O(m * n log(n))
space complexity O(n * m)
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
    
"""
simplified
time complexity O(m * n log(n))
space complexity O(n * m)
where n is the longest length of str[i]
and m is the length of strs
"""
class SolutionV2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaMap = defaultdict(list)
        for s in strs:
            ss = sorted(s)
            anaMap[tuple(ss)].append(s)
        return list(anaMap.values())
          


"""
fastest
time complexity O(n * m)
space complexity O(n * m)
"""
class SolutionV3:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaMap = defaultdict(list)
        for s in strs:
            count_arr = [0] * 26
            for c in s:
                count_arr[ord(c) - ord('a')] += 1
            anaMap[tuple(count_arr)].append(s)
        return list(anaMap.values())