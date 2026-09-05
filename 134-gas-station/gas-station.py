class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        totalGas, totalCost = sum(gas), sum(cost)
        startIdx, runningGas = 0, 0

        if totalGas - totalCost < 0:
            return -1

        for idx in range(len(gas)):
            runningGas += gas[idx] - cost[idx]

            if runningGas < 0:
                runningGas = 0
                startIdx = idx + 1

        return startIdx