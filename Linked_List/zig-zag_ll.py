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
    def zig_zag(self):
        temp=self.head
        count=1
        while temp.next:
            if count==1 and temp.data>temp.next.data:
                swap = temp.data
                temp.data = temp.next.data
                temp.next.data = swap
            elif count==-1 and temp.data<temp.next.data:
                swap=temp.data
                temp.data=temp.next.data
                temp.next.data=swap
            count*=(-1)
            temp=temp.next
class Node:
    def __init__(self,n):
        self.data=n
        self.next=None

if __name__ == '__main__':
    ll1=LL()
    lst=input().split()
    #lst=list(map(int,input().split()))
    for i in lst:
        ll1.push(int(i))
    ll1.printll()
    ll1.zig_zag()
    ll1.printll()