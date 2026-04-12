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

class UnorderedList(object):
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        new_node = Node(item)
        new_node.set_next(self.head)
        self.head = new_node

    def length(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def search(self, item):
        current = self.head
        while current is not None:
            if current.get_data() == item:
                return True
            current = current.get_next()
        return False

    def remove(self, item):
        current = self.head
        previous = None
        while current is not None:
            if current.get_data() == item:
                if previous is None:
                    self.head = current.get_next()
                else:
                    previous.set_next(current.get_next())
                return
            previous = current
            current = current.get_next()

    def append(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.get_next() is not None:
            current = current.get_next()
        current.set_next(new_node)

    def index(self, item):
        current = self.head
        position = 0
        while current is not None:
            if current.get_data() == item:
                return position
            current = current.get_next()
            position += 1

    def insert(self, pos, item):
        new_node = Node(item)
        if pos == 0:
            new_node.set_next(self.head)
            self.head = new_node
            return
        current = self.head
        previous = None
        count = 0
        while count < pos:
            previous = current
            current = current.get_next()
            count += 1
        previous.set_next(new_node)
        new_node.set_next(current)

    def pop(self, pos=None):
        if self.head is None:
            return None
        if pos is None:
            pos = self.length() - 1
        current = self.head
        previous = None
        count = 0
        while count < pos:
            previous = current
            current = current.get_next()
            count += 1
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
        return current.get_data()

    def __repr__(self):
        result = "UnorderedList["
        next_node = self.head
        while next_node is not None:
            result += str(next_node.get_data()) + ","
            next_node = next_node.get_next()
        result += "]"
        return result
    
class UnorderedListStack:
    def __init__(self):
        self.items = UnorderedList()

    def push(self, item):
        self.items.add(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self.items.head.get_data()

    def size(self):
        return self.items.length()

    def is_empty(self):
        return self.items.is_empty()

class HashTable:
    def __init__(self, size):
        self.size = size
        self.slots = [None] * size
        self.data = [None] * size

    def __repr__(self):
        result = "Slots: " + str(self.slots) + "\n"
        result = result + "Data:  " + str(self.data)
        return result

    def hash_function(self, key):
        return key % self.size

    def put(self, key, value):
        hash_value = self.hash_function(key)

        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = value
        elif self.slots[hash_value] == key:
            self.data[hash_value] = value
        else:
            next_slot = (hash_value + 1) % self.size

            while self.slots[next_slot] is not None and self.slots[next_slot] != key:
                next_slot = (next_slot + 1) % self.size

                if next_slot == hash_value:
                    print("Hash table is full.")
                    return

            if self.slots[next_slot] is None:
                self.slots[next_slot] = key
                self.data[next_slot] = value
            else:
                self.data[next_slot] = value

    def get(self, key):
        start_slot = self.hash_function(key)
        position = start_slot

        while self.slots[position] is not None:
            if self.slots[position] == key:
                return self.data[position]

            position = (position + 1) % self.size

            if position == start_slot:
                return None

        return None
    
class BinaryTree:
    def binary_tree(val):
        return [val, [], []]

    def get_root_val(root):
        return root[0]

    def set_root_val(root, new_val):
        root[0] = new_val

    def get_left_child(root):
        return root[1]

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
    ul = UnorderedList()
    print("Is list empty? " + str(ul.is_empty()))
    ul.add(10)
    ul.add(20)
    ul.add(30)
    print("After adding 10, 20, 30: " + str(ul))
    print("List length: " + str(ul.length()))
    print("Search 20: " + str(ul.search(20)))
    ul.append(5)
    print("After appending 5: " + str(ul))
    print("Index of 20: " + str(ul.index(20)))
    ul.insert(2, 99)
    print("After inserting 99 at position 2: " + str(ul))
    ul.remove(20)
    print("After removing 20: " + str(ul))
    print("Pop last: " + str(ul.pop()))
    print("After popping last: " + str(ul))
    print("Pop position 1: " + str(ul.pop(1)))
    print("After popping position 1: " + str(ul))
    print("Final length: " + str(ul.length()))