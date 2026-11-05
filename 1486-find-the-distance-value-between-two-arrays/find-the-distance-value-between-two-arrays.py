class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        # |5 - x| <= d
        # 5 - d <= x <= d + 5
        arr2.sort()
        count = 0

        for elem in arr1:
            low = 0
            high = len(arr2) - 1

            while low <= high:
                mid = low + (high - low) // 2
                if elem - d <= arr2[mid] <= elem + d:
                    count += 1
                    break
                elif arr2[mid] < elem - d:
                    low = mid + 1
                elif arr2[mid] > elem + d:
                    high = mid - 1

        return len(arr1) - count