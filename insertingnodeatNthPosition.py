class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data, pos):
        new_node = Node(data)
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            return
        temp = self.head
        for _ in range(pos - 2):
            if not temp:
                return
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node

    def delete_at_pos(self, pos):
        if not self.head:
            return
        if pos == 1:
            self.head = self.head.next
            return
        temp = self.head
        for _ in range(pos - 2):
            if not temp.next:
                return
            temp = temp.next
        if temp.next:
            temp.next = temp.next.next

    def display(self):
        t = self.head
        while t:
            print(t.data, end=" -> ")
            t = t.next

ll = MyLinkedList()
ll.insert(10, 1)
ll.insert(20, 2)
ll.insert(15, 2)
ll.delete_at_pos(2)
ll.display()
