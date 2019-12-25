class LL:
    def __init__(self):
        self.head=None
    def push(self,head,val):
        n1=Node(val)
        n1.down=head
        head=n1
        return head
    def printll(self):
        temp=self.head
        while(temp is not None):
            print(temp.data,end=" ")
            temp=temp.down
        print()
    def merge(self,first,sec):

        if first==None:
            return sec
        if sec==None:
            return first
        join=None
        if first.data>sec.data:
            join=first
            join.down=self.merge(first.down,sec)
        else:
            join=sec
            join.down=self.merge(first,sec.down)
        return join
    def flatten(self,head):
        if head==None or head.right==None:
            return head
        head.right=self.flatten(head.right)
        head=self.merge(head,head.right)
        return head
class Node:
    def __init__(self,val):
        self.data=val
        self.right=None
        self.down=None

if __name__ == '__main__':
    ll1=LL()
    ll1.head=ll1.push(ll1.head,10)
    ll1.head =ll1.push(ll1.head,20)
    ll1.head =ll1.push(ll1.head,30)
    ll1.head =ll1.push(ll1.head,40)
    print(ll1.head.data)
    ll1.head.right=ll1.push(ll1.head.right,15)
    ll1.head.right=ll1.push(ll1.head.right,60)
    ll1.head.right.right=ll1.push(ll1.head.right.right,70)
    ll1.head.right.right=ll1.push(ll1.head.right.right,80)
    ll1.head.right.right=ll1.push(ll1.head.right.right,90)
    ll1.head=ll1.flatten(ll1.head)
    ll1.printll()