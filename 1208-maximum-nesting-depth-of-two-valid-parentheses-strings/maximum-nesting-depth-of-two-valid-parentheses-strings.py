class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        answer = [0] * len(seq)
        currDepth = 0

        for idx, char in enumerate(seq):
            if char == ')':
                currDepth -= 1

            answer[idx] = currDepth & 1

            if char == '(':
                currDepth += 1

        return answer