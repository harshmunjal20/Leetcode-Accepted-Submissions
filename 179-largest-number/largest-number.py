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
            elif a + b < b + a:
                return 1
            else:
                return 0

        strs = []

        for currNum in nums:
            strs.append(str(currNum))
        
        strs.sort(key = cmp_to_key(compare))

        ansStr = "".join(strs)

        return ansStr if ansStr[0] != '0' else "0"