class Solution(object):
    def countArrangement(self, n):
        count = [0]
        
        def permutation(idx, nums):
            if idx == len(nums):
                count[0] += 1
                return
                
            i = idx
            while i < len(nums):
                # 1. Swap to try a number at the current position
                nums[i], nums[idx] = nums[idx], nums[i]
                
                # 2. Correct 1-based positioning check (idx + 1)
                pos = idx
                if nums[idx] % pos == 0 or pos % nums[idx] == 0:
                    # Recurse only if it's a valid condition
                    permutation(idx + 1, nums)
                
                # 3. Always backtrack (unswap) before moving to the next iteration
                nums[i], nums[idx] = nums[idx], nums[i]
                i += 1
                
        nums = [i for i in range(0, n + 1)]
        permutation(1, nums)
        return count[0]

