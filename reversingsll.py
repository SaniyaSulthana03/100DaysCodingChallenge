class Node:
    def __init__(self,val):
        self.val=val
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.root = None

    def addNode(self,val):
        n=Node(val)
        if self.root==None:
            self.root=n
            return
        temp=self.root
        while temp.next!=None:
            temp=temp.next
        temp.next=n

    def display(self):
        temp = self.root
        while temp:
            print(temp.val, end=" -> ")
            temp = temp.next
        print()

    def reverseDisplay(self,node):
        if node is None:
            return
        self.reverseDisplay(node.next)
        print(node.val,end=' -> ')

ssl=SingleLinkedList()
ssl.addNode(10)
ssl.addNode(20)
ssl.addNode(30)
ssl.display()
ssl.reverseDisplay(ssl.root)



