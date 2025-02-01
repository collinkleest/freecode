# https://leetcode.com/problems/top-k-frequent-elements/

from collections import defaultdict
from typing import List



"""
initial solution
very slow
good memory usage tho
time complexity o(k * n)
space complexity O(n)
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsMap = defaultdict(int)
        for n in nums:
            numsMap[n] += 1
        res = []
        for i in range(k):
            highest = 0
            highestKey = 0
            for key, val in numsMap.items():
                if val > highest and key not in res:
                    highest = val
                    highestKey = key
            res.append(highestKey)
        return res
                

"""
slightly faster using sorting of values
time complexity O(n log(n))
space complexity O(n)
"""
class SolutionV2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsMap = defaultdict(int)
        for n in nums:
            numsMap[n] += 1
        sorted_dict = dict(sorted(numsMap.items(), key=lambda item: item[1], reverse=True))
        sorted_list = list(sorted_dict.keys())
        res = []
        for i in range(k):
            res.append(sorted_list[i])
        return res