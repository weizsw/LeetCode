class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minS = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.minS) == 0:
            self.minS.append(x)
        else:
            last_min = self.minS[-1]
            if x <= last_min:
                self.minS.append(x)
        self.stack.append(x)

    def pop(self):
        """
        :rtype: None
        """
        if len(self.stack) > 0 and self.stack.pop() == self.minS[-1]:
            self.minS.pop()
    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """

        return self.minS[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()