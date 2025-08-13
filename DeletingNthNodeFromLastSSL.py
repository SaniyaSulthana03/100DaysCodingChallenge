class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
    def deleteNthFromEnd(self, n):
        dummy = Node(0)
        dummy.next = self.head
        first = dummy
        second = dummy
        for _ in range(n + 1):
            if first:
                first = first.next
        while first:
            first = first.next
            second = second.next

        second.next = second.next.next
        self.head = dummy.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print()

ll = LinkedList()
for i in [1, 2, 3, 4, 5]:
    ll.insert(i)

print("Before deletion:")
ll.display()

ll.deleteNthFromEnd(2)

print("After deleting 2nd node from end:")
ll.display()
