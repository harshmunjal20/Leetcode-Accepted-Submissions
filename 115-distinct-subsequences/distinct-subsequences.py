class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if len(s) < len(t):
            return 0

        dp = [0] * (len(t) + 1)

        dp[len(t)] = 1

        for idxS in range(len(s) - 1 , -1, -1):
            currDp = [0] * (len(t) + 1)
            currDp[len(t)] = 1

            for idxT in range(len(t) - 1, -1, -1):
                if s[idxS] == t[idxT]:
                    currDp[idxT] = dp[idxT + 1] + dp[idxT]
                else:
                    currDp[idxT] = dp[idxT]
            
            dp = currDp

        return dp[0]