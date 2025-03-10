# https://leetcode.com/problems/3sum


"""
time complexity O(n * log(n)) + O(n^2) = O(n^2)
space complexity O(n) 
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the nums to make out two pointer solution work
        nums.sort()
        result = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return result
