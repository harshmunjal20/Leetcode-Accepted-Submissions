class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        def daysToComplete(mid : int) -> int:
            currDays = 1
            currSum = 0

            for weight in weights:
                currSum += weight

                if weight > mid:
                    return 1e10
                
                if currSum > mid:
                    currSum = weight
                    currDays += 1

            return currDays 

        low = 1
        high = sum(weights)

        while low <= high:
            mid = low + (high - low) // 2

            if daysToComplete(mid) > days:
                low = mid + 1
            else:
                high = mid - 1
        
        return low