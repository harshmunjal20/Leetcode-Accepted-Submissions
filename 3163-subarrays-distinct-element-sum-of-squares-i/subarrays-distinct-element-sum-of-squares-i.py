class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        ans = 0

        for rowIdx in range(len(nums)):
            hashSet = set()
            for colIdx in range(rowIdx, len(nums)):
                hashSet.add(nums[colIdx])
                ans += len(hashSet) ** 2

        return ans
