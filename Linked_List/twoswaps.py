class LL:
    def __init__(self):
        self.head=None

    def swaptwos(self):
        first=self.head
        while first and first.next:
            suf=first.next
            x=first.data
            first.data=suf.data
            suf.data=x
            first=first.next.next


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
    ll1.append(85)
    ll1.append(95)
    ll1.printll()
    ll1.swaptwos()
    ll1.printll()