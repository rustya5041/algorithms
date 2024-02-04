# basic implementation of Queue class in Python
# FIFO - first in, first out

class Queue():
    def __init__(self, max_len=50):
        self.queue = [0] * max_len 
        self.head = 0
        self.tail = 0
        self.max_len = max_len

    def enqueue(self, key):
        self.queue[self.tail] = key
        self.tail = (self.tail + 1) % self.max_len
    
    def dequeue(self):
        res = self.queue[self.head]
        self.head = (self.head + 1) % self.max_len
        return res
    
    def empty(self) -> None:
        return self.head == self.tail
    
    def __str__(self) -> str:
        i = self.head
        q = []
        while i < self.tail:
            q.append(self.queue[i])
            i = (i + 1) % self.max_len
        return str(q)
    
# if __name__ == '__main__':
#     q = Queue()
#     q.enqueue(2)
#     q.enqueue(3)
#     print(q)
#     q.dequeue()
#     print(q)

# implementation of Queue on two Stacks
class Queue2Stacks():
    def __init__(self) -> None:
        self.to_enqueue = []
        self.to_deque = []
    
    def enqueue(self, key):
        self.to_enqueue.append(key)

    def deque(self):
        for i in range(len(self.to_enqueue)-1):
            self.to_deque.append(self.to_enqueue.pop(i))
        return self.to_deque.pop()

if __name__ == '__main__':
    q = Queue2Stacks()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(5)
    print(q.deque())
    print(q.deque())
    print(q.enqueue(17))




        