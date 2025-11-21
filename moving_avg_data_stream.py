class MovingAverage:
    from collections import deque

    def __init__(self, size: int):
        self.queue = deque()
        self.size = size
        self.count = 0
        self.window_sum = 0

    def next(self, val: int) -> float:
        self.count += 1
        self.queue.append(val)
        
        if self.count > self.size:
            remove = self.queue.popleft()
            self.window_sum += val
            self.window_sum -= remove
            
        else:
            self.window_sum += val
            
        return self.window_sum/len(self.queue)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)