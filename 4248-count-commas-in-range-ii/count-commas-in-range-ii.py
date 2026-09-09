class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        multiplicationFactor = 1000
        ans = 0

        while multiplicationFactor <= n:
            count = n + 1 - multiplicationFactor
            ans += count
            multiplicationFactor *= 1000
        
        return ans