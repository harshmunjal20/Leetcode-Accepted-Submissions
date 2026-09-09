class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if len(s) < len(t):
            return 0

        dp = [[-1 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]

        def calculateSubsequences(idxS, idxT):
            if idxT == len(t):
                return 1

            if idxS == len(s):
                return 0

            if dp[idxS][idxT] != -1:
                return dp[idxS][idxT]

            count = 0

            if s[idxS] == t[idxT]:
                count += calculateSubsequences(idxS + 1, idxT + 1)
            
            count += calculateSubsequences(idxS + 1, idxT)
            dp[idxS][idxT] = count
            return count

        idxS , idxT = 0, 0
        return calculateSubsequences(idxS, idxT)