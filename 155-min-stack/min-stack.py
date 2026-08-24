class MinStack(object):

    def __init__(self):
        self.stack = []
        self.currMin = None

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        if not self.stack:
            self.stack.append(value)
            self.currMin = value
        elif value < self.currMin:
            self.stack.append(2 * value - self.currMin)
            self.currMin = value
        else:
            self.stack.append(value)

    def pop(self):
        """
        :rtype: None
        """
        if self.stack[-1] < self.currMin:
            self.currMin = 2 * self.currMin - self.stack[-1]
        self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        if self.stack[-1] < self.currMin:
            return self.currMin
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.currMin
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()