class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        i, j = 0, 0
        sz = len(nums)
        currSum = sum(nums)
        minSize = 1e10

        if x > currSum:
            return -1
        elif currSum == x:
            return sz
        
        for j in range(sz):
            currSum -= nums[j]

            while currSum < x:
                currSum += nums[i]
                i += 1
            
            if currSum == x:
                minSize = min(minSize, sz - 1 - j + i)

        return minSize if minSize != 1e10 else -1

