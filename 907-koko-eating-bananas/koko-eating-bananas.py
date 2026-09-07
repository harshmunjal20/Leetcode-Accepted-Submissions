class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """

        left = 1
        right = max(piles)

        while left <= right:
            mid = left + (right - left) / 2

            currHours = 0

            for bananas in piles:
                currHours += (bananas + mid - 1) / mid

            if currHours <= h:
                right = mid - 1
            else:
                left = mid + 1

        return left