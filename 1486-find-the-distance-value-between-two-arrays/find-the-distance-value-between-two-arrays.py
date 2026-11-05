class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        count = 0
        
        for num1 in arr1:
            flag = True

            for num2 in arr2:
                if abs(num1 - num2) <= d:
                    flag = False
                    break
            
            if flag:
                count += 1

        return count