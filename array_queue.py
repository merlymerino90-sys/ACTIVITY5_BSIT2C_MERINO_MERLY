class ArrayQueue:
    def __init__(self, capacity=5):
        if capacity <= 0:
            raise ValueError("Capacity must be greater than zero.")
        self.capacity = capacity
        self.data = [None] * capacity
        self.front = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, item):
        if self.is_full():
            raise OverflowError("Queue overflow: the queue is full.")
        rear = (self.front + self.size) % self.capacity
        self.data[rear] = item
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue underflow: cannot dequeue from an empty queue.")
        removed_item = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1

        if self.size == 0:
            self.front = 0

        return removed_item

    def peek_front(self):
        if self.is_empty():
            raise IndexError("Queue is empty: there is no front item.")
        return self.data[self.front]

    def display(self):
        queue_items = []
        for index in range(self.size):
            queue_items.append(self.data[(self.front + index) % self.capacity])
        print("Queue (front -> rear):", queue_items)
        print("Array storage:", self.data)
