class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        minRemovals = 0
        intervals.sort(key=lambda x : x[1])
        prevEnd = -1e10

        for interval in intervals:
            currStart = interval[0]

            if prevEnd == -1e10 or prevEnd <= currStart : # non overlapping
                prevEnd = max(prevEnd, interval[1])
            else:
                minRemovals += 1
        
        return minRemovals