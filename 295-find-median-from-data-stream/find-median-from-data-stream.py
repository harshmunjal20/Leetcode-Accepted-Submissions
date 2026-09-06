import heapq

class MedianFinder(object):

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.minHeap) >= len(self.maxHeap): # push into the maxHeap
            if not self.maxHeap or -self.maxHeap[0] >= num:
                heapq.heappush(self.maxHeap, -num)
            else:
                heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
                heapq.heappush(self.minHeap, num)
        else: # push into the minHeap
            if num >= -self.maxHeap[0]:
                heapq.heappush(self.minHeap, num)
            else:
                heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
                heapq.heappush(self.maxHeap, -num)


    def findMedian(self):
        """
        :rtype: float
        """
        if (len(self.minHeap) + len(self.maxHeap)) % 2 != 0:
            return min(-self.maxHeap[0] if self.maxHeap else 1e10, self.minHeap[0] if self.minHeap else 1e10)
        
        return (self.minHeap[0] - self.maxHeap[0]) / 2.00


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()