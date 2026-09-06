import bisect

class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        dp = [[-1 for _ in range(3)] for _ in range(len(days))]

        def lower_bound(days, target):
            low = 0
            high = len(days) - 1

            while low <= high:
                mid = low + (high - low) / 2

                if days[mid] >= target:
                    high = mid - 1
                else:
                    low = mid + 1
            
            return low

        def minCostTicketsUtil(currIdx, currPass):
            if currIdx >= len(days):
                return 0
            
            if dp[currIdx][currPass] != -1:
                return dp[currIdx][currPass]
            
            currDay = days[currIdx]
            oneDayCost = costs[0] + minCostTicketsUtil(lower_bound(days, currDay + 1), 0)
            oneWeekCost = costs[1] + minCostTicketsUtil(lower_bound(days, currDay + 7), 1)
            oneMonthCost = costs[2] + minCostTicketsUtil(lower_bound(days, currDay + 30), 2)

            dp[currIdx][currPass] = min(oneDayCost, oneWeekCost, oneMonthCost)
            return dp[currIdx][currPass]

        currIdx = 0
        currPass = 0
        return minCostTicketsUtil(currIdx, currPass)
