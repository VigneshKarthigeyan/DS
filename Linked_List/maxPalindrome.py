class LL:
    def __init__(self):
        self.head=None
    def push(self,v):
        n=Node(v)
        n.next=self.head
        self.head=n
    def max(self,head):
        pre=None
        cur=head
        maxcount=0
        while cur:
            ocount=0
            ecount=0
            suf=cur.next
            cur.next=pre
            ctemp=cur
            stemp=suf
            while ctemp and stemp:
                print("loop")
                if ctemp.data == stemp.data:
                    ecount+=1
                ctemp=ctemp.next
                stemp=stemp.next
            ctemp = pre
            stemp = suf
            while ctemp and stemp:
                print("loop")
                if ctemp.data == stemp.data:
                    ocount+=1
                ctemp=ctemp.next
                stemp=stemp.next
            if ocount>ecount:
                count=(2*ocount)+1
            else:
                count=2*ecount
            if maxcount<count:
                print("2nd loop")
                maxcount=count

            print("outer")
            pre=cur
            cur=suf
        print(maxcount)
    def printll(self,head):
        temp=head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
        print()
class Node:
    def __init__(self,v):
        self.data=v
        self.next=None
if __name__ == '__main__':
    ll1=LL()
    ll1.push(12)
    ll1.push(4)
    ll1.push(4)
    ll1.push(3)
    ll1.push(14)
    ll1.printll(ll1.head)
    ll1.max(ll1.head)