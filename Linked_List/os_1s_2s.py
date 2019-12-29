class LL:
    def __init__(self):
        self.head=None
    def push(self,val):
        n_node=Node(val)
        n_node.next=self.head
        self.head=n_node
    def priint(self):
        temp=self.head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
        print()
    def countn(self):
        temp=self.head
        count=[0,0,0]
        while temp:
            count[temp.data]+=1
            temp=temp.next
        print(count)
        temp = self.head
        l=0
        while temp:
            if count[l]==0:
                l+=1
            else:
                temp.data=l
                count[l]-=1
                temp=temp.next

class Node:
    def __init__(self,val):
        self.data=val
        self.next=None

if __name__ == '__main__':
    ll1=LL()
    ll1.push(2)
    ll1.push(0)
    ll1.push(1)
    ll1.push(0)
    ll1.push(1)
    ll1.push(0)
    ll1.push(2)
    ll1.push(1)
    ll1.push(0)
    ll1.countn()

    ll1.priint()