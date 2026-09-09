class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        multiplicationFactor = 1000
        
        while multiplicationFactor <= n:
            count = n + 1 - multiplicationFactor
            ans += count
            multiplicationFactor *= 1000

        return ans