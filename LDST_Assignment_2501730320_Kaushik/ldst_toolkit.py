# Linear Data Structures Toolkit (LDST)


# Dynamic Array
class DynamicArray:
    def __init__(self):
        self.capacity = 2
        self.size = 0
        self.data = [None] * self.capacity

    def append(self, x):
        if self.size == self.capacity:
            self._resize()

        self.data[self.size] = x
        self.size += 1

    def _resize(self):
        self.capacity *= 2
        new_data = [None] * self.capacity
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data
        print(f"Resized to {self.capacity}")

    def pop(self):
        if self.size == 0:
            print("Array is empty")
            return None
        val = self.data[self.size - 1]
        self.size -= 1
        return val

    def __str__(self):
        return str([self.data[i] for i in range(self.size)])


# Singly Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, x):
        new_node = Node(x)
        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete_by_value(self, x):
        temp = self.head
        if temp and temp.data == x:
            self.head = temp.next
            return

        prev = None
        while temp:
            if temp.data == x:
                prev.next = temp.next
                return
            prev = temp
            temp = temp.next

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# Doubly Linked List
class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_after(self, target, x):
        temp = self.head
        while temp:
            if temp.data == target:
                new_node = DNode(x)
                new_node.next = temp.next
                new_node.prev = temp

                if temp.next:
                    temp.next.prev = new_node
                temp.next = new_node
                return
            temp = temp.next

    def delete_at_position(self, pos):
        if not self.head:
            return

        temp = self.head

        if pos == 0:
            self.head = temp.next
            if self.head:
                self.head.prev = None
            return

        for _ in range(pos):
            if not temp:
                return
            temp = temp.next

        if temp:
            if temp.prev:
                temp.prev.next = temp.next
            if temp.next:
                temp.next.prev = temp.prev


# Stack (using SLL)
class Stack:
    def __init__(self):
        self.head = None

    def push(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if not self.head:
            return None
        val = self.head.data
        self.head = self.head.next
        return val

    def peek(self):
        if not self.head:
            return None
        return self.head.data


# Queue (using SLL)
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, x):
        new_node = Node(x)
        if not self.tail:
            self.head = self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        if not self.head:
            return None
        val = self.head.data
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return val

    def front(self):
        if not self.head:
            return None
        return self.head.data


# Parentheses Checker
def is_balanced(expr):
    stack = Stack()
    pairs = {')': '(', '}': '{', ']': '['}

    for ch in expr:
        if ch in "({[":
            stack.push(ch)
        elif ch in ")}]":
            if stack.pop() != pairs[ch]:
                return False

    return stack.peek() is None


# MAIN (Testing)
def main():
    print("=== Dynamic Array ===")
    arr = DynamicArray()
    for i in range(10):
        arr.append(i)
    print(arr)
    arr.pop()
    arr.pop()
    arr.pop()
    print(arr)

    print("\n=== Singly Linked List ===")
    sll = SinglyLinkedList()
    sll.insert_at_beginning(3)
    sll.insert_at_end(5)
    sll.insert_at_end(7)
    sll.traverse()
    sll.delete_by_value(5)
    sll.traverse()

    print("\n=== Stack ===")
    st = Stack()
    st.push(1)
    st.push(2)
    print(st.pop(), st.peek())

    print("\n=== Queue ===")
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    print(q.dequeue(), q.front())

    print("\n=== Parentheses Checker ===")
    print("([]):", is_balanced("([])"))
    print("([)]:", is_balanced("([)]"))


if __name__ == "__main__":
    main()