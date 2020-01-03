class LL:
    def __init__(self):
        self.head=None
    def push(self,v1,v2):
        n=Node(v1,v2)
        n.next=self.head
        self.head=n
    def add_poly(self,head1,head2):
        res=LL()
        while head1 and head2:
            data=head1.data+head2.data
            res.push(data,head1.xpow)
            head1=head1.next
            head2=head2.next
        return res.head
    def printll(self,head1):
        head=head1
        while head:
            print("%dx^%d"%(head.data,head.xpow),end=" ")
            if head.next:
                print("+",end=" ")
            head=head.next
        print()

class Node:
    def __init__(self,v1,v2):
        self.data=v1
        self.xpow=v2
        self.next=None
if __name__ == '__main__':
    ll1=LL()
    ll1.push(10,0)
    ll1.push(20,1)
    ll1.push(30,2)
    ll1.printll(ll1.head)
    ll2=LL()
    ll2.push(30,0)
    ll2.push(20,1)
    ll2.push(10,2)
    ll2.printll(ll2.head)
    add=LL().add_poly(ll1.head,ll2.head)
    LL().printll(add)
