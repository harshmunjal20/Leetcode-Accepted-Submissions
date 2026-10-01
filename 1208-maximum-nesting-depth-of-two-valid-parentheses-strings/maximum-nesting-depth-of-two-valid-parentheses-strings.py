class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        answer = [0] * len(seq)
        maxValidOpen = 0
        currValidOpen = 0

        for char in seq:
            if char == '(':
                currValidOpen += 1
                maxValidOpen = max(maxValidOpen, currValidOpen)
            else:
                currValidOpen -= 1
        
        minDepth = maxValidOpen // 2
        currDepth = 0

        for idx, char in enumerate(seq):
            if char == ')':
                currDepth -= 1

            if currDepth < minDepth:
                answer[idx] = 1

            if char == '(':
                currDepth += 1

        return answer