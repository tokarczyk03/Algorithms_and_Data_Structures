class Node:
    def __init__(self, max_size):
        self.data = [None] * max_size
        self.max_size = max_size
        self.size = 0
        self.next = None

class UnrolledLinkedList:
    def __init__(self, node_size):
        self.head = None
        self.node_size = node_size

    def insert(self, index, value):
        if not self.head:
            self.head = Node(self.node_size)
            self.head.data[0] = value
            self.head.size += 1
            return

        cur = self.head
        prev = None
        while cur:
            if index <= cur.size:
                if cur.size < self.node_size:
                    for i in range(cur.size, index, -1):
                        cur.data[i] = cur.data[i-1]
                    cur.data[index] = value
                    cur.size += 1
                else:
                    new_node = Node(self.node_size)
                    new_node.next = cur.next
                    cur.next = new_node
                    for i in range(self.node_size//2, self.node_size):
                        new_node.data[i-self.node_size//2] = cur.data[i]
                        cur.data[i] = None
                    cur.size = new_node.size = self.node_size // 2
                    if index <= cur.size:
                        self.insert(index, value)
                    else:
                        self.insert(index-cur.size, value)
                return
            index -= cur.size
            prev = cur
            cur = cur.next

        if prev.size < self.node_size:
            prev.data[prev.size] = value
            prev.size += 1
        else:
            new_node = Node(self.node_size)
            new_node.data[0] = value
            new_node.size = 1
            prev.next = new_node

    def get(self, index):
        cur = self.head
        while cur:
            if index < cur.size:
                return cur.data[index]
            index -= cur.size
            cur = cur.next
        raise IndexError('List index out of range')

    def delete(self, index):
        cur = self.head
        while cur:
            if index < cur.size:
                for i in range(index, cur.size-1):
                    cur.data[i] = cur.data[i+1]
                cur.data[cur.size-1] = None
                cur.size -= 1
                if cur.size < self.node_size // 2 and cur.next:
                    for i in range(cur.next.size):
                        cur.data[cur.size+i] = cur.next.data[i]
                    cur.size += cur.next.size
                    cur.next = cur.next.next
                return
            index -= cur.size
            cur = cur.next
        raise IndexError('List index out of range')

    def print_list(self):
        cur = self.head
        while cur:
            for i in range(cur.size):
                print(cur.data[i], end=' ')
            cur = cur.next
        print()

# Testowanie listy
list = UnrolledLinkedList(6)
for i in range(1, 10):
    list.insert(i-1, i)
print(list.get(4))
list.insert(1, 10)
list.insert(8, 11)
list.print_list()
list.delete(1)
list.delete(2)
list.print_list()
