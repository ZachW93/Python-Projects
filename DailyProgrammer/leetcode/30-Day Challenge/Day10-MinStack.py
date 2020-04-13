class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = ""
        

    def push(self, x: int) -> None:
        
        self.stack.append(x)
        

    def pop(self) -> None:
        
        popped_val = self.stack.pop(len(self.stack) - 1)

    def top(self) -> int:
        
        top_val = self.stack[len(self.stack) - 1]
        return top_val

    def getMin(self) -> int:

        sorted_stack = sorted(self.stack)
        return sorted_stack[0]
        
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()