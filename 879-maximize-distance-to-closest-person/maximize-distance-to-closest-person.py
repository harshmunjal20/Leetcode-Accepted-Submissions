class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        # bad approach : creating a next array
        next = []
        idx = len(seats) - 1
        nextIdx = 1e10

        while idx >= 0:
            if seats[idx] == 1:
                nextIdx = idx

            next.append(nextIdx)
            idx -= 1

        next.reverse()
        prevIdx = -1e10
        maxLen = 0

        for idx in range(len(seats)):
            if seats[idx] == 1:
                prevIdx = idx
            elif seats[idx] == 0:
                maxLen = max(maxLen, min(idx - prevIdx, next[idx] - idx))
        
        return maxLen