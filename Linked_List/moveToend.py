#Remove all occurences of
# key to end of ll
class LL:
    def __init__(self):
        self.head=None

    def printll(self):
        temp=self.head
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
    def movetoend(self,val):
        lst=[]
        temp=self.head
        prev=None
        while temp:
            if temp.data==val:
                lst.append(val)
                prev.next=temp.next
            else:
                prev=temp
            tail=temp
            temp=temp.next
        for i in lst:
            self.append(tail,i)


class Node:
    def __init__(self,val):
        self.data=val
        self.next=None

if __name__ == '__main__':
    ll1=LL()
    ll1.head=Node(10)
    ll1.append(ll1.head,20)
    ll1.append(ll1.head,20)
    ll1.append(ll1.head,20)
    ll1.append(ll1.head,40)
    ll1.append(ll1.head,30)
    ll1.append(ll1.head,50)
    ll1.printll()
    ll1.movetoend(20)
    ll1.printll()
