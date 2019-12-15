#Add the user input data to Linked list
class Node:
    def __init__(self,val):
        self.data=val
        self.next=None

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

if __name__ == '__main__':
    ll1=LL()
    for i in range(0,4):
        x=int(input())
        if(i==0):
            n=Node(x)
            ll1.head=n
        else:
            ll1.append(x)
    ll1.printll()