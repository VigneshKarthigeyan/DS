class LL:
    def __init__(self):
        self.head=None

    def altsplit(self,cur):
        ll1=LL()
        ll2=LL()
        count=0
        while cur:
            if count%2==0:
                ll1.append(cur.data)
            else:
                ll2.append(cur.data)
            count+=1
            cur=cur.next
        return ll1,ll2
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
class Node:
    def __init__(self,val):
        self.data=val
        self.next=None

if __name__ == '__main__':
    ll1=LL()
    ll2,ll3=LL(),LL()
    n1=Node(5)
    ll1.head=n1
    ll1.append(25)
    ll1.append(55)
    ll1.append(75)
    ll1.append(85)
    ll1.append(95)
    ll1.printll()
    ll2,ll3=ll1.altsplit(ll1.head)
    ll2.printll()
    ll3.printll()