class Solution:
    def maxDepth(self, s: str) -> int:
        maxNestingDepth = 0
        currDepth = 0

        for char in s:
            if char == '(':
                currDepth += 1
                maxNestingDepth = max(maxNestingDepth, currDepth)
            elif char == ')':
                currDepth -= 1

        return maxNestingDepth