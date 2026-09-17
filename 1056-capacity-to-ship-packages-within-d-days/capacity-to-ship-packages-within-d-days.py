class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:

        def canShipPackages(mid: int, weights: list[int]) -> int:
            numDays = 1
            currSum = 0

            for weight in weights:
                currSum += weight

                if weight > mid:
                    return False

                if currSum > mid:
                    numDays += 1
                    currSum = weight

            return numDays <= days

        low = 1
        high = sum(weights)

        while low <= high:
            mid = low + (high - low) // 2
            print(mid)

            if canShipPackages(mid, weights):
                high = mid - 1
            else:
                low = mid + 1
            
        return low