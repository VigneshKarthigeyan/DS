#1-2-3-4 and 5-6-7 to 1-5-2-6-3-7-4
class LL:
    def __init__(self):
        self.head=None

    def printll(self):
        temp=self.head
        while(temp!=None):
            print(temp.data,end=' ')
            temp=temp.next
        print()
    def printl(self,head):
        if head==None:
            print("None")
        temp=head
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
    def merge_alternatively(self,head1,head2):
        l1=head1
        l2=head2
        while head1 and head2:
            next1=head1.next
            next2=head2.next
            head1.next=head2
            head2.next=next1

            head1=next1
            head2=next2
        l2 = head2
        self.printl(l1)

        self.printl(l2)


class Node:
    def __init__(self,val):
        self.data=val
        self.next=None
if __name__ == '__main__':
    ll1,ll2=LL(),LL()
    ll1.head=Node(1)
    ll1.append(2)
    ll1.append(3)
    ll2.head=Node(5)
    ll2.append(6)
    ll2.append(10)
    ll2.append(15)
    ll2.append(16)
    ll1.printll()
    ll2.printll()
    print("After modification:")
    LL().merge_alternatively(ll1.head,ll2.head)