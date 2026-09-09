from math import isqrt

class Solution(object):
    def countPrimes(self, n):
        if n <= 2:
            return 0

        dp = bytearray(b'\x01') * n
        dp[0] = dp[1] = 0

        for p in range(2, isqrt(n) + 1):
            if dp[p]:
                dp[p * p:n:p] = b'\x00' * (((n - 1 - p * p) // p) + 1)

        return sum(dp)