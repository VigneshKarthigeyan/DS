#1->1 multiply 1->0 gives 110
#Remove all dup occurences in a ll
class LL:
    def __init__(self):
        self.head=None

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
    def convert_number(self,head):
        temp=head
        sum=0
        while temp:
            sum=10*sum
            sum+=temp.data
            temp=temp.next
        return sum
    def mulLL(self,h1,h2):
        a=self.convert_number(h1)
        b=self.convert_number(h2)
        print(a*b)

class Node:
    def __init__(self,val):
        self.data=val
        self.next=None

if __name__ == '__main__':
    ll1=LL()
    ll1.head=Node(5)
    ll1.append(2)
    ll1.append(3)
    ll1.printll()
    ll2=LL()
    ll2.head=Node(1)
    ll2.append(3)
    ll2.append(4)
    ll2.printll()
    LL().mulLL(ll1.head,ll2.head)
