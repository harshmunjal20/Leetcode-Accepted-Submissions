class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        maxLen = 0
        maxLen = max(maxLen, seats.index(1))
        seats.reverse()
        prevOneIdx = seats.index(1)
        maxLen = max(maxLen, prevOneIdx)
        totalSeats = len(seats)
        idx = prevOneIdx

        while idx < totalSeats:
            if seats[idx] == 1:
                groupSize = (idx - prevOneIdx) / 2
                maxLen = max(maxLen, groupSize)
                prevOneIdx = idx
            
            idx += 1

        return maxLen