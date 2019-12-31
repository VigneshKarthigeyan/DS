#In a ll make all the even
#positions following odd
class LL:
    def __init__(self):
        self.head=None
    def OddEven_Position(self):
        odd=self.head
        even=self.head.next
        start=even
        while odd.next.next and even.next.next:
            odd.next=even.next
            odd=even.next
            even.next=odd.next
            even=odd.next
        if even.next!=None:
            odd.next=even.next
            odd=even.next
        even.next=None
        odd.next=start


    def push(self,val):
        n_node=Node(val)
        n_node.next=self.head
        self.head=n_node
    def printll(self):
        temp=self.head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
        print()

class Node:
    def __init__(self,val):
        self.data=val
        self.next=None

if __name__ == '__main__':
    ll1=LL()
    ll1.push(75)
    ll1.push(70)
    ll1.push(65)
    ll1.push(60)
    ll1.push(55)
    ll1.push(50)
    ll1.push(45)
    ll1.push(40)
    ll1.printll()
    ll1.OddEven_Position()
    ll1.printll()