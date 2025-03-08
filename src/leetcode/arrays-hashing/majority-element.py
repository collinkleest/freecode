
# https://leetcode.com/problems/majority-element/

from typing import List


"""
using hashmap solutio
O(N) time complexity
O(N - 1) space complexity 
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elements = {}
        threshold = len(nums) / 2
        for num in nums:
            elements[num] = elements.get(num, 0) + 1
        for elem, count in elements.items():
            if count > threshold: 
                return elem