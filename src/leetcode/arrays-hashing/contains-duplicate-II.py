#  https://leetcode.com/problems/contains-duplicate-ii


"""
brute force solution, too slow
space complexity O(1)
time complexity O(N^2)
"""


from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and abs(i - j) <= k:
                    return True
        return False


"""
using hashmap to keep track of last nearby dupp
time complexity O(n)
space complexity O(n)
"""


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = dict()

        for i, num in enumerate(nums):
            if num in seen:
                if abs(seen[num] - i) <= k:
                    return True
                else:
                    seen[num] = i
            else:
                seen[num] = i

        return False


"""
less code more readable
same solution as above
"""


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = dict()

        for i, num in enumerate(nums):
            if num in seen and abs(seen[num] - i) <= k:
                return True
            seen[num] = i

        return False
