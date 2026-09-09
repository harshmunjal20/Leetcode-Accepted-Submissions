class Solution(object):
    mx = int(5e6 + 1)

    primes = [True] * mx
    primes[0], primes[1] = False, False
    num = 2

    while num * num < mx:
        if primes[num]:
            currNum = num * num

            while currNum < mx:
                primes[currNum] = False
                currNum += num

        num += 1

    prefixSumArr = []
    currSum = 0

    for isPrimeNum in primes:
        if isPrimeNum:
            currSum += 1
        
        prefixSumArr.append(currSum)

        
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0

        return self.prefixSumArr[n - 1]