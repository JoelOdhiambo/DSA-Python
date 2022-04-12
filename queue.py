from collections import deque

class QueueDeque:
    def __init__(self):
        self.queue=deque()
    
    def enqueue(self,item):
        self.queue.append(item)
        
    def dequeue(self):
        if(len(self.queue)>0):
            self.queue.popleft()
        else: 
            return None
        
    def front(self):
        if(len(self.queue)>0):
            return self.queue[0]
        else:
            return None
    
    def rear(self):
        if(len(self.queue)>0):
            return self.queue[len(self.queue)-1]
        else:
            return None
        
    def __str__(self) -> str:
        return str(self.queue)
         

if __name__ == '__main__':
    # Test
    queue=QueueDeque()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.dequeue()
    print(queue.__str__())