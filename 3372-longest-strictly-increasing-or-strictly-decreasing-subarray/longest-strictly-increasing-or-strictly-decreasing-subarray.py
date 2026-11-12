class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        increasingMaxCount = 1
        currMaxCount = 1

        currMinCount = 1
        increasingMinCount = 1

        for idx in range(len(nums) - 1, 0, -1):
            if nums[idx] > nums[idx - 1]: # strictly increasing
                currMaxCount += 1
                increasingMaxCount = max(increasingMaxCount, currMaxCount)
            else:
                currMaxCount = 1

        for idx in range(len(nums) - 1):
            if nums[idx] > nums[idx + 1]: # strictly decreasing
                currMinCount += 1
                increasingMinCount = max(increasingMinCount, currMinCount)
            else:
                currMinCount = 1

        return max(increasingMinCount, increasingMaxCount)