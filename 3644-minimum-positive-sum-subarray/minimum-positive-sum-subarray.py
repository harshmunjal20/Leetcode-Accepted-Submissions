class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        minSum = 1e10

        for i in range(len(nums)):
            sum = 0

            for j in range(i, len(nums)):
                sum += nums[j]
                if sum > 0 and (l <= j - i + 1 <= r):
                    minSum = min(minSum, sum)

        return minSum if minSum != 1e10 else -1
                