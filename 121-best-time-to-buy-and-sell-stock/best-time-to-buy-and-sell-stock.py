class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buyPrice , profit = 1e10, 0

        for currPrice in prices:
            if currPrice < buyPrice:
                buyPrice = currPrice
            else:
                profit = max(profit, currPrice - buyPrice)

        return profit