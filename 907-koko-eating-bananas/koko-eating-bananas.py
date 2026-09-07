class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """

        def hoursTaken(piles, bananas):
            hoursTaken = 0

            for currBananas in piles:
                if currBananas <= bananas:
                    hoursTaken += 1
                else:
                    hoursTaken += (currBananas / bananas) + (1 if (currBananas % bananas) != 0 else 0)

            return hoursTaken

        left = 1
        right = max(piles)
        minSpeed = 0

        while left <= right:
            mid = left + (right - left) / 2

            if hoursTaken(piles, mid) <= h:
                minSpeed = mid
                right = mid - 1
            else:
                left = mid + 1

        return minSpeed