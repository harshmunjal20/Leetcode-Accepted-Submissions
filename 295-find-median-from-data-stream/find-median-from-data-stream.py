import heapq

class MedianFinder(object):
    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.max_heap) <= len(self.min_heap): # push in maxHeap the num
            if not self.max_heap or (self.max_heap and -self.max_heap[0] >= num):
                heapq.heappush(self.max_heap, -num)
            elif self.min_heap:
                heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
                heapq.heappush(self.min_heap, num)
        else: # push in min_heap the num
            if (self.max_heap and -self.max_heap[0] <= num):
                heapq.heappush(self.min_heap, num)
            elif self.max_heap:
                heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
                heapq.heappush(self.max_heap, -num)

    def findMedian(self):
        """
        :rtype: float
        """
        if (len(self.min_heap) + len(self.max_heap)) % 2 == 0:
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0
        return min(-self.max_heap[0] if self.max_heap else 1e9, self.min_heap[0] if self.min_heap else 1e9)



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()