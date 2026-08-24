class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minimumList = []

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        if self.minimumList:
            self.minimumList.append(min(value, self.minimumList[-1]))
        else:
            self.minimumList.append(value)
        self.stack.append(value)
        

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.minimumList.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minimumList[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()