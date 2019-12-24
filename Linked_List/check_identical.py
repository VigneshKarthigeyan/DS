class LL:
    def __init__(self):
        self.head=None

    def check_identical(self,head1,head2):
        while head1 and head2:
            if head1.data != head2.data:
                print("Not identical")
                return
            head1 = head1.next
            head2 = head2.next
        if head1 or head2:
            print("Not identical")
        else:
            print("identical")

    def rec(self,h1,h2):
        if h1.data!=h2.data:
            print("Not identical")
            return
        if h1.next and h2.next:
            self.rec(h1.next,h2.next)
        elif not(h1.next or h2.next):
            print("identical")
        else:
            print("not identical")

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
    ll1.append(10)
    ll1.append(20)
    ll1.append(30)
    ll1.append(40)
    ll1.append(50)
    ll2 = LL()
    ll2.append(10)
    ll2.append(20)
    ll2.append(30)
    ll2.append(40)
    ll2.append(50)
    LL().rec(ll1.head,ll2.head)
