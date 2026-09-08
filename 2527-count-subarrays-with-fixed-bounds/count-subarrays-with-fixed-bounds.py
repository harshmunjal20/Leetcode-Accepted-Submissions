class Solution(object):
    def countSubarrays(self, nums, minK, maxK):
        """
        :type nums: List[int]
        :type minK: int
        :type maxK: int
        :rtype: int
        """
        lastMinIdx = -1
        lastMaxIdx = -1
        prevInvalidIdx = -1
        count = 0

        for idx in range(len(nums)):
            if nums[idx] == minK :
                lastMinIdx = idx
            if nums[idx] == maxK:
                lastMaxIdx = idx
            elif minK > nums[idx] or nums[idx] > maxK:
                prevInvalidIdx = idx
            
            count += max(0, min(lastMinIdx, lastMaxIdx) - prevInvalidIdx)

        return count