class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        sortedArr = copy.deepcopy(arr)
        sortedArr.sort()
        sortedArr.append(1e10)
        hashMap = {}
        rank = 1

        for idx in range(len(sortedArr) - 1):
            if sortedArr[idx] != sortedArr[idx + 1]:
                hashMap[sortedArr[idx]] = rank
                rank += 1
        

        for idx in range(len(arr)):
            arr[idx] = hashMap[arr[idx]]

        return arr