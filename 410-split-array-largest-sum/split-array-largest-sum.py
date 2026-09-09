class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        low = 0
        high = sum(nums)

        def isValid(nums, mid):
            currStudent = 1
            currSum = 0

            for num in nums:
                currSum += num

                if num > mid:
                    return False
                
                if currSum >  mid:
                    currSum = num
                    currStudent += 1

            return currStudent <= k

        while low <= high:
            mid = low + (high - low) / 2

            if isValid(nums, mid):
                high = mid - 1
            else:
                low = mid + 1

        return low