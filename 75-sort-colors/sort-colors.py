from collections import Counter

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freqMap = Counter(nums)
        idx = 0

        for num in range(3):
            for _ in range(freqMap[num]):
                nums[idx] = num
                idx += 1