class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __str__(self):
        return "Queue[" + ",".join(self.items) + "]"
    

class Deque:
    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        if not self.is_empty():
            return self.items.pop(0)

    def remove_rear(self):
        if not self.is_empty():
            return self.items.pop(-1)

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __str__(self):
        return "Deque[" + ",".join(self.items) + "]"

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next

if __name__ == "__main__":
    stack = Stack()
    print("Popping from empty stack:", stack.pop())
    print("Peeking at empty stack:", stack.peek())
    stack.push(10)
    stack.push(20)
    print("Top item:", stack.peek())
    print("Stack size:", stack.size())
    print("Popped item:", stack.pop()) 
    print("Is stack empty?", stack.is_empty())
    dq = Deque()
    dq.add_rear("a")
    dq.add_rear("b")
    dq.add_front("c")
    print(dq)
    print(dq.remove_front())
    print(dq.remove_rear())
    print(dq)
    node1 = Node(100)
    node2 = Node(200)
    print("Node1 data: " + str(node1.get_data()))
    print("Node1 next: " + str(node1.get_next()))
    node1.set_next(node2)
    print("After linking node1 to node2:")
    print("Node1 next data: " + str(node1.get_next().get_data()))
    node1.set_data(150)
    print("After changing node1 data: " + str(node1.get_data()))