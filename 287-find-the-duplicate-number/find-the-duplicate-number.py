class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        n = len(nums)
        isPresent = [False] * (n + 1)

        for num in nums:
            if isPresent[num]:
                return num
            
            isPresent[num] = True
        
        return -1