#delete if right node is greather
#than left node
class LL:
    def __init__(self):
        self.head=None

    def delcondition(self):
        cur=self.head
        while cur and cur.next:
            suf=cur.next
            if cur.data<suf.data:
                self.dele(cur.data)
                cur=suf
            else:
                cur=cur.next
    def dele(self,val):
        temp=self.head
        prev=None
        if temp.data==val:
            self.head=temp.next
            return
        while temp is not None:
            if temp.data==val:
                prev.next=temp.next
                return
            prev=temp
            temp=temp.next
    def printll(self):
        if self.head is None:
            print("Empty ll")
            return
        temp=self.head
        while(temp!=None):
            print(temp.data,end=' ')
            temp=temp.next
        print()

    def append(self,val):
        n_node=Node(val)
        if self.head is None:
            self.head=n_node
        else:
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            temp.next=n_node
    def push(self,val):
        if self.head is None:
            self.head=Node(val)
        else:
            n1=Node(val)
            n1.next=self.head
            self.head=n1

class Node:
    def __init__(self,val):
        self.data=val
        self.next=None

if __name__ == '__main__':
    ll1=LL()
    ll1.append(12)
    ll1.append(15)
    ll1.append(10)
    ll1.append(9)
    ll1.append(5)
    ll1.append(8)
    ll1.printll()
    ll1.delcondition()
    ll1.printll()