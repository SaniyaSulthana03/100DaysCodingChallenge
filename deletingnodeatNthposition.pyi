class Node:
    def _init_(self, data):
        self.data = data
        self.next = None

def delete_at_pos(head, pos):
    if pos == 0:
        return head.next
    temp = head
    for _ in range(pos - 1):
        temp = temp.next
        if temp is None:
            return head
    if temp.next:
        temp.next = temp.next.next
    return head

def display(head):
    curr = head
    while curr:
        print(curr.data, end=" -> ")
        curr = curr.next
    print("None")

# Example usage
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

display(head)