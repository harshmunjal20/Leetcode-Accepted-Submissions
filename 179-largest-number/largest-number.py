from functools import cmp_to_key

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """

        def compare(a, b):
            if a + b > b + a:
                return -1
            else:
                return 1

        numsStr = [str(num) for num in nums]

        numsStr.sort(key=cmp_to_key(compare))

        maxNumber = "".join(numsStr)

        return maxNumber if maxNumber[0] != '0' else "0"