class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedQueue:
    
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def is_full(self):
        # A linked queue has no fixed capacity.
        return False

    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue underflow: cannot dequeue from an empty queue.")
        removed_item = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return removed_item

    def peek_front(self):
        if self.is_empty():
            raise IndexError("Queue is empty: there is no front item.")
        return self.head.data

    def display(self):
        current = self.head
        values = []
        while current is not None:
            values.append(current.data)
            current = current.next
        print("Queue (front -> rear):", values)
