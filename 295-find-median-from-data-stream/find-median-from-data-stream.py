from bisect import insort

class MedianFinder(object):

    def __init__(self):
        self.freq = [0] * 101

        # Outliers
        self.small = []   # numbers < 0, sorted
        self.large = []   # numbers > 100, sorted

        self.count = 0

    def addNum(self, num):
        self.count += 1

        if num < 0:
            insort(self.small, num)

        elif num > 100:
            insort(self.large, num)

        else:
            self.freq[num] += 1


    def getKth(self, k):
        # k is 1-indexed

        # Case 1: kth element is in small
        if k <= len(self.small):
            return self.small[k - 1]

        # Skip all elements < 0
        k -= len(self.small)

        # Case 2: kth element is in [0, 100]
        for num in range(101):
            if k <= self.freq[num]:
                return num

            k -= self.freq[num]

        # Case 3: kth element is in large
        return self.large[k - 1]


    def findMedian(self):

        if self.count % 2 == 1:
            k = self.count // 2 + 1
            return self.getKth(k)

        k1 = self.count // 2
        k2 = k1 + 1

        return (self.getKth(k1) + self.getKth(k2)) / 2.0
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()