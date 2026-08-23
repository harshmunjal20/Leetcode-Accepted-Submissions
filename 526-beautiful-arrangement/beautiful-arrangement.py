from functools import lru_cache

class Solution:
    def countArrangement(self, n: int) -> int:
        @lru_cache
        def permutation(idx, bitMask):
            if idx > n:
                return 1

            numWays = 0

            for i in range(1, n + 1):
                if not bitMask & (1 << (i - 1)):
                    if i % idx == 0 or idx % i == 0:
                        numWays += permutation(idx + 1, bitMask | (1 << (i - 1)))

            return numWays

        return permutation(1, 0)