class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        low, high = 1, x

        while low <= high:
            mid = low + (high - low) / 2

            product = mid * mid

            if product <= x:
                low = mid + 1
            else:
                high = mid - 1

        return high
        