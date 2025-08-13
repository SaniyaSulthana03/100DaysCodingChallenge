class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class SingleLinkedList:
    def __init__(self):
        self.root=None

    def AddNode(self,val):
        n=Node(val)
        if self.root==None:
            self.root=n
            return
        temp = self.root
        while temp.next != None:
            temp=temp.next
        temp.next=n

    def display(self):
        temp=self.root
        while temp:
            print(temp.val,'->')
            return
        print("SSL is empty")

    def middleNode(self):
        temp=self.root




ssl=SingleLinkedList()
ssl.AddNode(10)
ssl.AddNode(20)
ssl.AddNode(30)
ssl.AddNode(40)
ssl.AddNode(50)
ssl.display()
