class Solution(object):
    def minOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0

        while n:
            if n & 1:
                if n & 3 == 3:
                    n += 1
                else:
                    n -= 1
                count += 1
            else:
                n >>= 1
        
        return count