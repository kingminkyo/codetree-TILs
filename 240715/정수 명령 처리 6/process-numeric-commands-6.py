import heapq

class PriorityQueue:
    def __init__(self):
        self.items = []

    def push(self, item):
        heapq.heappush(self.items, -item)

    def empty(self):
        return not self.items
    
    def size(self):
        return len(self.items)
    
    def pop(self):
        if self.empty():
            raise Exception("q is empty")
        
        return -heapq.heappop(self.items)
    
    def top(self):
        if self.empty():
            raise Exception("q is empty")
        
        return -self.items[0]

n = int(input())
hq = PriorityQueue()

for _ in range(n):
    command = input()

    if command.startswith("push"):
        _, num = command.split()
        num = int(num)
        hq.push(num)
    
    elif command.startswith("size"):
        print(hq.size())

    elif command.startswith("empty"):
        print(1 if hq.empty() else 0)

    elif command.startswith("pop"):
        print(hq.pop())

    elif command.startswith("top"):
        print(hq.top())