class Solution(object):
    def countSubarrays(self, nums, minK, maxK):
        """
        :type nums: List[int]
        :type minK: int
        :type maxK: int
        :rtype: int
        """
        prevInvalidIdx = -1
        prevMinIdx = -1
        prevMaxIdx = -1
        count = 0

        for idx in range(len(nums)):
            if nums[idx] == minK:
                prevMinIdx = idx
            
            if nums[idx] == maxK:
                prevMaxIdx = idx
            elif nums[idx] > maxK or nums[idx] < minK:
                prevInvalidIdx = idx
            
            if prevMinIdx > prevInvalidIdx and prevMaxIdx > prevInvalidIdx:
                count += min(prevMinIdx, prevMaxIdx) - prevInvalidIdx
        
        return count