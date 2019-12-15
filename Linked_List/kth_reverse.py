#reverse elements upto given counter value
class LL:
    def __init__(self):
        self.head=None
    def append(self,val):
        n=Node(val)
        temp=self.head
        while(temp.next is not None):
            temp=temp.next
        temp.next=n
    def printLL(self):
        temp=self.head
        while temp is not None:
            print(temp.data,end=' ')
            temp=temp.next
        print()
    def rev(self,head,val):
        prev=None
        cur=head
        count=0
        while(cur is not None) and (count<val):
            suf=cur.next
            cur.next=prev
            prev=cur
            cur=suf
            count+=1
        if suf is not None:
            head.next=self.rev(suf,val)
        return prev
class Node:
    def __init__(self,val):
        self.data=val
        self.next=None
if __name__ == '__main__':
    ll1 = LL()
    x = Node(2)
    ll1.head = x
    ll1.append(5)
    ll1.append(7)
    ll1.append(9)
    ll1.append(11)
    ll1.append(13)
    ll1.append(15)
    ll1.printLL()
    ll1.head=ll1.rev(ll1.head,3)
    ll1.printLL()
