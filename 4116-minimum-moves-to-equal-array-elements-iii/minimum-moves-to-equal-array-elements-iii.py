class Solution:
    def minMoves(self, nums: List[int]) -> int:
        minMoves = 1e10

        for elem in nums:
            currMoves = 0
            flag = True

            for newElem in nums:
                if elem - newElem < 0:
                    flag = False
                    break
                currMoves += elem - newElem

            if not flag:
                continue
            minMoves = min(minMoves, currMoves)

        return minMoves