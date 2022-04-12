from collections import deque


class StackList:
    def __init__(self):
        self.stack = list()
    def push(self,item):
        self.stack.append(item)
    def pop(self):
        if len(self.stack)>0:
          return self.stack.pop()
        else:
          return None
    def peek(self):
        if len(self.stack)>0:
            return self.stack[len(self.stack)-1]
        else:
            return None
    def __str__(self):
        return str(self.stack)

class StackDeque:
    def __init__(self):
        self.stack=deque()
        
    def push(self,item):
        self.stack.append(item)
        
    def pop(self):
        if(len(self.stack)>0):
            return self.stack.pop()
        else:
            return None
        
    def peek(self):
        if(len(self.stack)>0):
            return self.stack[len(self.stack)-1]
        else:
            return None
    
    def is_empty(self):
        if(len(self.stack)>0):
            return False
        else:
            return True
    
    def __str__(self) -> str:
        return str(self.stack)
    
    
    

if __name__ == '__main__':
    # Test
    stack=StackDeque()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.pop()

    print(stack.is_empty())
        
    

