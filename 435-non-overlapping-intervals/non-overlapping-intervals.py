class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key = lambda x : x[1])
        prevEnd = -1e10
        count = 0

        for interval in intervals:
            currStart = interval[0]
            currEnd = interval[1]

            if prevEnd == -1e10 or prevEnd <= currStart: # non overlapping
                prevEnd = currEnd
            else:
                count += 1

        return count
