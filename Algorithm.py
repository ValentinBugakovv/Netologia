class Node:
    next = None
    # prev = None
    value = None

    def __init__(self, value):
        self.value = value


class List:
    head = None
    tail = None

    def append(self, value):
        node = Node(value)
        if self.head is None and self.tail is None:
            self.head = node
            self.tail = node
        else:
            # node.prev = self.tail
            self.tail.next = node
            self.tail = node

    def reverse(self):
        h = self.head
        t = self.tail

        cur = A.head
        cur_next = cur.next
        cur.next = None
        while cur_next is not None:
            next = cur_next.next
            cur_next.next = cur
            cur = cur_next
            cur_next = next

        self.head = t
        self.tail = h

    def print(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next


A = List()
A.append(25)
A.append(14)
A.append(35)
A.append(11)
A.print()
print(" ")
A.reverse()
A.print()

# T = O(n)
# M = O(1)
