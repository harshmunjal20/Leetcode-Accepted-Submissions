import heapq
class MedianFinder(object):

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        # push into maxHeap , no matter what
        heapq.heappush(self.maxHeap, -num)

        # ensuring that top element in maxHeap is less than equal to minHeap top
        if self.minHeap and self.maxHeap and (-self.maxHeap[0] > self.minHeap[0]):
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        
        # maxHeap can have atmost 1 size more than minHeap
        if len(self.maxHeap) > len(self.minHeap) + 1:
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        elif len(self.minHeap) > len(self.maxHeap):
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))



    def findMedian(self):
        """
        :rtype: float
        """
        if (len(self.maxHeap) + len(self.minHeap)) % 2 == 1:
            return -self.maxHeap[0]
        
        return (self.minHeap[0] - self.maxHeap[0]) / 2.0
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()