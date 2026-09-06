import bisect

class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        dp = [[-1 for _ in range(3)] for _ in range(len(days))]

        def minCostTicketsUtil(currIdx, currPass):
            if currIdx >= len(days):
                return 0
            
            if dp[currIdx][currPass] != -1:
                return dp[currIdx][currPass]
            
            currDay = days[currIdx]
            oneDayPassCost = costs[0] + minCostTicketsUtil(bisect.bisect_left(days, currDay + 1), 0)
            oneWeekPassCost = costs[1] + minCostTicketsUtil(bisect.bisect_left(days, currDay + 7), 1)
            oneMonthPassCost = costs[2] + minCostTicketsUtil(bisect.bisect_left(days, currDay + 30), 2)

            dp[currIdx][currPass] = min(oneDayPassCost, oneWeekPassCost, oneMonthPassCost)
            return dp[currIdx][currPass]

        currIdx = 0

        return minCostTicketsUtil(currIdx, 0)