class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        totalSum = sum(nums)

        if x > totalSum:
            return -1

        i = 0
        currSum = 0
        maxSize = -1e9
        n = len(nums)
        toFindSum = totalSum - x

        for j in range(n):
            currSum += nums[j]

            while currSum > toFindSum:
                currSum -= nums[i]
                i += 1
            
            if currSum == toFindSum:
                maxSize = max(maxSize, j - i + 1)

            j += 1
        
        if maxSize == -1e9:
            return -1
        
        return n - maxSize