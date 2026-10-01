class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        currDepth = 0
        maxDepth = 0
        answer = [0] * len(seq)

        for char in seq:
            if char == '(':
                currDepth += 1
                maxDepth = max(maxDepth, currDepth)
            else:
                currDepth -= 1
        
        depth = maxDepth // 2

        for idx, char in enumerate(seq):
            if char == ')':
                currDepth -= 1

            if currDepth < depth:
                answer[idx] = 1

            if char == '(':
                currDepth += 1

        return answer