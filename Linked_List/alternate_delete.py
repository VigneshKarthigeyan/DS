class LL:
    def __init__(self):
        self.head=None

    def printll(self):
        temp=self.head
        while(temp!=None):
            print(temp.data,end=' ')
            temp=temp.next
        print()

    def push(self,val):
        if self.head is None:
            self.head=Node(val)
        else:
            n1=Node(val)
            n1.next=self.head
            self.head=n1

    def altdel(self,cur):
        while cur and cur.next:
            if cur.next.next:
                cur.next=cur.next.next
            cur=cur.next

    def recaltdel(self,cur):
        if cur and cur.next and cur.next.next:
            cur.next = cur.next.next
            self.recaltdel(cur.next)

class Node:
    def __init__(self,val):
        self.data=val
        self.next=None

if __name__ == '__main__':
    ll1=LL()
    ll1.push(30)
    ll1.push(20)
    ll1.push(10)
    #ll1.altdel(ll1.head)
    ll1.recaltdel(ll1.head)
    ll1.printll()
