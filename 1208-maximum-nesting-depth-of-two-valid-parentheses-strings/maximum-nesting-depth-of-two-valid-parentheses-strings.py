class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        answer = [0] * len(seq)
        depth = 0

        for idx, char in enumerate(seq):
            if char == ')':
                depth -= 1
            
            answer[idx] = depth & 1

            if char == '(':
                depth += 1

        return answer