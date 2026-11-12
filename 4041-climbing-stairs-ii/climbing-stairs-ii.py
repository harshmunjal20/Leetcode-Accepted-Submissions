class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [-1 for _ in range(n)]

        for idx in range(n):
            oneStepBelow = dp[idx - 1] + 1 if idx - 1 >= 0 else 1
            twoStepsBelow = dp[idx - 2] + 4 if idx - 2 >= 0 else 4
            threeStepsBelow = dp[idx - 3] + 9 if idx - 3 >= 0 else 9

            dp[idx] = costs[idx] + min(oneStepBelow, twoStepsBelow, threeStepsBelow)

        return dp[n - 1]