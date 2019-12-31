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

    def lastoccurence_del(self,n):
        temp=self.head
        occured=None
        while temp:
            if temp.data==n:
                occured=temp
            temp=temp.next
        if occured and occured.next:
            occured.data=occured.next.data
            occured.next=occured.next.next
        if not occured.next:
            temp=self.head
            while temp.next is not occured:
                temp=temp.next
            temp.next=None


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
    ll1.append(25)
    ll1.append(75)
    ll1.printll()
    ll1.lastoccurence_del(75)
    ll1.printll()
