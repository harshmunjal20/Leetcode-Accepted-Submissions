class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix = [1]
        suffix = [1] * (len(nums) + 1)

        for num in nums:
            prefix.append(prefix[-1] * num)
        
        # start , stop , step
        for idx in range(len(nums) - 1, -1, -1):
            suffix[idx] = suffix[idx + 1] * nums[idx]

        for idx in range(len(nums) + 1):
            nums[idx - 1] = prefix[idx - 1] * suffix[idx]

        return nums