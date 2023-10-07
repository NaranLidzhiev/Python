class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def is_empty(self):
        return self.first is None

    def push_back(self, val):
        p = Node(val)
        if self.is_empty():
            self.first = p
            self.last = p
            return
        self.last.next = p
        self.last = p

    def print_list(self):
        if self.is_empty():
            return
        p = self.first
        while p:
            print(p.val, end=" ")
            p = p.next
        print()

    def reverse_list(self):
        if self.is_empty() or self.first.next is None:
            return

        prev = None
        current = self.first
        next_node = None

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.first.next = prev

if __name__ == "__main__":
    l = LinkedList()
    for i in range(1, 6):
        l.push_back(str(i))

    l.print_list()
    l.reverse_list()
    l.print_list()
