class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1 for _ in range(n + 1)]

        def climbStairsUtil(n: int) -> int:
            if n < 0:
                return 0
            if n <= 1:
                dp[n] = 1
                return dp[n]
            if dp[n] != -1:
                return dp[n]
            dp[n] = climbStairsUtil(n - 1) + climbStairsUtil(n - 2)
            return dp[n]

        return climbStairsUtil(n)