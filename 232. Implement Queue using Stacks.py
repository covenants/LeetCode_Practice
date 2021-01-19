class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        #print('content of stack ', self.stack)
        if not self.empty():
            return self.stack.pop(0)
        else:
            return None
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        #print('content of stack is ', self.stack, len(self.stack))
        if not self.empty():
            #print('1 got executed')
            return self.stack[0]
        else:
            #print(len(self.stack) == 0)
            #print('2 got executed')
            return None 
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if len(self.stack) == 0:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
