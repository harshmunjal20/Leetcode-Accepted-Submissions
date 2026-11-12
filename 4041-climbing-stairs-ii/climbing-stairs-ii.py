class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        first, second, third = 0, 0, 0

        for idx in range(n):
            oldThird = third
            third = costs[idx] + min(first + 9, second + 4, third + 1)
            first = second
            second = oldThird
        
        return third