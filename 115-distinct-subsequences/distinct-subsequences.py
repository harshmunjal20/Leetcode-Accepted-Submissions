class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if len(s) < len(t):
            return 0

        dp = [[0 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]

        for idxS in range(len(s) + 1):
            dp[idxS][len(t)] = 1

        for idxS in range(len(s) - 1 , -1, -1):
            for idxT in range(len(t) - 1, -1, -1):
                if s[idxS] == t[idxT]:
                    dp[idxS][idxT] = dp[idxS + 1][idxT + 1] + dp[idxS + 1][idxT]
                else:
                    dp[idxS][idxT] = dp[idxS + 1][idxT]

        return dp[0][0]