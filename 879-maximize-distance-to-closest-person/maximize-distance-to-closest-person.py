class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        # first approach again
        totalSeats = len(seats)
        idx = totalSeats - 1
        next = []
        nextIdx = 1e10

        while idx >= 0:
            if seats[idx] == 1:
                nextIdx = idx

            next.append(nextIdx)
            idx -= 1

        next.reverse()
        prevIdx = -1e10
        maxLen = 0
        idx = 0

        while idx < totalSeats:
            if seats[idx] == 1:
                prevIdx = idx
            elif seats[idx] == 0:
                maxLen = max(maxLen, min(idx - prevIdx, next[idx] - idx))

            idx += 1

        return maxLen
