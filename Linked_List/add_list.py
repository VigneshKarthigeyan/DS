#Get two integers as lists
#Add and display them
class LL:
    def __init__(self):
        self.head=None
    def print(self):
        temp=self.head
        while(temp is not None):
            print(temp.data,end='')
            temp=temp.next
        print()
    def push(self,val):
        n1=Node(val)
        n1.next=self.head
        self.head=n1

    def add(self,first,sec):
        prev=None
        n1=None
        carry=0
        while(first is not None or sec is not None):
            val1=0 if first is None else first.data
            val2=0 if sec is None else sec.data
            sum=val1+val2+carry

            if sum>=10:
                carry=1
            else:
                carry=0
            if(sum<10):
                sum=sum
            else:
                sum=sum%10
            n1=Node(sum)
            if self.head is None:
                self.head=n1
            else:
                prev.next=n1
            prev=n1
            if(first is not None):
                first=first.next
            if (sec is not None):
                sec = sec.next
        if carry>0:
            n1.next=Node(carry)
class Node:
    def __init__(self,val):
        self.data=val
        self.next=None

if __name__ == '__main__':
    ll1=LL()
    ll2=LL()
    ll3=LL()
    ll1.push(2)
    ll2.push(3)
    ll1.push(3)
    ll1.push(4)
    ll2.push(7)
    ll2.push(9)
    ll1.print()
    ll2.print()
    ll3.add(ll1.head,ll2.head)
    ll3.print()
