# a < b > c < d > e < f ..
class LL:
    def __init__(self):
        self.head=None
    def push(self,v):
        n=Node(v)
        n.next=self.head
        self.head=n
    def printll(self):
        temp=self.head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
        print()
    def parb(self):
        temp=self.head
        while temp and temp.next1:
            print(temp.data,"=",temp.next1.data)
            temp=temp.next
        print()
    def arbto_greatest(self):
        self.reverse()
        temp=self.head.next
        max=self.head
        while temp:
            temp.next1=max
            if temp.data>max.data:
                max=temp

            temp=temp.next
        self.reverse()

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
    def __init__(self,n):
        self.data=n
        self.next=None
        self.next1=None

if __name__ == '__main__':
    ll1=LL()
    ll1.push(3)
    ll1.push(2)
    ll1.push(10)
    ll1.push(5)
    ll1.printll()
    ll1.parb()
    ll1.arbto_greatest()
    ll1.parb()