class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # currently treating answer as suffix
        answer = [1] * (len(nums) + 1)

        for idx in range(len(nums) - 1, -1, -1):
            answer[idx] = answer[idx + 1] * nums[idx]
        
        prefixProd = 1

        for idx in range(len(nums)):
            answer[idx] = answer[idx + 1] * prefixProd
            prefixProd *= nums[idx]

        answer.pop()
        return answer