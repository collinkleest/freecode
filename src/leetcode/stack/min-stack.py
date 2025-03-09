
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


"""
keep track of min value when adding to stack
keep tuples in stack 
each stack element maps to (val, minVal)
faster time complexity O(1)
space complexity O(n)
"""


class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if self.stack:
            topMin = self.getMin()
            if topMin < val:
                self.stack.append(tuple([val, topMin]))
            else:
                self.stack.append(tuple([val, val]))
        else:
            self.stack.append(tuple([val, val]))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[len(self.stack) - 1][0]

    def getMin(self) -> int:
        return self.stack[len(self.stack) - 1][1]
