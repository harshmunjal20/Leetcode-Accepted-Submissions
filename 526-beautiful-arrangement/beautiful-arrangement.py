class Solution(object):
    def countArrangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = [0]

        def permutation(idx, nums):
            if idx == len(nums):
                count[0] += 1
                return

            i = idx

            while i < len(nums):
                nums[i], nums[idx] = nums[idx], nums[i]
                if idx % nums[idx] == 0 or nums[idx] % idx == 0:
                    permutation(idx + 1, nums)
                nums[i], nums[idx] = nums[idx], nums[i]

                i += 1

        nums = [i for i in range(0, n + 1)]
        permutation(1, nums)
        return count[0]
        