#Flatten a multilevel ll

class Node:
    def __init__(self,val):
        self.data=val
        self.next=None
        self.child=None

def printlist(head):
    while head:
        print(head.data,end=' ')
        head=head.next

def flat(head):
    tail=head
    while tail.next:
        tail=tail.next
    temp=head
    while temp!=tail:
        if temp.child:
            tail.next=temp.child
            tmp=temp.child
            while tmp.next:
                tmp=tmp.next
            tail=tmp
        temp=temp.next

if __name__ == '__main__':
    head=Node(10)
    head.child=Node(70)
    head.child.next=Node(80)
    head.child.next.child=Node(100)
    head.child.next.next=Node(90)
    head.child.next.next.child=Node(110)
    head.next=Node(20)
    head.next.next=Node(30)
    head.next.next.next=Node(40)
    head.next.next.next.next=Node(50)
    head.next.next.next.child=Node(120)
    flat(head)
    printlist(head)