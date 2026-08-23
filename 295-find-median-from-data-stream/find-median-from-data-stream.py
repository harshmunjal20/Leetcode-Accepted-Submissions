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
        if len(self.min_heap) >= len(self.max_heap): # push it in the maxHeap
            if not self.max_heap or num < -self.max_heap[0]:
                heapq.heappush(self.max_heap, -num)
            else:
                # minHeap to maxHeap transfer
                heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
                heapq.heappush(self.min_heap, num)
        else: # push it in the minHeap
            if num >= -self.max_heap[0]:
                heapq.heappush(self.min_heap, num)
            else:
                # tranfer top of maxheap to minheap and num to maxheap
                heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
                heapq.heappush(self.max_heap, -num)
        

    def findMedian(self):
        """
        :rtype: float
        """
        if (len(self.min_heap) + len(self.max_heap)) % 2 == 0:
            return (self.min_heap[0] - self.max_heap[0]) / 2.0
        return min(-self.max_heap[0] if self.max_heap else 1e9, self.min_heap[0] if self.min_heap else 1e9)
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()