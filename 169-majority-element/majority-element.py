class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # By Boyer Moore voting algorithm

        currFreq = 0
        currElem = 0

        for num in nums:
            if num == currElem:
                currFreq += 1
            else:
                currFreq -= 1

            if currFreq < 0:
                currElem = num
                currFreq = 1

        return currElem