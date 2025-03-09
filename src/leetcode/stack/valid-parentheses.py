# https://leetcode.com/problems/valid-parentheses


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracketMapping = {')': '(', '}': '{', ']': '['}

        for c in s:
            if c in bracketMapping.keys():
                if len(stack):
                    elem = stack.pop()
                    if bracketMapping[c] != elem:
                        return False
                else:
                    return False
            else:
                stack.append(c)

        return len(stack) == 0
