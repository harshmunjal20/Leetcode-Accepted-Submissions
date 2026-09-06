class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
    
class LRUCache(object):
    def removeTailNode(self):
        toDeleteNode = self.tail.prev
        toDeletePrev = toDeleteNode.prev
        toDeletePrev.next = self.tail
        self.tail.prev = toDeletePrev
        key = toDeleteNode.key
        self.keyToNodeMap.pop(key)
        del toDeleteNode

    def detachNodeToHead(self, currNode):
        prevCurrNode = currNode.prev
        if prevCurrNode == self.head:
            return

        nextCurrNode = currNode.next
        prevCurrNode.next = nextCurrNode
        nextCurrNode.prev = prevCurrNode


        headNextNode = self.head.next
        self.head.next = currNode
        currNode.prev = self.head
        currNode.next = headNextNode
        headNextNode.prev = currNode

    def addNodeAtHead(self, currNode):
        headNextNode = self.head.next
        headNextNode.prev = currNode
        currNode.next = headNextNode
        currNode.prev = self.head

        self.head.next = currNode

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.capacity = capacity
        self.head.next = self.tail
        self.tail.prev = self.head
        self.keyToNodeMap = {}
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # head indicates the most recently used node
        if key not in self.keyToNodeMap:
            return -1

        currNode = self.keyToNodeMap[key]
        self.detachNodeToHead(currNode)
        return currNode.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.keyToNodeMap:
            currNode = self.keyToNodeMap[key]
            currNode.val = value
            self.detachNodeToHead(currNode)
        elif self.capacity > 0:
            currNode = Node(key, value)
            self.addNodeAtHead(currNode)
            self.capacity -= 1
            self.keyToNodeMap[key] = currNode
        else:
            currNode = Node(key, value)
            self.removeTailNode()
            self.addNodeAtHead(currNode)
            self.keyToNodeMap[key] = currNode



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)