class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = len(nums) - 2

        while idx >= 0:
            if nums[idx] < nums[idx + 1]:
                tempIdx = idx + 1

                while tempIdx < len(nums) and nums[idx] < nums[tempIdx]:
                    tempIdx += 1

                nums[tempIdx - 1] , nums[idx] = nums[idx], nums[tempIdx - 1]
                break

            idx -= 1

        nums[idx + 1: len(nums)] = nums[idx + 1 : len(nums)][::-1]
        