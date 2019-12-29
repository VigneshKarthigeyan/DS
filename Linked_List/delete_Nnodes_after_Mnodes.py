#delete n_nodes after
# m nodes
class LL:
    def __init__(self):
        self.head=None
    def push(self,val):
        n=Node(val)
        n.next=self.head
        self.head=n
    def printl(self):
        temp=self.head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
        print()
    def delcon(self,n1,m):
        temp=self.head
        count=0
        while temp:
            count+=1
            if count==m:
                count=0
                tmp=temp
                n=n1
                while n!=0:
                    tmp=tmp.next
                    n-=1
                temp.next=tmp.next
            temp=temp.next

class Node:
    def __init__(self,val):
        self.data=val
        self.next=None

if __name__ == '__main__':
    ll1=LL()
    ll1.push(10)
    ll1.push(9)
    ll1.push(8)
    ll1.push(7)
    ll1.push(6)
    ll1.push(5)
    ll1.push(4)
    ll1.push(3)
    ll1.push(2)
    ll1.push(1)
    ll1.printl()
    ll1.delcon(2,3)
    ll1.printl()