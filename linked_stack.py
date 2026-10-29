class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedStack:
   
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def is_full(self):
        # A linked stack has no fixed capacity.
        return False

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow: cannot pop from an empty stack.")
        removed_item = self.top.data
        self.top = self.top.next
        return removed_item

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty: there is no top item.")
        return self.top.data

    def display(self):
        current = self.top
        values = []
        while current is not None:
            values.append(current.data)
            current = current.next
        print("Stack (top -> bottom):", values)
