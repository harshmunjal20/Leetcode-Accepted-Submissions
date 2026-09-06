import bisect

class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        dp = [[1e10 for _ in range(3)] for _ in range(len(days) + 1)]
        idx = len(days) - 1

        dp[len(days)][0] = dp[len(days)][1] = dp[len(days)][2] = 0
        
        while idx >= 0:
            currDay = days[idx]

            dp[idx][0] = dp[idx][1] = dp[idx][2] = min(costs[0] + dp[bisect.bisect_left(days, currDay + 1)][0], costs[1] + dp[bisect.bisect_left(days, currDay + 7)][1], costs[2] + dp[bisect.bisect_left(days, currDay + 30)][2])

            idx -= 1

        return dp[0][0]