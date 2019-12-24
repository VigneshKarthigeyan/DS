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
        n1=Node(val)
        n1.next=self.head
        self.head=n1

    def append(self,val):
        n_node=Node(val)
        temp=self.head
        while(temp.next!=None):
            temp=temp.next
        temp.next=n_node

    def insatbeg(self,val):
        n_node = Node(val)
        n_node.next=self.head
        self.head=n_node

    def insafter(self,val,ind):
        n_node = Node(val)
        temp=self.head
        count=0
        while(temp.next!=None):
            if(count==ind-1):
                n_node.next=temp.next
                temp.next = n_node
                break
            count+=1
            temp=temp.next


    def deletebind(self,ind):
        temp = self.head
        count = 0
        while (temp!= None):
            if (count == ind-1):
                swap=temp.next
                temp.next = swap.next
                return
            count += 1
            temp=temp.next

    def deletebval(self,val):
        temp = self.head
        if(temp.data is val):
            self.head=temp.next
            return
        else:
            while (temp!= None):
                if (temp.data==val):
                    swap.next=temp.next
                    swap=None
                    return
                swap=temp
                temp=temp.next

    def swap(self,x,y):
        temp=self.head
        while(temp is not None):
            if(temp.data==x):
                curx=temp
                break
            prevx=temp
            temp=temp.next
        print("The prev and curr node of x is ",prevx.data,curx.data)
        while (temp is not None):
            if (temp.data == y):
                cury = temp
                break
            prevy = temp
            temp = temp.next
        print("The prev and curr node of y is ", prevy.data, cury.data)
        if prevx is not None:
            prevx.next=cury
        else:
            self.head=cury
        if prevy is not None:
            prevy.next=curx
        else:
            self.head=curx
        swap=curx.next
        curx.next=cury.next
        cury.next=swap

    def reverse(self):
        prev=None
        cur=self.head

        while cur!=None:
            suf = cur.next
            cur.next=prev
            prev=cur
            cur=suf
        self.head=prev

    def recrrev(self):
        return self.recrev(self.head,None)
    def recrev(self,cur,prev):
        if(cur.next is None):
            self.head=cur
            cur.next=prev
            return
        suf=cur.next
        cur.next=prev
        return self.recrev(suf,cur)


class Node:
    def __init__(self,val):
        self.data=val
        self.next=None

if __name__ == '__main__':
    ll1=LL()
    n1=Node(5)
    n2=Node(10)
    ll1.head=n1
    ll1.append(25)
    ll1.append(55)
    ll1.append(75)
    ll1.printll()
    ll1.insatbeg(1)
    ll1.printll()
    ll1.insafter(100,2)
    ll1.printll()
    ll1.deletebind(1)
    ll1.printll()
    ll1.deletebval(25)
    ll1.printll()
    ll1.swap(100,75)
    ll1.printll()
    ll1.recrrev()
    ll1.printll()
    ll1.reverse()
    ll1.printll()
