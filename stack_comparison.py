"""
Stack Comparison Analysis

This program compares the performance of two stack implementations:
1) Stack (list-based)
2) UnorderedListStack (built on the UnorderedList linked list)

We measure the time for a large number of push() and pop() operations
using Python's time module.

Expected results:
- The list-based Stack is faster because Python lists are optimized. 
    Append() and pop() at the end are very fast.
- The UnorderedListStack is slower because each operation requires
    creating Node objects and adjusting pointers.

This shows that even if two implementations have the same conceptual
efficiency (constant-time stack operations), practical performance can differ.
"""

import time
from atds import Stack, UnorderedList, Node

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

def test_push(stack_class, n):
    stack = stack_class()
    start = time.time()
    for i in range(n):
        stack.push(i)
    end = time.time()
    return end - start


def test_pop(stack_class, n):
    stack = stack_class()
    for i in range(n):
        stack.push(i)
    start = time.time()
    for i in range(n):
        stack.pop()
    end = time.time()
    return end - start

def main():
    sizes = [1000, 10000, 50000, 100000]

    print("STACK PERFORMANCE COMPARISON")

    for n in sizes:
        print("Testing with " + str(n) + " operations")

        list_push = test_push(Stack, n)
        linked_push = test_push(UnorderedListStack, n)

        print("Push Operations:")
        print("List-based Stack: " + str(round(list_push, 6)) + " seconds")
        print("UnorderedListStack: " + str(round(linked_push, 6)) + " seconds")

        list_pop = test_pop(Stack, n)
        linked_pop = test_pop(UnorderedListStack, n)

        print("Pop Operations:")
        print("List-based Stack: " + str(round(list_pop, 6)) + " seconds")
        print("UnorderedListStack: " + str(round(linked_pop, 6)) + " seconds")
        print()

if __name__ == "__main__":
    main()