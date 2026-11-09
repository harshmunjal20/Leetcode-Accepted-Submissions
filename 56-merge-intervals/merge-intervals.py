class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        ans = []

        for [startTime, endTime] in intervals:
            if ans and ans[-1][1] >= startTime:
                ans[-1][1] = max(ans[-1][1], endTime)
            else:
                ans.append([startTime, endTime])
            
        return ans