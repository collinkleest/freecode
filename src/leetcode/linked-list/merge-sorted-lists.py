# https://leetcode.com/problems/merge-two-sorted-lists/


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
its just simply awful
time complexity O(n log n)
space complexity O(n)
"""


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        arr1 = []
        arr2 = []

        while list1:
            arr1.append(list1.val)
            list1 = list1.next

        while list2:
            arr2.append(list2.val)
            list2 = list2.next

        arr1.extend(arr2)
        arr1.sort()
        result = ListNode()
        head = result
        for i, num in enumerate(arr1):
            temp = ListNode()
            result.val = num
            if i == len(arr1) - 1:
                result.next = None
                break
            result.next = temp
            result = temp
        return head
