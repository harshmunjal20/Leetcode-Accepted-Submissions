class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        # make a dp of max days
        maxDay = days[len(days) - 1]
        dp = [None] * (maxDay + 1)
        dp[0] = 0
        daysSet = set(days)

        for currDay in range(1, maxDay + 1):
            if currDay not in daysSet:
                dp[currDay] = dp[currDay - 1]
                continue

            weekStore = 0
            monthStore = 0

            if currDay - 7 >= 0:
                weekStore = dp[currDay - 7]
            
            if currDay - 30 >= 0:
                monthStore = dp[currDay - 30]
            
            dp[currDay] = min(costs[0] + dp[currDay - 1], costs[1] + weekStore, costs[2] + monthStore)

        return dp[maxDay]