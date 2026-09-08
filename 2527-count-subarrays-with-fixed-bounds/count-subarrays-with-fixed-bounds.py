from collections import deque

class Solution(object):
    def countSubarrays(self, nums, minK, maxK):
        """
        :type nums: List[int]
        :type minK: int
        :type maxK: int
        :rtype: int
        """
        minDq = []
        maxDq = []
        count = 0
        prevInvalidIdx = -1

        for idx in range(len(nums)):
            if nums[idx] > maxK or nums[idx] < minK:
                prevInvalidIdx = idx
                del minDq[:]
                del maxDq[:]
                continue
            
            while minDq and nums[minDq[-1]] >= nums[idx]:
                minDq.pop()
            
            minDq.append(idx)

            while maxDq and nums[maxDq[-1]] <= nums[idx]:
                maxDq.pop()
            
            maxDq.append(idx)
        
            if nums[minDq[0]] == minK and nums[maxDq[0]] == maxK:
                count += max(0, min(minDq[0], maxDq[0]) - prevInvalidIdx)

        return count