class Solution(object):
    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        used = [False] * 1000
        totalDigits = len(digits)
        ans = 0

        for i in range(len(digits)):
            if digits[i] == 0:
                continue

            for j in range(len(digits)):
                if i == j:
                    continue

                for k in range(len(digits)):
                    if k == i or k == j or digits[k] % 2 != 0:
                        continue
                    
                    number = digits[i] * 100 + digits[j] * 10 + digits[k]
                    
                    if not used[number]:
                        used[number] = True
                        ans += 1

        return ans