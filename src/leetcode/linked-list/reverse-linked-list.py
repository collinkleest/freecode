# https://leetcode.com/problems/reverse-linked-list

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""

init a null node
we will point to this and move this node along so our head can point to it

we will need to use a temp node as well to keep the next node to track

time complexity O(n)
space complexity O(1)
"""


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = None

        while head:
            temp = head.next
            head.next = node
            node = head
            head = temp

        return node
