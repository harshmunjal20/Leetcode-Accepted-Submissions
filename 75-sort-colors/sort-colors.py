class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j, runningIdx = 0, len(nums) - 1, 0

        while runningIdx <= j:
            if nums[runningIdx] == 0:
                nums[i], nums[runningIdx] = nums[runningIdx], nums[i]
                i += 1
                runningIdx += 1
            elif nums[runningIdx] == 1:
                runningIdx += 1
            else:
                nums[j], nums[runningIdx] = nums[runningIdx], nums[j]
                j -= 1