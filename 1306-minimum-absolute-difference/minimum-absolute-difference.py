class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        arr.sort()
        minDiff = 1e10
        ans = []

        for idx in range(len(arr) - 1):
            minDiff = min(minDiff, abs(arr[idx] - arr[idx + 1]))
        
        for idx in range(len(arr) - 1):
            if abs(arr[idx] - arr[idx + 1]) == minDiff:
                ans.append((arr[idx], arr[idx + 1]))

        return ans