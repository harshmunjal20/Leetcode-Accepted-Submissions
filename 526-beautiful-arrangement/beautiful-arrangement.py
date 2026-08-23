class Solution(object):
    def countArrangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        def permutation(idx, bitMask, dp):
            if idx > n:
                return 1
            
            if dp[bitMask] != -1:
                return dp[bitMask]

            numWays = 0

            for i in range(1, n + 1):
                if not bitMask & (1 << (i - 1)):
                    if idx % i == 0 or i % idx == 0:
                        numWays += permutation(idx + 1, bitMask | (1 << (i - 1)), dp)
            
            dp[bitMask] = numWays
            return numWays
        
        dp = [-1 for _ in range(1 << n)] 
        return permutation(1, 0, dp)