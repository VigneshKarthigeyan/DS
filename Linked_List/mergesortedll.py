class LL:
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
    def mergesorted(self,ll1,ll2):
        retll=Node(0)
        dummy=retll
        count=0
        while(True):
            if(ll1 is None):
                dummy.next=ll2
                break
            if(ll2 is None):
                dummy.next=ll1
                break
            if(ll1.data<=ll2.data):
                dummy.next=ll1
                ll1=ll1.next
            else:
                dummy.next=ll2
                ll2=ll2.next
            dummy=dummy.next
        return(retll.next)

    def recmersort(self,ll1,ll2):
        if ll1 is None:
            return ll2
        if ll2 is None:
            return ll1
        if ll1.data<=ll2.data:
            dummy=ll1
            dummy.next=self.recmersort(ll1.next,ll2)
        else:
            dummy=ll2
            dummy.next=self.recmersort(ll1,ll2.next)
        return dummy

class Node:
    def __init__(self,val):
        self.data=val
        self.next=None

if __name__ == '__main__':
    ll1=LL()
    ll2=LL()
    x=Node(2)
    y=Node(3)
    ll1.head=x
    ll2.head=y
    ll1.append(5)
    ll1.append(7)
    ll1.append(9)
    ll1.append(11)
    ll2.append(4)
    ll2.append(6)
    ll2.append(8)
    ll2.append(10)
    ll1.printll()
    ll2.printll()
    ll3=LL()
    ll3.head=LL().recmersort(ll1.head,ll2.head)
    ll3.printll()