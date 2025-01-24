# https://leetcode.com/problems/contains-duplicate/description/

from typing import List

"""
hashmap aka dict solution
O(N) time complexity
O(N) space complexity
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dupp_map = {}
        for num in nums:
            if dupp_map.get(num):
                return True
            else:
                dupp_map[num] = True
        return False


"""
using set
O(N) time complexity
O(N) space complexity
"""
class SolutionV2:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dupp_set = set()
        for num in nums:
            if num in dupp_set:
                return True
            else:
                dupp_set.add(num)
        return False

"""
brute force method
time complexity O(n^2)
space complexity O(1)
"""
class SolutionV3:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False


"""
sorting method
time complexity O(1)
space complexity O(n log(n))
"""
class SolutionV4:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                return True
        return False
    

"""
set length method
time complexity O(n)
space complexity O(n)
"""
class SolutionV4:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)


"""
Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true

"""