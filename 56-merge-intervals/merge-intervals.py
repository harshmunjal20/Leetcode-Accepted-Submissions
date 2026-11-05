class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        ans = []

        for [start, end] in intervals:
            if ans and ans[-1][1] >= start:
                ans[-1][1] = max(ans[-1][1], end)
            else:
                ans.append([start, end])
        
        return ans