#Remove all dup occurences in a ll
class LL:
    def __init__(self):
        self.head=None

    def printll(self,head):
        temp=head
        while(temp!=None):
            print(temp.data,end=' ')
            temp=temp.next
        print()
    def append(self,head,val):
        n_node=Node(val)
        temp=head
        while(temp.next!=None):
            temp=temp.next
        temp.next=n_node
    def remove_dup(self,head):
        cur=head
        prev=Node(0)
        ret=prev
        prev.next=cur
        while cur and cur.next:

            if cur and cur.next and cur.data==cur.next.data:
                while cur.data==cur.next.data:
                    cur=cur.next
                cur=cur.next
                prev.next=cur
            else:
                prev=prev.next
                cur=cur.next
        self.printll(ret.next)


class Node:
    def __init__(self,val):
        self.data=val
        self.next=None

if __name__ == '__main__':
    ll1=LL()
    ll1.head=Node(10)
    ll1.append(ll1.head,20)
    ll1.append(ll1.head,20)
    ll1.append(ll1.head,40)
    ll1.append(ll1.head,40)
    ll1.append(ll1.head,30)
    ll1.append(ll1.head,50)
    ll1.printll(ll1.head)
    ll1.remove_dup(ll1.head)
