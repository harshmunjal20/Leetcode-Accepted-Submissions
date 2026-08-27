class Solution(object):
    def baseNeg2(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 0:
            return "0"
            
        ans = []

        while n != 0:
            rem = abs(n) % 2
            ans.append(str(rem))
            n = (rem - n) / 2
        
        ansFinal = "".join(ans)
        return ansFinal[::-1]