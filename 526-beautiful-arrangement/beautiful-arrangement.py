class Solution(object):
    def countArrangement(self, n):
        """
        :type n: int
        :rtype: int
        """

        def permutation(idx, bitMask, dp):
            if idx > n:
                return 1

            if dp[idx][bitMask] != -1:
                return dp[idx][bitMask]

            numWays = 0

            for i in range(1, n + 1):
                if not bitMask & (1 << (i - 1)):
                    if i % idx == 0 or idx % i == 0:
                        numWays += permutation(idx + 1, bitMask | (1 << (i - 1)), dp)

            dp[idx][bitMask] = numWays
            return numWays

        dp = [[-1 for _ in range(1 << n)] for _ in range(n + 1)]
        return permutation(1, 0, dp)
        