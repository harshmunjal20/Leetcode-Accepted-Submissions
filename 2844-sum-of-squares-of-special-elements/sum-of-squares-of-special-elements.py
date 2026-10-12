class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for idx in range(1, len(nums) + 1):
            if n % idx == 0:
                ans += nums[idx - 1] ** 2

        return ans