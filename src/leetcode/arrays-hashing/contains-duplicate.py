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