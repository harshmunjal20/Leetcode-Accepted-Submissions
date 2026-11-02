class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        arr.sort()
        minDiff = 1e10
        ans = []

        for idx in range(len(arr) - 1):
            if minDiff > arr[idx + 1] - arr[idx]:
                ans.clear()
                minDiff = arr[idx + 1] - arr[idx]
                ans.append((arr[idx], arr[idx + 1]))
            elif minDiff == arr[idx + 1] - arr[idx]:
                ans.append((arr[idx], arr[idx + 1]))
        
        return ans