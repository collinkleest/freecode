# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

from typing import List

"""
initial implementation

pointer on both ends of the array
since we know the array is sorted we can then sum up our left and right pointers
if the sum is larger than the target we know we need to move the left pointer
if the sum is smaller than the target then we know we need to move the right pointer

time complexity O(n)
space complexity O(1)
"""


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            total = numbers[l] + numbers[r]
            if total == target:
                return [l + 1, r + 1]
            elif total > target:
                r -= 1
            else:
                l += 1
