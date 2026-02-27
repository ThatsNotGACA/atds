from atds import Node

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
    
if __name__ == "__main__":
    ul = UnorderedList()
    print("Is empty? " + str(ul.is_empty()))
    ul.add(10)
    ul.add(20)
    ul.add(30)
    print("After adding 10, 20, 30: " + str(ul))
    print("Length: " + str(ul.length()))
    print("Search 20: " + str(ul.search(20)))
    print("Search 99: " + str(ul.search(99)))
    ul.append(5)
    print("After append 5: " + str(ul))
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