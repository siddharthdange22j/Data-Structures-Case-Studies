# Case Study 4: Stack and Queue implemented with linked lists

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedStack:
    def __init__(self):
        self.top = None

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.top is None:
            return None
        value = self.top.data
        self.top = self.top.next
        return value

    def peek(self):
        return None if self.top is None else self.top.data

    def display(self):
        values, current = [], self.top
        while current:
            values.append(str(current.data))
            current = current.next
        return " -> ".join(values) if values else "(empty)"


class LinkedQueue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, value):
        node = Node(value)
        if self.rear is None:
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if self.front is None:
            return None
        value = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return value

    def peek(self):
        return None if self.front is None else self.front.data

    def display(self):
        values, current = [], self.front
        while current:
            values.append(str(current.data))
            current = current.next
        return " -> ".join(values) if values else "(empty)"


if __name__ == "__main__":
    print("STACK (LIFO)")
    stack = LinkedStack()
    for item in ["Book-A", "Book-B", "Book-C"]:
        stack.push(item)
        print("push:", item)
    print("Top ->", stack.display())
    print("peek:", stack.peek())
    print("pop:", stack.pop())
    print("After pop:", stack.display())

    print("\nQUEUE (FIFO)")
    queue = LinkedQueue()
    for item in ["Student-101", "Student-102", "Student-103"]:
        queue.enqueue(item)
        print("enqueue:", item)
    print("Front ->", queue.display())
    print("peek:", queue.peek())
    print("dequeue:", queue.dequeue())
    print("After dequeue:", queue.display())
