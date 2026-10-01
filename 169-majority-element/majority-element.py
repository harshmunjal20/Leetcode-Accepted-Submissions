class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # By boyer-moore voting algorithm

        currElem = 0
        currFreq = 0

        for num in nums:
            if currElem == num:
                currFreq += 1
            else:
                currFreq -= 1

            if currFreq < 0:
                currElem = num
                currFreq = 1
        
        return currElem