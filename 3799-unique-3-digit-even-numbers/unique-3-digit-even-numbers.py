from collections import Counter

class Solution(object):
    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        used = set()
        freqMap = Counter(digits)
        count = 0

        for firstDigit in range(1, 10):
            if freqMap[firstDigit] == 0:
                continue

            freqMap[firstDigit] -= 1

            for secondDigit in range(0, 10):
                if freqMap[secondDigit] == 0:
                    continue
                
                freqMap[secondDigit] -= 1

                for thirdDigit in range(0, 10, 2):
                    if freqMap[thirdDigit] == 0:
                        continue

                    freqMap[thirdDigit] -= 1
                    number = firstDigit * 100 + secondDigit * 10 + thirdDigit
                    freqMap[thirdDigit] += 1
                    
                    if number in used:
                        continue

                    used.add(number)
                    count += 1
                
                freqMap[secondDigit] += 1

            freqMap[firstDigit] += 1

        return count
                    