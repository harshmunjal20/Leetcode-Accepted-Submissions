class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        for idx in range(1, len(nums) - 1):
            if nums[idx - 1] < nums[idx] > nums[idx + 1]:
                return idx
        
        if len(nums) >= 2:
            if nums[0] > nums[1]:
                return 0
            elif nums[len(nums) - 1] > nums[len(nums) - 2]:
                return len(nums) - 1
        
        return 0