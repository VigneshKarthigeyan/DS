class LL:
    def __init__(self):
        self.head=None

    def printll(self):
        temp=self.head
        while(temp!=None):
            print(temp.data,end=' ')
            temp=temp.next
        print()

    def append(self,val):
        n_node=Node(val)
        temp=self.head
        while(temp.next!=None):
            temp=temp.next
        temp.next=n_node

    def reverse(self):
        prev=None
        cur=self.head

        while cur!=None:
            suf = cur.next
            cur.next=prev
            prev=cur
            cur=suf
        self.head=prev

class Node:
    def __init__(self,val):
        self.data=val
        self.next=None

if __name__ == '__main__':
    ll1=LL()
    n1=Node(5)
    ll1.head=n1
    ll1.append(25)
    ll1.append(55)
    ll1.append(75)
    print("Actual Linked list:",end="")
    ll1.printll()
    ll1.reverse()
    print("Reversed Linked list:", end="")
    ll1.printll()
