class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maxElem = max(nums)
        ans = 0

        for elem in nums:
            ans += maxElem - elem
        
        return ans