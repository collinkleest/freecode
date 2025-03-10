# https://leetcode.com/problems/valid-palindrome


"""
use two pointers
start at the start of array and end of the array
if we find something that is not alphanumeric ignore the character
if they are alphanumeric check the values equality

time complexity O(N/2)
space complexity O(1)
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        r, l = 0, len(s) - 1

        while r < l:
            if not s[r].isalnum():
                r += 1
                continue
            if not s[l].isalnum():
                l -= 1
                continue

            if s[r].lower() != s[l].lower():
                return False
            else:
                r += 1
                l -= 1

        return True
