class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        i, j, k = 0, 0, 0
        maxDist = 0
        totalSeats = len(seats)

        while k < totalSeats:
            while j < totalSeats and seats[j] == 1:
                j += 1

            i = j - 1
            k = j + 1

            while k < totalSeats and seats[k] == 0:
                k += 1

            while j < totalSeats and j < k:
                maxDist = max(maxDist, min(abs(i - j) if i >= 0 else 1e10, (abs(k - j) if k < totalSeats else 1e10)))
                j += 1


        return maxDist
