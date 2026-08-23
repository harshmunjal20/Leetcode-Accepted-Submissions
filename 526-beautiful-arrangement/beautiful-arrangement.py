class Solution(object):
    def countArrangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = [0]
        def permutation(index, nums):
            if index == len(nums):
                count[0] += 1
                return

            i = index

            while i < len(nums):
                nums[i], nums[index] = nums[index], nums[i]
                if nums[index] % index == 0 or index % nums[index] == 0:
                    permutation(index + 1, nums)
                nums[i], nums[index] = nums[index], nums[i]
                i += 1

        nums = [i for i in range(0, n + 1)]
        permutation(1, nums)

        return count[0]