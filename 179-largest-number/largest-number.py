class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        numsStr = [str(num) for num in nums]

        numsStr.sort(key= lambda x : x * 10, reverse = True)

        return "".join(numsStr) if numsStr[0] != '0' else "0"