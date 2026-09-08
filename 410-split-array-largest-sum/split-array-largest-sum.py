class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def isValid(mid, nums):
            students = 1
            currSum = 0

            for elem in nums:
                currSum += elem

                if elem > mid:
                    return False
                
                if currSum > mid:
                    students += 1
                    currSum = elem

            return students <= k

        low = 0
        high = sum(nums)

        while low <= high:
            mid = low + (high - low) / 2

            if isValid(mid, nums):
                high = mid - 1
            else:
                low = mid + 1
        
        return low