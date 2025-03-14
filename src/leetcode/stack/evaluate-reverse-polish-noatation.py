# https://leetcode.com/problems/evaluate-reverse-polish-notation

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                stack.append(stack.pop() + stack.pop())
            elif token == '*':
                stack.append(stack.pop() * stack.pop())
            elif token == '/':
                val1, val2 = stack.pop(), stack.pop()
                stack.append(int(val2 / val1))
            elif token == '-':
                val1, val2 = stack.pop(), stack.pop()
                stack.append(val2 - val1)
            else:
                stack.append(int(token))
        return stack.pop()
