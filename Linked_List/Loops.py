#Detection and removal of loops
#in a linked list
class LL:
    def __init__(self):
        self.head=None

    def detection(self,head):
        slow=fast=head
        while(slow and fast and fast.next):
            slow=slow.next
            fast=fast.next.next
            if(slow==fast):
                self.removal(slow)
                return 1
        return 0
    def removal(self,joint):
        ptr1=self.head

        while(True):
            ptr2 = joint
            while(ptr2.next is not ptr1) and (ptr2.next is not joint):
                ptr2=ptr2.next
            if(ptr2.next==ptr1):
                break
            ptr1=ptr1.next
        ptr2.next = None
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

class Node:
    def __init__(self,val):
        self.data=val
        self.next=None
if __name__ == '__main__':
    ll1=LL()
    n1=Node(10)
    ll1.head=n1
    ll1.append(5)
    ll1.append(15)
    ll1.append(25)
    ll1.append(35)
    ll1.printll()
    ll1.head.next.next.next.next.next=ll1.head.next.next
    ll1.detection(ll1.head)
    ll1.printll()

