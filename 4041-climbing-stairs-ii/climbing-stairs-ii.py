class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [-1 for _ in range(n + 1)]

        def climbStairsUtil(n : int) -> int:
            if n < 0:
                return 0
            if dp[n] != -1:
                return dp[n]

            oneStepBelow = climbStairsUtil(n - 1) + 1
            twoStepsBelow = climbStairsUtil(n - 2) + 4
            threeStepsBelow = climbStairsUtil(n - 3) + 9

            dp[n] = costs[n] + min(oneStepBelow, twoStepsBelow, threeStepsBelow)
            return dp[n]

        return climbStairsUtil(n - 1)