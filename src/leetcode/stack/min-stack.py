
# https://leetcode.com/problems/min-stack


"""
using sorting not ideal because of time complexity
have to re-sort the stack each time we add or pop an element which is O(n log (n))
"""


class MinStack:

    def __init__(self):
        self.stack = []
        self.sortedStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.sortedStack = sorted(self.stack)

    def pop(self) -> None:
        self.stack.pop()
        self.sortedStack = sorted(self.stack)

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        return self.sortedStack[0]
